# -*- coding: utf-8 -*-
"""Genera el blog a partir de tools/blog_posts.py:
  - /blog/<slug>.html   (un artículo por página)
  - /blog.html          (índice)
  - bloque "Del blog" en index.html (entre <!-- BLOG:INICIO --> y <!-- BLOG:FIN -->)
  - sitemap.xml

Uso (desde la raíz del repo):  python3 tools/build_blog.py
"""
import html, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from blog_posts import POSTS  # noqa: E402
from sitemap import write_sitemap  # noqa: E402

SITE = "https://muralia.cl"
e = lambda s: html.escape(s or "", quote=True)
T_POST = open(os.path.join(ROOT, "tools", "blog.template.html"), encoding="utf-8").read()
T_INDEX = open(os.path.join(ROOT, "tools", "blog-index.template.html"), encoding="utf-8").read()
PRODUCTS = {p["slug"]: p for c in json.load(open(os.path.join(ROOT, "products.json"), encoding="utf-8"))["categories"]
            for p in c["products"]}
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
ORG = {"@type": "Organization", "name": "Muralia", "url": SITE + "/",
       "logo": {"@type": "ImageObject", "url": SITE + "/logo-graphite.png"}}


def slugify(s):
    s = unicodedata.normalize("NFD", re.sub(r"<[^>]+>", "", s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def fecha(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} de {MESES[int(m) - 1]} de {y}"


def fill(tpl, rep):
    for k, v in rep.items():
        tpl = tpl.replace("{{" + k + "}}", v)
    left = re.findall(r"\{\{\w+\}\}", tpl)
    assert not left, left
    return tpl


def ld(*objs):
    return "\n".join('<script type="application/ld+json">\n' + json.dumps(o, ensure_ascii=False, indent=1) + "\n</script>"
                     for o in objs)


def card(p, level="h3"):
    src, w, h = p["image"]
    return (f'<a class="post-card" href="/blog/{p["slug"]}.html">'
            f'<img src="{src}" alt="{e(p["image_alt"])}" width="{w}" height="{h}" loading="lazy" decoding="async">'
            f'<div class="post-card-body"><span class="kicker">{e(p["kicker"])}</span>'
            f'<{level}>{e(p["h1"])}</{level}><p>{e(p["excerpt"])}</p>'
            f'<span class="post-meta">{fecha(p["date"])} · {p["read_min"]} min</span>'
            f'<span class="post-read">Leer artículo →</span></div></a>')


def prepare(p):
    # ids en los <h2> para el índice del artículo
    toc = []

    def add_id(m):
        text = m.group(1)
        sid = slugify(text)
        toc.append((sid, re.sub(r"<[^>]+>", "", text)))
        return f'<h2 id="{sid}">{text}</h2>'
    p["body_html"] = re.sub(r"<h2>(.*?)</h2>", add_id, p["body"])
    toc.append(("preguntas-frecuentes", "Preguntas frecuentes"))
    if p.get("sources"):
        toc.append(("fuentes", "Fuentes"))
    p["toc"] = toc
    words = len(re.sub(r"<[^>]+>", " ", p["body"]).split()) + sum(len((q + a).split()) for q, a in p["faq"])
    p["read_min"] = max(3, round(words / 200))
    for s in p["related"]:
        assert s in PRODUCTS, f"{p['slug']}: producto desconocido {s}"


def sources_html(p):
    # fuentes: (título, organismo/fabricante, url)
    if not p.get("sources"):
        return ""
    items = "".join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a> — {e(org)}</li>' for t, org, u in p["sources"])
    return ('        <div class="article-sources">\n          <h2 id="fuentes">Fuentes</h2>\n'
            f'          <ol>{items}</ol>\n'
            '          <p>Los valores citados corresponden a las fuentes indicadas a la fecha de publicación. '
            'Normas y fichas técnicas se actualizan: verifica siempre la versión vigente para tu proyecto.</p>\n        </div>')


def build_post(p, others):
    url = f"{SITE}/blog/{p['slug']}.html"
    src, w, h = p["image"]
    img_abs = SITE + src
    article_ld = {
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": p["h1"], "description": p["meta"], "image": [img_abs],
        "datePublished": p["date"], "dateModified": p.get("updated", p["date"]),
        "author": ORG, "publisher": ORG, "inLanguage": "es-CL",
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
    }
    if p.get("sources"):
        article_ld["citation"] = [s[2] for s in p["sources"]]
    crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog.html"},
        {"@type": "ListItem", "position": 3, "name": p["h1"], "item": url}]}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}
    extra = (f'<meta property="article:published_time" content="{p["date"]}">\n'
             f'<meta property="article:modified_time" content="{p.get("updated", p["date"])}">\n'
             f'<meta property="og:image:width" content="{w}">\n<meta property="og:image:height" content="{h}">')
    return fill(T_POST, {
        "TITLE": e(p["title"] + " | Muralia"), "META": e(p["meta"]), "URL": url, "OG_TYPE": "article",
        "IMG": e(img_abs), "IMG_ALT": e(p["image_alt"]), "EXTRA_META": extra,
        "JSONLD": ld(article_ld, crumbs_ld, faq_ld),
        "KICKER": e(p["kicker"]), "H1": e(p["h1"]), "DATE_ISO": p["date"], "DATE_TXT": fecha(p["date"]),
        "READ_MIN": str(p["read_min"]), "IMG_SRC": src, "IMG_W": str(w), "IMG_H": str(h),
        "BODY": p["body_html"],
        "FAQ": "".join(f'<details class="faq-item"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in p["faq"]),
        "SOURCES": sources_html(p),
        "TOC": "".join(f'<li><a href="#{sid}">{e(t)}</a></li>' for sid, t in p["toc"]),
        "RELATED": "".join(f'<a href="/productos/{s}.html"><span>{e(PRODUCTS[s]["name"])}</span><span class="arrow">&#8594;</span></a>'
                           for s in p["related"]),
        "MORE": "".join(card(o) for o in others),
    })


def build_index(posts):
    url = SITE + "/blog.html"
    meta = ("Guías técnicas sobre protección pasiva contra incendios, resistencia al fuego, sellos cortafuego, "
            "aislación térmica y acústica: normativa chilena y buenas prácticas.")
    blog_ld = {"@context": "https://schema.org", "@type": "Blog", "name": "Blog Muralia", "url": url,
               "inLanguage": "es-CL", "publisher": ORG,
               "blogPost": [{"@type": "BlogPosting", "headline": p["h1"], "url": f"{SITE}/blog/{p['slug']}.html",
                             "datePublished": p["date"]} for p in posts]}
    return fill(T_INDEX, {
        "TITLE": e("Blog: aislación y protección contra incendios | Muralia"), "META": e(meta), "URL": url,
        "OG_TYPE": "website", "IMG": SITE + posts[0]["image"][0], "IMG_ALT": e(posts[0]["image_alt"]), "EXTRA_META": "",
        "JSONLD": ld(blog_ld),
        "POSTS": "".join(card(p, "h2") for p in posts),
    })


def update_home(posts):
    path = os.path.join(ROOT, "index.html")
    s = open(path, encoding="utf-8").read()
    a, b = "<!-- BLOG:INICIO -->", "<!-- BLOG:FIN -->"
    if a not in s:
        print("  (index.html no tiene el bloque del blog; se omite)")
        return
    block = (f'{a}\n      <div class="post-grid">' + "".join(card(p) for p in posts[:3]) + f'</div>\n      {b}')
    s = re.sub(re.escape(a) + r".*?" + re.escape(b), lambda m: block, s, flags=re.S)
    open(path, "w", encoding="utf-8").write(s)


posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)  # orden estable: a igual fecha, el orden de POSTS
for p in posts:
    prepare(p)
os.makedirs(os.path.join(ROOT, "blog"), exist_ok=True)
for i, p in enumerate(posts):
    others = [o for o in posts if o is not p][:3]
    with open(os.path.join(ROOT, "blog", p["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(build_post(p, others))
with open(os.path.join(ROOT, "blog.html"), "w", encoding="utf-8") as f:
    f.write(build_index(posts))
update_home(posts)
n = write_sitemap()
print(f"{len(posts)} artículos + blog.html + sitemap.xml ({n} URLs)")
