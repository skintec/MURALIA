# -*- coding: utf-8 -*-
"""Genera sitemap.xml con las páginas fijas, las fichas de producto y el blog.
Lo llaman tools/build_product_pages.py y tools/build_blog.py."""
import datetime, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://muralia.cl"


def write_sitemap():
    today = datetime.date.today().isoformat()
    productos = sorted(glob.glob(os.path.join(ROOT, "productos", "*.html")))
    posts = sorted(glob.glob(os.path.join(ROOT, "blog", "*.html")))
    pages = [SITE + "/", SITE + "/productos.html", SITE + "/empresa.html", SITE + "/contacto.html"]
    pages += [f"{SITE}/productos/{os.path.basename(p)}" for p in productos]
    if posts:
        pages += [SITE + "/blog.html"] + [f"{SITE}/blog/{os.path.basename(p)}" for p in posts]
    pages += [SITE + "/privacidad.html"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in pages]
    sm.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm) + "\n")
    return len(pages)
