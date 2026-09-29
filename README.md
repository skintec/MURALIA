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

## Historial de cotizaciones (Cloudflare Worker)
Las cotizaciones se guardan en `cotizaciones/data.json`. El generador escribe ahí a través de un Worker de Cloudflare (`tools/cloudflare-worker.js`) que guarda el token de GitHub como secreto, así ningún dispositivo necesita configurarlo.

1. Crea un token fine-grained en GitHub (solo `skintec/MURALIA`, permiso Contents: Read and write).
2. Cloudflare → Workers & Pages → Create Worker → pega `tools/cloudflare-worker.js` → Deploy.
3. En el Worker → Settings → Variables and Secrets: agrega el secreto `GITHUB_TOKEN`. Opcional: `ACCESS_KEY` (clave corta; cada dispositivo la pide una vez en Historial → Configurar acceso).
4. Copia la URL del Worker (`https://…workers.dev`) en `WORKER_URL` dentro de `generador.html`.
