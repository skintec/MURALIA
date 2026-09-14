/* ============================================================
   MURALIA — Superposición "Sitio en construcción"
   ------------------------------------------------------------
   Cómo usar:
   1) Sube este archivo a la raíz del repo (junto a index.html).
   2) En CADA página que quieras cubrir (index.html, empresa.html,
      productos.html, contacto.html, presencia.html) agrega esta
      línea justo antes de </head>:

        <script src="construccion.js" defer></script>

   3) Listo. La superposición se dibuja arriba de todo el sitio,
      el contenido real queda intacto debajo, sin tocarlo.

   Para quitarla cuando el sitio esté listo:
   - Opción rápida: borra este archivo (construccion.js) del repo.
     Las etiquetas <script> que quedan en las páginas no rompen
     nada (el navegador simplemente no encuentra el archivo).
   - Opción prolija: además borra esa misma línea <script> de
     cada página.

   Para revisar el sitio real mientras la superposición está
   activa (sin publicar el cambio), agrega #ver al final de la
   URL, por ejemplo: muralia.cl/index.html#ver
   ============================================================ */

(function () {
  "use strict";

  // Escape hatch para previsualizar el sitio real mientras se trabaja
  if (window.location.hash === "#ver") return;

  var FONT_LINK_ID = "muralia-construccion-fonts";
  if (!document.getElementById(FONT_LINK_ID)) {
    var fontLink = document.createElement("link");
    fontLink.id = FONT_LINK_ID;
    fontLink.rel = "stylesheet";
    fontLink.href =
      "https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;500;600&display=swap";
    document.head.appendChild(fontLink);
  }

  var style = document.createElement("style");
  style.id = "muralia-construccion-styles";
  style.textContent = [
    "html.muralia-construccion-lock, body.muralia-construccion-lock {",
    "  overflow: hidden !important;",
    "  height: 100% !important;",
    "}",
    "#muralia-construccion-overlay {",
    "  position: fixed;",
    "  inset: 0;",
    "  z-index: 2147483647;",
    "  display: flex;",
    "  align-items: center;",
    "  justify-content: center;",
    "  background-color: #EFE7DA;",
    "  background-image:",
    "    linear-gradient(rgba(43,42,38,0.05) 1px, transparent 1px),",
    "    linear-gradient(90deg, rgba(43,42,38,0.05) 1px, transparent 1px);",
    "  background-size: 40px 40px;",
    "  padding: 24px;",
    "  box-sizing: border-box;",
    "}",
    "#muralia-construccion-overlay * { box-sizing: border-box; }",
    "#muralia-construccion-card {",
    "  width: 100%;",
    "  max-width: 560px;",
    "  background: #FFFDF9;",
    "  border: 2px solid #2B2A26;",
    "  padding: 48px 40px;",
    "  text-align: center;",
    "  font-family: 'Oswald', Arial, sans-serif;",
    "}",
    "#muralia-construccion-mark {",
    "  display: inline-block;",
    "  border: 3px solid #2B2A26;",
    "  padding: 10px 22px;",
    "  margin-bottom: 28px;",
    "}",
    "#muralia-construccion-mark span {",
    "  display: block;",
    "  font-family: 'Anton', 'Arial Narrow', sans-serif;",
    "  font-size: 30px;",
    "  line-height: 1.05;",
    "  letter-spacing: 2px;",
    "  color: #C2551F;",
    "}",
    "#muralia-construccion-label {",
    "  font-family: 'Oswald', Arial, sans-serif;",
    "  font-size: 12px;",
    "  font-weight: 600;",
    "  letter-spacing: 3px;",
    "  text-transform: uppercase;",
    "  color: #9c4318;",
    "  margin: 0 0 14px;",
    "}",
    "#muralia-construccion-title {",
    "  font-family: 'Anton', 'Arial Narrow', sans-serif;",
    "  font-weight: normal;",
    "  font-size: clamp(26px, 5vw, 36px);",
    "  line-height: 1.15;",
    "  color: #2B2A26;",
    "  margin: 0 0 16px;",
    "}",
    "#muralia-construccion-text {",
    "  font-size: 16px;",
    "  line-height: 1.5;",
    "  color: #3E4A3C;",
    "  margin: 0 0 28px;",
    "}",
    "#muralia-construccion-cta {",
    "  display: inline-block;",
    "  font-family: 'Oswald', Arial, sans-serif;",
    "  font-weight: 600;",
    "  font-size: 14px;",
    "  letter-spacing: 1px;",
    "  text-transform: uppercase;",
    "  text-decoration: none;",
    "  color: #FFFDF9;",
    "  background: #C2551F;",
    "  padding: 14px 28px;",
    "  border: 2px solid #C2551F;",
    "  transition: background 0.15s ease, color 0.15s ease;",
    "}",
    "#muralia-construccion-cta:hover {",
    "  background: #9c4318;",
    "  border-color: #9c4318;",
    "}",
    "#muralia-construccion-foot {",
    "  margin-top: 24px;",
    "  font-size: 12px;",
    "  letter-spacing: 0.5px;",
    "  color: #3E4A3C;",
    "  opacity: 0.75;",
    "}"
  ].join("\n");
  document.head.appendChild(style);

  var overlay = document.createElement("div");
  overlay.id = "muralia-construccion-overlay";
  overlay.setAttribute("role", "dialog");
  overlay.setAttribute("aria-label", "Sitio en construcción");
  overlay.innerHTML = [
    '<div id="muralia-construccion-card">',
    '  <div id="muralia-construccion-mark"><span>MUR</span><span>ALIA</span></div>',
    '  <p id="muralia-construccion-label">Sitio en construcción</p>',
    "  <h1 id=\"muralia-construccion-title\">Estamos renovando nuestro sitio</h1>",
    '  <p id="muralia-construccion-text">Estamos actualizando la información de esta página. Muy pronto vas a encontrar todo al día.</p>',
    '  <a id="muralia-construccion-cta" href="mailto:contacto@muralia.cl">Escríbenos</a>',
    '  <p id="muralia-construccion-foot">© 2026 Muralia</p>',
    "</div>"
  ].join("\n");

  function mount() {
    document.documentElement.classList.add("muralia-construccion-lock");
    document.body.classList.add("muralia-construccion-lock");
    document.body.appendChild(overlay);
  }

  if (document.body) {
    mount();
  } else {
    document.addEventListener("DOMContentLoaded", mount);
  }
})();
