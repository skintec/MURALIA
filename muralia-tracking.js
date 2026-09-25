/* ============================================================
   MURALIA — Eventos de Google Analytics (GA4)
   ------------------------------------------------------------
   Registra en GA las acciones de contacto que la etiqueta de
   Google no mide sola:
     - generate_lead   clic en "Enviar por correo" (#cart-email-btn)
     - click_telefono  clic en un enlace tel:
     - click_email     clic en un enlace mailto:
     - add_to_quote    producto agregado al carrito de cotización
   Los clics en WhatsApp (click_whatsapp) se crean en GA a partir
   de los clics salientes, así que no se envían desde aquí.
   Debe cargarse después de cart.js (ambos con defer).
   ============================================================ */

(function () {
  "use strict";

  function track(name, params) {
    if (typeof window.gtag !== "function") return;
    params = params || {};
    // beacon: el evento se envía aunque la página cambie (mailto:, tel:)
    params.transport_type = "beacon";
    window.gtag("event", name, params);
  }

  function cartItems() {
    return window.MuraliaCart ? window.MuraliaCart.getItems() : [];
  }

  function toGaItem(item) {
    var variant = [item.thickness, item.density, item.finish].filter(Boolean).join(" / ");
    var gaItem = {
      item_id: item.slug,
      item_name: item.name,
      quantity: item.qty || 1
    };
    if (item.category) gaItem.item_category = item.category;
    if (variant) gaItem.item_variant = variant;
    return gaItem;
  }

  // add_to_quote: envuelve MuraliaCart.addItem sin cambiar su comportamiento
  if (window.MuraliaCart && typeof window.MuraliaCart.addItem === "function") {
    var originalAddItem = window.MuraliaCart.addItem;
    window.MuraliaCart.addItem = function (item) {
      var result = originalAddItem.apply(this, arguments);
      try {
        track("add_to_quote", { items: [toGaItem(item)] });
      } catch (e) { /* la medición nunca debe romper el carrito */ }
      return result;
    };
  }

  document.addEventListener("click", function (event) {
    var link = event.target.closest ? event.target.closest("a[href]") : null;
    if (!link) return;
    var href = link.getAttribute("href") || "";

    try {
      if (link.id === "cart-email-btn") {
        var items = cartItems();
        if (!items.length) return;
        var products = items.map(function (i) { return i.name; }).join(", ");
        track("generate_lead", {
          lead_source: "cotizacion_email",
          items: items.map(toGaItem),
          product_count: items.length,
          products: products.slice(0, 100)
        });
      } else if (/^tel:/i.test(href)) {
        track("click_telefono", {
          phone_number: href.replace(/^tel:/i, ""),
          page_location: location.href
        });
      } else if (/^mailto:/i.test(href)) {
        track("click_email", {
          email_address: href.replace(/^mailto:/i, "").split("?")[0],
          page_location: location.href
        });
      }
    } catch (e) { /* silencioso */ }
  }, true);
})();
