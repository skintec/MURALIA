// Cloudflare Worker: puente entre el generador y cotizaciones/data.json en GitHub.
// El token de GitHub vive aquí como secreto (GITHUB_TOKEN) y nunca llega al navegador ni al repositorio.
// Variables: GITHUB_TOKEN (secreto, obligatorio) · ACCESS_KEY (secreto, opcional: clave corta que el generador envía).
const REPO = "skintec/MURALIA", BRANCH = "main", PATH = "cotizaciones/data.json";
const ORIGINS = ["https://muralia.cl", "https://www.muralia.cl"];
const MAX_BYTES = 4 * 1024 * 1024;

export default {
  async fetch(req, env) {
    const origin = req.headers.get("Origin") || "";
    const allowed = ORIGINS.includes(origin);
    const cors = {
      "Access-Control-Allow-Origin": allowed ? origin : ORIGINS[0],
      "Access-Control-Allow-Methods": "GET, PUT, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, X-Muralia-Key",
      "Vary": "Origin",
    };
    const reply = (body, status = 200) => new Response(body, { status, headers: { ...cors, "Content-Type": "application/json" } });
    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    if (!allowed) return reply('{"error":"origen no permitido"}', 403);
    if (env.ACCESS_KEY && req.headers.get("X-Muralia-Key") !== env.ACCESS_KEY) return reply('{"error":"clave incorrecta"}', 401);

    const url = `https://api.github.com/repos/${REPO}/contents/${PATH}`;
    const gh = { Authorization: `Bearer ${env.GITHUB_TOKEN}`, Accept: "application/vnd.github+json", "User-Agent": "muralia-worker" };

    if (req.method === "GET") {
      const r = await fetch(`${url}?ref=${BRANCH}`, { headers: gh });
      return reply(await r.text(), r.status);
    }
    if (req.method === "PUT") {
      const text = await req.text();
      if (text.length > MAX_BYTES * 1.4) return reply('{"error":"demasiado grande"}', 413);
      let b;
      try { b = JSON.parse(text); JSON.parse(atob(b.content.replace(/\s/g, "")) ); } catch (e) { return reply('{"error":"formato inválido"}', 400); }
      // Solo se puede escribir ESE archivo, en esa rama; el cliente no elige ruta ni rama.
      const body = { message: String(b.message || "Cotizaciones").slice(0, 200), content: b.content, branch: BRANCH };
      if (b.sha) body.sha = b.sha;
      const r = await fetch(url, { method: "PUT", headers: { ...gh, "Content-Type": "application/json" }, body: JSON.stringify(body) });
      return reply(await r.text(), r.status);
    }
    return reply('{"error":"método no permitido"}', 405);
  },
};
