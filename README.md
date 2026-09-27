# MURALIA
www.muralia.cl/index.html#ver    https://muralia.cl/generador.html    https://github.com/skintec/oc

## SEO: fichas de producto estáticas
Las fichas viven en `/productos/<slug>.html` y se generan con:

    python3 tools/build_product_pages.py

Ejecútalo cada vez que cambies `products.json` o `tools/seo_content.py` (títulos, meta descripciones, usos y preguntas frecuentes). También regenera `sitemap.xml`. `producto.html?slug=` quedó como redirección.

## Blog
Los artículos viven en `/blog/<slug>.html` y el índice en `/blog.html`. Se generan con:

    python3 tools/build_blog.py

Para publicar un artículo nuevo, agrégalo en `tools/blog_posts.py` (las instrucciones están al inicio del archivo), deja su foto principal en `img/blog/` y ejecuta el comando. También actualiza el bloque "Guías técnicas" del inicio y `sitemap.xml`. Los créditos de fotos externas van en `img/blog/CREDITOS.md`.
