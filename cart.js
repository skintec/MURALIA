/* ============================================================
   MURALIA — Carrito de cotización (localStorage, sin backend)
   ------------------------------------------------------------
   Guarda los productos que el cliente quiere cotizar en el
   navegador, con la cantidad que necesita de cada uno. Al
   terminar, genera un correo (mailto:) con el detalle completo,
   dirigido a ventas@muralia.cl.
   ============================================================ */

(function () {
  "use strict";

  var KEY = "muralia_cotizacion_v1";
  var EMAIL = "ventas@muralia.cl";

  function getItems() {
    try {
      var raw = localStorage.getItem(KEY);
      var items = raw ? JSON.parse(raw) : [];
      // compatibilidad con carritos guardados antes de tener cantidad
      items.forEach(function (i) { if (!i.qty) i.qty = 1; });
      return items;
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
    var qty = item.qty && item.qty > 0 ? item.qty : 1;
    var existing = items.find(function (i) {
      return i.slug === item.slug && i.thickness === item.thickness && i.density === item.density;
    });
    if (existing) {
      existing.qty = (existing.qty || 1) + qty;
    } else {
      item.qty = qty;
      items.push(item);
    }
    setItems(items);
    return true;
  }

  function updateQty(index, qty) {
    var items = getItems();
    if (!items[index]) return;
    qty = parseInt(qty, 10);
    items[index].qty = (isNaN(qty) || qty < 1) ? 1 : qty;
    setItems(items);
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
    var items = getItems();
    var count = items.reduce(function (sum, i) { return sum + (i.qty || 1); }, 0);
    document.querySelectorAll(".cart-count").forEach(function (el) {
      el.textContent = String(count);
      el.style.display = count > 0 ? "" : "none";
    });
  }

  function buildMailto(items, note) {
    var subject = "Solicitud de cotización - Muralia";
    var lines = ["Hola, quisiera cotizar los siguientes productos:", ""];
    items.forEach(function (item, i) {
      var qty = item.qty || 1;
      var line = (i + 1) + ". " + item.name + " — Cantidad: " + qty;
      if (item.thickness) line += " — Espesor: " + item.thickness;
      if (item.density) line += " — Densidad: " + item.density;
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
    updateQty: updateQty,
    removeItem: removeItem,
    clearItems: clearItems,
    updateBadges: updateBadges,
    buildMailto: buildMailto
  };

  document.addEventListener("DOMContentLoaded", updateBadges);
})();
