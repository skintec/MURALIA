# MURALIA
www.muralia.cl/index.html#ver
https://muralia.cl/generador.html

## SEO: fichas de producto estáticas
Las fichas viven en `/productos/<slug>.html` y se generan con:

    python3 tools/build_product_pages.py

Ejecútalo cada vez que cambies `products.json` o `tools/seo_content.py` (títulos, meta descripciones, usos y preguntas frecuentes). También regenera `sitemap.xml`. `producto.html?slug=` quedó como redirección.
