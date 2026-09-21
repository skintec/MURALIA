/* ============================================================
   MURALIA — Carrito de cotización (localStorage, sin backend)
   ------------------------------------------------------------
   Guarda los productos que el cliente quiere cotizar en el
   navegador. Al terminar, genera un correo (mailto:) con el
   detalle de todo lo agregado, dirigido a ventas@muralia.cl.
   ============================================================ */

(function () {
  "use strict";

  var KEY = "muralia_cotizacion_v1";
  var EMAIL = "ventas@muralia.cl";

  function getItems() {
    try {
      var raw = localStorage.getItem(KEY);
      return raw ? JSON.parse(raw) : [];
    } catch (e) {
      return [];
    }
  }

  function setItems(items) {
    try {
      localStorage.setItem(KEY, JSON.stringify(items));
    } catch (e) {
      /* localStorage no disponible (modo privado, etc.) — silencioso */
    }
    updateBadges();
  }

  function addItem(item) {
    var items = getItems();
    var exists = items.some(function (i) {
      return i.slug === item.slug && i.thickness === item.thickness;
    });
    if (!exists) {
      items.push(item);
      setItems(items);
    }
    return !exists;
  }

  function removeItem(index) {
    var items = getItems();
    items.splice(index, 1);
    setItems(items);
  }

  function clearItems() {
    setItems([]);
  }

  function updateBadges() {
    var count = getItems().length;
    document.querySelectorAll(".cart-count").forEach(function (el) {
      el.textContent = String(count);
      el.style.display = count > 0 ? "" : "none";
    });
  }

  function buildMailto(items, note) {
    var subject = "Solicitud de cotización - Muralia";
    var lines = ["Hola, quisiera cotizar los siguientes productos:", ""];
    items.forEach(function (item, i) {
      var line = (i + 1) + ". " + item.name;
      if (item.thickness) line += " — Espesor: " + item.thickness;
      if (item.category) line += " (" + item.category + ")";
      lines.push(line);
    });
    lines.push("");
    if (note) { lines.push(note); lines.push(""); }
    lines.push("Nombre:");
    lines.push("Teléfono:");
    lines.push("Comuna / dirección de despacho (opcional):");
    var body = lines.join("\n");
    return "mailto:" + EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
  }

  window.MuraliaCart = {
    getItems: getItems,
    addItem: addItem,
    removeItem: removeItem,
    clearItems: clearItems,
    updateBadges: updateBadges,
    buildMailto: buildMailto
  };

  document.addEventListener("DOMContentLoaded", updateBadges);
})();
