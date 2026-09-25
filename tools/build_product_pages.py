# -*- coding: utf-8 -*-
"""Genera una página HTML estática por producto en /productos/<slug>.html
a partir de products.json + tools/seo_content.py + la plantilla producto.template.html.

Uso (desde la raíz del repo):  python3 tools/build_product_pages.py
Vuelve a ejecutarlo cada vez que cambies products.json o seo_content.py.
También regenera sitemap.xml.
"""
import json, os, re, html, datetime, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from seo_content import CONTENT  # noqa: E402

SITE = "https://muralia.cl"
TEMPLATE = open(os.path.join(ROOT, "tools", "producto.template.html"), encoding="utf-8").read()
data = json.load(open(os.path.join(ROOT, "products.json"), encoding="utf-8"))
e = lambda s: html.escape(s or "", quote=True)

DIM_LABELS = [("type", "Tipos"), ("thickness", "Espesores"), ("density", "Densidades"), ("finish", "Recubrimientos")]


def abs_img(src):
    return src if src.startswith("http") else SITE + "/" + src.lstrip("/")


def availability(p):
    out = []
    for dim, label in DIM_LABELS:
        vals = []
        for v in p.get("variants", []):
            if v.get(dim) and v[dim] not in vals:
                vals.append(v[dim])
        if vals:
            out.append((label, ", ".join(vals)))
    if p.get("custom_dims"):
        out.append(("Medidas a pedido", "sí, indica espesor o densidad en tu cotización"))
    return out


def build(cat, p, siblings):
    c = CONTENT[p["slug"]]
    url = f"{SITE}/productos/{p['slug']}.html"
    title = f"{c['title']} | Muralia"
    img = abs_img(p["media"]["src"])

    product_ld = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": p["name"],
        "description": p["desc"],
        "image": img,
        "url": url,
        "category": cat["name"],
        "additionalProperty": [{"@type": "PropertyValue", "name": k, "value": v} for k, v in p.get("base_specs", [])],
    }
    crumbs_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Productos", "item": SITE + "/productos.html"},
            {"@type": "ListItem", "position": 3, "name": p["name"], "item": url},
        ],
    }
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]],
    }
    ld = "\n".join(
        '<script type="application/ld+json">\n' + json.dumps(x, ensure_ascii=False, indent=1) + "\n</script>"
        for x in (product_ld, crumbs_ld, faq_ld)
    )

    specs = "".join(f"<li><b>{e(k)}:</b> {e(v)}</li>" for k, v in availability(p))
    base = "".join(f"<li><b>{e(k)}:</b> {e(v)}</li>" for k, v in p.get("base_specs", []))
    uses = "".join(f"<li>{e(u)}</li>" for u in c["uses"])
    faqs = "".join(
        f'<details class="faq-item"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in c["faq"]
    )
    related = "".join(
        f'<a href="/productos/{s["slug"]}.html"><span>{e(s["name"])}</span><span class="arrow">&#8594;</span></a>'
        for s in siblings if s["slug"] != p["slug"]
    )
    media = f'<img src="{e(p["media"]["src"])}" alt="{e(p["media"].get("alt") or p["name"])}">'

    rep = {
        "{{TITLE}}": e(title),
        "{{META}}": e(c["meta"]),
        "{{URL}}": url,
        "{{IMG}}": e(img),
        "{{IMG_ALT}}": e(p["media"].get("alt") or p["name"]),
        "{{JSONLD}}": ld,
        "{{NAME}}": e(p["name"]),
        "{{CAT}}": e(cat["name"]),
        "{{CAT_ID}}": e(cat["id"]),
        "{{SHORT}}": e(p["short"]),
        "{{DESC}}": e(p["desc"]),
        "{{MEDIA}}": media,
        "{{AVAIL}}": specs,
        "{{BASE}}": base,
        "{{USES}}": uses,
        "{{FAQ}}": faqs,
        "{{RELATED}}": related,
        "{{SLUG}}": p["slug"],
    }
    out = TEMPLATE
    for k, v in rep.items():
        out = out.replace(k, v)
    assert "{{" not in out, re.findall(r"\{\{\w+\}\}", out)
    return out


os.makedirs(os.path.join(ROOT, "productos"), exist_ok=True)
urls = []
for cat in data["categories"]:
    for p in cat["products"]:
        with open(os.path.join(ROOT, "productos", p["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(build(cat, p, cat["products"]))
        urls.append(f"{SITE}/productos/{p['slug']}.html")

# sitemap.xml
today = datetime.date.today().isoformat()
pages = [SITE + "/", SITE + "/productos.html", SITE + "/empresa.html", SITE + "/contacto.html"] + urls + [SITE + "/privacidad.html"]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in pages]
sm.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")
print(f"{len(urls)} páginas de producto + sitemap.xml ({len(pages)} URLs)")
