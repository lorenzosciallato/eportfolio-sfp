# Sorgenti di E-Portfolio SFP

Questa cartella serve solo per modificare l'app: gli studenti usano il sito nella cartella principale.

- `src/app.html` — l'app (testi, grafica, funzioni). `src/privacy.html` — informativa privacy.
- `build.py` — costruisce il sito: incorpora font e illustrazioni e scrive `out/site/index.html`, `out/site/sw.js`, `out/site/privacy.html`. Poi si copiano `index.html`, `privacy.html`, `sw.js`, `manifest.webmanifest`, `icone/` e `assets/` nella cartella principale.
- `api.txt` — indirizzo del Worker Cloudflare che salva i profili.
- `out/site/assets/` — font, illustrazioni (webp) e motore del PDF; `out/site/icone/` — icone dell'app.
- `worker/` — il programma su Cloudflare (`worker.js`). Si pubblica con `npx wrangler@4 deploy` dalla cartella `worker`. La frase segreta PEPE è salvata solo su Cloudflare e non va mai scritta qui.
- `cassetta/pillole/` — i testi delle pillole della Cassetta degli attrezzi, un file per area (T01…T16); le immagini delle pillole sono `assets/pT01-01.webp` e così via.
- `illustrazioni/` — originali delle illustrazioni (anche `cassetta/` e `pillole/`); `logo/` — originale dell'icona.
