/* ============================================================
   MURALIA — Superposición "Sitio en construcción" (v2)
   ------------------------------------------------------------
   Igual que antes: sube este archivo a la raíz del repo y
   agrega <script src="construccion.js" defer></script> antes
   de </head> en cada página que quieras cubrir.

   Para quitarla: borra este archivo del repo.
   Para previsualizar el sitio real: agrega #ver a la URL.

   Novedades v2:
   - Usa el logo real del repo (logo-graphite.png) en vez de
     dibujar un cuadrado propio.
   - Fondo de grilla con desplazamiento lento.
   - Punto pulsante junto a la etiqueta.
   - Franja de rayas diagonales animada.
   - Entrada con fade suave. Respeta prefers-reduced-motion.
   ============================================================ */

(function () {
  "use strict";

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
    "    linear-gradient(rgba(43,42,38,0.06) 1px, transparent 1px),",
    "    linear-gradient(90deg, rgba(43,42,38,0.06) 1px, transparent 1px);",
    "  background-size: 40px 40px;",
    "  animation: muralia-grid-drift 6s linear infinite;",
    "  padding: 24px;",
    "  box-sizing: border-box;",
    "}",
    "#muralia-construccion-overlay * { box-sizing: border-box; }",
    "#muralia-construccion-card {",
    "  width: 100%;",
    "  max-width: 560px;",
    "  background: #FFFDF9;",
    "  border: 2px solid #2B2A26;",
    "  overflow: hidden;",
    "  text-align: center;",
    "  font-family: 'Oswald', Arial, sans-serif;",
    "  animation: muralia-fade-up 0.6s ease both;",
    "}",
    "#muralia-construccion-stripes {",
    "  height: 10px;",
    "  width: 100%;",
    "  background-image: repeating-linear-gradient(",
    "    -45deg,",
    "    #C2551F, #C2551F 14px,",
    "    #2B2A26 14px, #2B2A26 28px",
    "  );",
    "  background-size: 200% 100%;",
    "  animation: muralia-stripes 3s linear infinite;",
    "}",
    "#muralia-construccion-inner { padding: 44px 40px 48px; }",
    "#muralia-construccion-logo {",
    "  height: 56px;",
    "  width: auto;",
    "  margin-bottom: 28px;",
    "}",
    "#muralia-construccion-logo-fallback {",
    "  display: none;",
    "  font-family: 'Anton', 'Arial Narrow', sans-serif;",
    "  font-size: 28px;",
    "  letter-spacing: 2px;",
    "  color: #2B2A26;",
    "  margin-bottom: 28px;",
    "}",
    "#muralia-construccion-label {",
    "  display: flex;",
    "  align-items: center;",
    "  justify-content: center;",
    "  gap: 8px;",
    "  font-family: 'Oswald', Arial, sans-serif;",
    "  font-size: 12px;",
    "  font-weight: 600;",
    "  letter-spacing: 3px;",
    "  text-transform: uppercase;",
    "  color: #9c4318;",
    "  margin: 0 0 14px;",
    "}",
    "#muralia-construccion-dot {",
    "  width: 7px;",
    "  height: 7px;",
    "  border-radius: 50%;",
    "  background: #C2551F;",
    "  animation: muralia-pulse 1.6s ease-in-out infinite;",
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
    "}",
    "@keyframes muralia-grid-drift {",
    "  from { background-position: 0 0, 0 0; }",
    "  to   { background-position: 40px 40px, 40px 40px; }",
    "}",
    "@keyframes muralia-stripes {",
    "  from { background-position: 0 0; }",
    "  to   { background-position: 56px 0; }",
    "}",
    "@keyframes muralia-pulse {",
    "  0%, 100% { opacity: 1; transform: scale(1); }",
    "  50% { opacity: 0.35; transform: scale(0.7); }",
    "}",
    "@keyframes muralia-fade-up {",
    "  from { opacity: 0; transform: translateY(16px); }",
    "  to   { opacity: 1; transform: translateY(0); }",
    "}",
    "@media (prefers-reduced-motion: reduce) {",
    "  #muralia-construccion-overlay,",
    "  #muralia-construccion-stripes,",
    "  #muralia-construccion-dot,",
    "  #muralia-construccion-card {",
    "    animation: none !important;",
    "  }",
    "}"
  ].join("\n");
  document.head.appendChild(style);

  var overlay = document.createElement("div");
  overlay.id = "muralia-construccion-overlay";
  overlay.setAttribute("role", "dialog");
  overlay.setAttribute("aria-label", "Sitio en construcción");
  overlay.innerHTML = [
    '<div id="muralia-construccion-card">',
    '  <div id="muralia-construccion-stripes"></div>',
    '  <div id="muralia-construccion-inner">',
    '    <img id="muralia-construccion-logo" src="/logo-graphite.png" alt="Muralia" ' +
      'onerror="this.style.display=\'none\'; document.getElementById(\'muralia-construccion-logo-fallback\').style.display=\'block\';">',
    '    <div id="muralia-construccion-logo-fallback">MURALIA</div>',
    '    <p id="muralia-construccion-label"><span id="muralia-construccion-dot"></span>Sitio en construcción</p>',
    '    <h1 id="muralia-construccion-title">Estamos renovando nuestro sitio</h1>',
    '    <p id="muralia-construccion-text">Estamos actualizando la información de esta página. Muy pronto vas a encontrar todo al día.</p>',
    '    <a id="muralia-construccion-cta" href="mailto:ventas@muralia.cl">Escríbenos</a>',
    '    <p id="muralia-construccion-foot">© 2026 Muralia</p>',
    "  </div>",
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
