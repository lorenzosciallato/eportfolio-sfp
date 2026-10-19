/* E-Portfolio SFP — salvataggio dei profili su Cloudflare R2.
   Il profilo si ritrova con il numero di matricola. Nello spazio dati la matricola
   non compare mai in chiaro: ogni profilo è salvato sotto un codice ricavato dalla
   matricola e da una frase segreta (PEPE) che conosce solo il Worker. */

const MATRICOLA = /^[0-9]{4,10}$/;
const ID_IMG = /^[a-z0-9]{6,32}$/;
const MAX_TESTO = 400 * 1024;        // testi del profilo
const MAX_IMG = 3 * 1024 * 1024;     // una foto (già compressa dall'app)

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, PUT, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  "Access-Control-Max-Age": "86400"
};
const risposta = (corpo, stato = 200, tipo = "application/json") =>
  new Response(typeof corpo === "string" ? corpo : JSON.stringify(corpo), {
    status: stato, headers: { ...CORS, "Content-Type": tipo, "Cache-Control": "no-store" }
  });

async function codice(matricola, pepe){
  const dati = new TextEncoder().encode(`${pepe}|${matricola}`);
  const h = await crypto.subtle.digest("SHA-256", dati);
  return [...new Uint8Array(h)].map(b => b.toString(16).padStart(2, "0")).join("");
}

export default {
  async fetch(req, env){
    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: CORS });
    if (!env.DATI || !env.PEPE) return risposta({ errore: "configurazione" }, 500);

    const parti = new URL(req.url).pathname.split("/").filter(Boolean);
    const [tipo, matricola, id] = parti;
    if (!tipo) return risposta({ ok: true, servizio: "eportfolio-sfp" });
    if (!MATRICOLA.test(matricola || "")) return risposta({ errore: "matricola" }, 400);
    const h = await codice(matricola, env.PEPE);

    /* testi del profilo */
    if (tipo === "profilo" && parti.length === 2){
      const chiave = `profili/${h}/profilo.json`;
      if (req.method === "GET"){
        /* freno contro chi prova tante matricole di fila: poche aperture al minuto per connessione */
        if (env.LIMITE){
          const ip = req.headers.get("cf-connecting-ip") || "sconosciuto";
          const { success } = await env.LIMITE.limit({ key: `apri:${ip}` });
          if (!success) return risposta({ errore: "troppi tentativi" }, 429);
        }
        const o = await env.DATI.get(chiave);
        return o ? risposta(await o.text()) : risposta({ errore: "assente" }, 404);
      }
      if (req.method === "PUT"){
        const testo = await req.text();
        if (testo.length > MAX_TESTO) return risposta({ errore: "troppo grande" }, 413);
        try { JSON.parse(testo); } catch(e){ return risposta({ errore: "formato" }, 400); }
        await env.DATI.put(chiave, testo, { httpMetadata: { contentType: "application/json" } });
        return risposta({ ok: true });
      }
      if (req.method === "DELETE"){
        let cursore;
        do {
          const elenco = await env.DATI.list({ prefix: `profili/${h}/`, cursor: cursore });
          if (elenco.objects.length) await env.DATI.delete(elenco.objects.map(o => o.key));
          cursore = elenco.truncated ? elenco.cursor : undefined;
        } while (cursore);
        return risposta({ ok: true });
      }
    }

    /* foto, una per una */
    if (tipo === "foto" && parti.length === 3 && ID_IMG.test(id || "")){
      const chiave = `profili/${h}/foto/${id}`;
      if (req.method === "GET"){
        const o = await env.DATI.get(chiave);
        return o ? risposta(await o.text(), 200, "text/plain") : risposta({ errore: "assente" }, 404);
      }
      if (req.method === "PUT"){
        const testo = await req.text();
        if (testo.length > MAX_IMG) return risposta({ errore: "troppo grande" }, 413);
        if (!/^data:image\/(jpeg|png|webp);base64,/.test(testo)) return risposta({ errore: "formato" }, 400);
        await env.DATI.put(chiave, testo, { httpMetadata: { contentType: "text/plain" } });
        return risposta({ ok: true });
      }
      if (req.method === "DELETE"){
        await env.DATI.delete(chiave);
        return risposta({ ok: true });
      }
    }
    return risposta({ errore: "richiesta" }, 404);
  }
};
