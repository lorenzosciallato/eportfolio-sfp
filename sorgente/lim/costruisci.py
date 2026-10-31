"""Schede LIM temporanee: scrive il blocco e lo inserisce nel sito.
   python3 sorgente/lim/costruisci.py         -> inserisce (o aggiorna) il blocco
   python3 sorgente/lim/costruisci.py togli   -> toglie il blocco e torna al sito originale
"""
import os, sys, json, re
qui = os.path.dirname(os.path.abspath(__file__))
radice = os.path.dirname(os.path.dirname(qui))
INIZIO, FINE = "<!-- LIM:INIZIO -->", "<!-- LIM:FINE -->"

CARTA = "https://new.unimc.it/it/ateneo/normativa/regolamenti-di-ateneo/sa-40-2025-impaginata-carta-dei-diritti-e-dei-doveri-della-comunita-studentesca.pdf"
CODICE = "https://new.unimc.it/it/ateneo/normativa/regolamenti-di-ateneo/ateneoreg/nuoviregolamentisitoweb.al.06.3.2014/Codice.etico.pdf"
COST = "https://www.consiglioregionale.calabria.it/upload/istruttoria/Costituzione%20Italiana%20artt%203,%2034,%2038.pdf"
ETIMO = "https://www.etymonline.com/word/Tutor"
KNOWLES = "https://www.routledge.com/The-Adult-Learner-The-Definitive-Classic-in-Adult-Education-and-Human-Resource-Development/Knowles-Robinson-Caraccioli/p/book/9781032481562"
ESG = "https://acpua.aragon.es/sites/default/files/revised_esg_intro_june_2015_tl.pdf"
RIVOLTELLA = "https://cris.unibo.it/handle/11585/966116"
ROSSI = "https://static.francoangeli.it/fa-contenuti/area_pdfdemo/1096.1.7_demo.pdf"

def fonte(*coppie):
    return '<p class="fonte">Fonti: ' + " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in coppie) + "</p>"

def figura(file, w, h, didascalia, sopra=""):
    return (f'<p class="data">{didascalia}</p>'
            f'<div class="fig"><div class="box" style="--r:{w}/{h}"><img src="assets/lim/{file}" alt="{didascalia}">{sopra}</div></div>')

SOTT = open(os.path.join(qui, "sottolineature.svg")).read()

LINEE = "https://www.unimc.it/it/qualita/sistemaAQ/documenti-linee-guida-per-i-processi-di-assicurazione-della-qualita-di-ateneo/lg_segnalazioni_suggerimenti_reclami_11_dicembre_2023.pdf"

def regola(titolo, dice, perche):
    return (f'<div class="regola"><p class="r-t">{titolo}</p>'
            f'<p><span class="r-e">Cosa dice</span> {dice}</p>'
            f'<p><span class="r-e">Perché c\'entra</span> {perche}</p></div>')

def contesta(frase, dove, norma, testo, perche):
    return (f'<div class="regola"><p class="cit">{frase}</p><p class="r-dove">{dove}</p>'
            f'<p class="r-t">{norma}</p><p>{testo}</p><p><span class="r-e">Il problema</span> {perche}</p></div>')

exec(open(os.path.join(qui, "schede.py")).read())
css = open(os.path.join(qui, "lim.css")).read()
js = open(os.path.join(qui, "lim.js")).read()
dati = json.dumps(S, ensure_ascii=False).replace("</", "<\\/")
blocco = f"{INIZIO}\n<style id=\"lim-css\">\n{css}</style>\n<script>window.LIM_SCHEDE = {dati};</script>\n<script id=\"lim-js\">\n{js}</script>\n{FINE}\n"

def togli(s):
    return re.sub(re.escape(INIZIO) + r".*?" + re.escape(FINE) + r"\n?", "", s, flags=re.S)

togliere = len(sys.argv) > 1 and sys.argv[1] == "togli"
for nome, prima in ((os.path.join(radice, "index.html"), "</body>"), (os.path.join(radice, "sorgente/src/app.html"), None)):
    s = togli(open(nome).read())
    if not togliere:
        s = s.replace(prima, blocco + prima, 1) if prima else s.rstrip("\n") + "\n" + blocco
    open(nome, "w").write(s)
    print(("tolto da " if togliere else "inserito in ") + os.path.relpath(nome, radice))
print(len(S), "schede")
