# -*- coding: utf-8 -*-
"""Descarga las imágenes que el sitio carga desde otros dominios (Unsplash, ayrsa.cl),
las guarda en img/ y reemplaza todas las referencias por la ruta local.

Uso (desde la raíz del repo):  python3 tools/descargar_imagenes_externas.py
Luego:                           python3 tools/build_product_pages.py
"""
import glob, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# Nombre local de cada foto externa (el ancho pedido se agrega al nombre: base-760.jpg)
NOMBRES = {
    "photo-1508450859948-4e04fabaa4ea": "img/hero-obra",          # fondo del inicio
    "photo-1527335988388-b40ee248d80c": "img/obra-estructura",    # inicio (nosotros) y Empresa
    "photo-1600965581129-eef8a214ec9d": "img/contacto-obra",      # Contacto
    "photo-1704742950992-9815a104820c": "img/cat-tabiques",       # Productos: tabiques y cielos
}
AYRSA = {"https://ayrsa.cl/wp-content/uploads/2016/08/lana-mineral-roca.jpg": "img/productos/lana-mineral.jpg"}

ARCHIVOS = [f for f in glob.glob("*.html") + glob.glob("productos/*.html") +
            ["styles.css", "products.json", "tools/producto.template.html"] if os.path.exists(f)]
URL_UNSPLASH = re.compile(r"https://images\.unsplash\.com/(photo-[0-9a-f-]+)\?[^'\"\s)]*")


def local_de(url):
    if url in AYRSA:
        return AYRSA[url]
    m = URL_UNSPLASH.fullmatch(url)
    if not m or m.group(1) not in NOMBRES:
        return None
    w = re.search(r"[?&]w=(\d+)", url)
    return f"{NOMBRES[m.group(1)]}-{w.group(1) if w else 'orig'}.jpg"


def descargar(url, destino):
    if os.path.exists(destino):
        return
    # fm=jpg: Unsplash entrega JPG (con auto=format podría responder AVIF/WebP)
    pedir = url + "&fm=jpg" if "unsplash" in url and "fm=" not in url else url
    req = urllib.request.Request(pedir, headers={"User-Agent": "Mozilla/5.0 (muralia.cl)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    if not data.startswith(b"\xff\xd8"):
        sys.exit(f"La respuesta de {url} no es un JPG; no se modificó nada.")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "wb") as f:
        f.write(data)
    print(f"  {destino}  ({len(data)//1024} KB)")


urls = set()
for f in ARCHIVOS:
    s = open(f, encoding="utf-8").read()
    urls.update(m.group(0) for m in URL_UNSPLASH.finditer(s))
    urls.update(u for u in AYRSA if u in s)

mapa = {u: local_de(u) for u in sorted(urls)}
sin_nombre = [u for u, l in mapa.items() if not l]
if sin_nombre:
    sys.exit("Faltan nombres locales para:\n  " + "\n  ".join(sin_nombre))

print("Descargando", len(mapa), "imágenes…")
for u, l in mapa.items():
    descargar(u, l)

print("Reemplazando referencias…")
for f in ARCHIVOS:
    s = o = open(f, encoding="utf-8").read()
    for u, l in mapa.items():
        # en styles.css la ruta es relativa a él (está en la raíz); en HTML y JSON, absoluta del sitio
        s = s.replace(u, l if f == "styles.css" else "/" + l)
    s = re.sub(r'<link rel="preconnect" href="https://images\.unsplash\.com">\n', "", s)
    if s != o:
        open(f, "w", encoding="utf-8").write(s)
        print("  " + f)
print("Listo. Ahora ejecuta: python3 tools/build_product_pages.py")
