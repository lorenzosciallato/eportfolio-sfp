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

def fonte(*coppie):
    return '<p class="fonte">Fonti: ' + " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in coppie) + "</p>"

def figura(file, w, h, didascalia, sopra=""):
    return (f'<p class="data">{didascalia}</p>'
            f'<div class="fig"><div class="box" style="--r:{w}/{h}"><img src="assets/lim/{file}" alt="{didascalia}">{sopra}</div></div>')

SOTT = open(os.path.join(qui, "sottolineature.svg")).read()

S = []

# 1 · 15 ottobre
S.append(f"""
<p class="data">15 ottobre 2026</p>
<div class="due">
 <div style="display:grid;gap:.8em">
  <p>Viene organizzato un colloquio introduttivo online atto ad illustrare le attività del Tirocinio.</p>
  <p>Viene comunicata la necessità per gli studenti di possedere un computer in grado di connettersi alla rete, e vengono banditi altri dispositivi come i tablet, nonostante abbiano in tutto e per tutto le stesse funzionalità dei PC. Il problema è il costante malfunzionamento della rete Wi‑Fi del Polo Bertelli, un problema strutturale che va avanti da anni.</p>
  <p><b>Iniziano i primi malumori…</b></p>
 </div>
 <div style="display:grid;gap:.8em">
  <p class="dom"><b>Domanda 1</b>Perché un problema strutturale dell'Ateneo viene fatto pagare agli studenti, chiedendo di spendere centinaia di euro per un dispositivo che non è necessario, visto che ne hanno già uno o che le prove si possono svolgere su carta?</p>
  <p class="norma"><b>Carta dei diritti e dei doveri, Art. 2 c. 4:</b> gli studenti «hanno il diritto di accedere alle strutture dell'Ateneo necessarie al supporto dei propri studi».</p>
  <p class="dom"><b>Domanda 2</b>In che modo l'insistenza e la pressione ad acquistare questi dispositivi non rappresentano una discriminazione socioeconomica per studenti che in larga misura non sono indipendenti economicamente?</p>
  <p class="norma"><b>Costituzione, art. 3 c. 2:</b> «È compito della Repubblica rimuovere gli ostacoli di ordine economico e sociale». <b>Art. 34 c. 3:</b> «I capaci e meritevoli, anche se privi di mezzi, hanno diritto di raggiungere i gradi più alti degli studi.»<br><b>Carta, Art. 1 c. 6:</b> accesso ai percorsi formativi «a prescindere dalle condizioni economiche e sociali».<br><b>Codice Etico, Art. 3 c. 2:</b> rifiuto delle discriminazioni basate su «condizioni personali e sociali» e su «la condizione economica».</p>
 </div>
</div>
{fonte(("Carta dei diritti e dei doveri UniMC", CARTA), ("Codice Etico UniMC", CODICE), ("Costituzione artt. 3 e 34", COST))}""")

# 2 · episodio della studentessa
S.append(f"""
<p class="data">In una classe di tirocinio</p>
<div class="centrato" style="align-items:stretch">
 <p>Secondo quanto riferito da più studenti presenti, a una studentessa che obiettava di non potersi permettere l'acquisto di un PC la tutor ha risposto con tono alterato, richiamando l'obbligo di attenersi all'autorità.</p>
 <p class="norma"><b>Codice Etico, Art. 3 c. 2:</b> l'Ateneo rifiuta le discriminazioni basate su «la condizione economica».<br><b>Codice Etico, Art. 2 c. 1:</b> tra i membri della comunità universitaria, «lealtà, collaborazione, rispetto reciproco, imparzialità».</p>
</div>
{fonte(("Codice Etico UniMC", CODICE))}""")

# 3 · post Teams 28 ottobre
S.append(figura("1-teams-avviso-28ott.png", 1374, 766, "Post su Teams · 28 ottobre 2026, 13:11"))

# 4 · il post e le reazioni
S.append(f"""
<p class="data">28 ottobre 2026</p>
<p>Viene scritto un post su Teams dal linguaggio poco professionale, condiscendente e con l'utilizzo di un'emoticon, che ad alcuni studenti sembra addirittura la prova che il messaggio non sia affidabile e non provenga effettivamente dalla professoressa.</p>
<p><b>Plot twist: proviene effettivamente dalla professoressa.</b></p>
<p>Gli studenti non la prendono bene: il problema del Wi‑Fi è strutturale, e attribuire la mancata connessione alle «schifezze» nei loro PC, accompagnando la frase con un'emoticon, scarica su di loro un disservizio che non hanno causato.</p>
<p class="norma"><b>Codice Etico, Art. 2 c. 1:</b> tutti i membri della comunità universitaria devono «lealtà, collaborazione, rispetto reciproco, imparzialità».</p>
<p>Alcuni scrivono email in cerca di delucidazioni sul tono adottato e sulle motivazioni che spingono a svolgere una prova online, nonostante non se ne veda il bisogno: si può svolgere su carta, e i problemi di connessione sono noti, anche ai tutor stessi.</p>
{fonte(("Codice Etico UniMC", CODICE))}""")

# 5 · esempio di lettera
S.append('<h2>Ecco un esempio di lettera:</h2>' + figura("2-mail-sciallato-28ott.png", 972, 671, "Email · 28 ottobre 2026, 16:11"))

# 6 · nel rispetto della Carta
S.append(f"""
<h2>Le lettere scritte da me e dai colleghi sono scritte nel pieno rispetto della Carta dei diritti e dei doveri della Comunità Studentesca, che:</h2>
<ul>
 <li>riconosce agli studenti «i diritti di partecipazione, di libertà espressiva e di autonomia culturale» <b>(Art. 1 c. 4)</b>;</li>
 <li>chiede loro: «È richiesta costanza nell'applicazione, rigore nello studio, spirito critico, dedizione e curiosità scientifica» <b>(Art. 1 c. 5)</b>;</li>
 <li>chiede di condividere «regole di civile convivenza e di rispetto reciproco» <b>(Art. 1 c. 14)</b>.</li>
</ul>
{fonte(("Carta dei diritti e dei doveri UniMC", CARTA))}""")

# 7 · titolo
S.append('<div class="centrato"><h2 class="grande">La risposta della professoressa alla mia domanda</h2></div>')

# 8 · la risposta, con le sottolineature
S.append(figura("3-mail-rucci-29ott.png", 972, 564, "Email della prof.ssa Rucci · 29 ottobre 2026, 9:45 · sottolineature aggiunte", SOTT))

# 9 · problematiche 1 e 2
S.append(f"""
<h2>Le problematiche oggettive</h2>
<div class="punto"><p><b class="n">1</b><span class="cit">«La parola schifezze, accompagnata da un'emoticon, era evidentemente una battuta»</span></p>
<p>La frase compare in un avviso ufficiale di prova valutata, rivolto a tutta la classe. Attribuire un problema strutturale della rete alle «schifezze» nei PC degli studenti non è coerente con il dovere di «lealtà, collaborazione, rispetto reciproco, imparzialità» <b>(Codice Etico, Art. 2 c. 1)</b>.</p></div>
<div class="punto"><p><b class="n">2</b><span class="cit">«Credo anche che lei debba rispettare le scelte assunte dai docenti e dai tutor»</span></p>
<p>Chiedere un chiarimento su una scelta organizzativa non è mancanza di rispetto: è l'esercizio dello «spirito critico» che la Carta richiede agli studenti <b>(Art. 1 c. 5)</b> e della «libertà espressiva» che riconosce loro <b>(Art. 1 c. 4)</b>. Il rispetto istituzionale non coincide con l'obbedienza senza domande.</p></div>
{fonte(("Codice Etico UniMC", CODICE), ("Carta dei diritti e dei doveri UniMC", CARTA))}""")

# 10 · problematica 3
S.append(f"""
<h2>Le problematiche oggettive</h2>
<div class="punto"><p><b class="n">3</b><span class="cit">«Quello che avete imparato a didattica non vale evidentemente per degli adulti, ma per classi di bambini»</span></p></div>
<ul>
 <li>La Didattica Generale studia i processi di insegnamento‑apprendimento, a prescindere dall'età anagrafica.</li>
 <li>Esiste un intero campo di studi dedicato a come apprendono gli adulti: l'<b>andragogia</b> (M. Knowles, <i>The Adult Learner</i>).</li>
 <li>Gli standard europei per la qualità dell'università chiedono che i corsi siano erogati in modo da incoraggiare gli studenti ad assumere un ruolo attivo <b>(ESG 2015, standard 1.3)</b>.</li>
 <li>Progettazione, analisi del contesto e piani alternativi per gli imprevisti valgono anche in un corso di laurea che forma insegnanti. Se valessero solo per i bambini, nemmeno il tirocinio universitario avrebbe bisogno di essere progettato.</li>
</ul>
{fonte(("Knowles, The Adult Learner (Routledge)", KNOWLES), ("ESG 2015", ESG))}""")

# 11 · problematica 4
S.append(f"""
<h2>Le problematiche oggettive</h2>
<div class="punto"><p><b class="n">4</b><span class="cit">«Siete voi a dovervi abituare a risolvere i problemi tecnici che incontrerete»</span></p></div>
<p>I problemi tecnici di queste settimane non nascono dall'imprevisto o dal caso, ma da scelte organizzative:</p>
<ul>
 <li>la rete Wi‑Fi del Polo Bertelli, instabile da anni e nota anche ai tutor;</li>
 <li>lo strumento fornito per generare il PDF, inaffidabile e difettoso: taglia il testo oltre le due frasi e prevede di scaricare un file HTML, generare il PDF e mandarlo a un link;</li>
 <li>Panquiz usato con licenza gratuita: finiti gli accessi, decine di studenti si sono ritrovati fuori.</li>
</ul>
<p><b>Chiedere agli studenti di risolvere problemi causati da strumenti e scelte che non dipendono da loro è un paradosso.</b></p>""")

# 12 · il tutor
S.append(f"""
<h2>Il paradosso del tutor</h2>
<p><b>Tutor</b> viene dal latino <i>tutor</i>, «tutore, guardiano», dal verbo <i>tueri</i>: <b>proteggere, sorvegliare</b>.</p>
<p>Il Codice Etico di Ateneo affida a professori e ricercatori «i compiti didattici e di assistenza agli studenti» <b>(Art. 2 c. 2)</b>: l'assistenza fa parte del ruolo di chi insegna.</p>
<p>Lasciare agli studenti il compito di cavarsela da soli con problemi creati dall'organizzazione rovescia il senso stesso della parola.</p>
{fonte(("Etymonline, «tutor»", ETIMO), ("Codice Etico UniMC", CODICE))}""")

# 13 · la mia controrisposta
S.append('<h2>La mia controrisposta</h2>' + figura("4-mail-sciallato-29ott.png", 972, 564, "Email · 29 ottobre 2026, 21:00"))

# 14 · perché non regge
S.append(f"""
<h2>Perché quell'affermazione non regge</h2>
<ul>
 <li>Come insegna il corso di Didattica Generale, progettare la didattica significa analizzare il contesto, <b>simulare in anticipo l'azione</b> e prevedere piani alternativi per gli imprevisti.</li>
 <li>La progettazione è il cuore dei manuali di didattica (es. P.C. Rivoltella, P.G. Rossi, <i>L'agire didattico. Manuale per l'insegnante</i>, Scholé 2017).</li>
 <li>Questi principi non hanno una scadenza anagrafica: l'andragogia li studia negli adulti, gli standard europei ESG li chiedono all'università.</li>
</ul>
<p class="dom"><b>Un esempio</b>Un professore di matematica entra in classe, scrive alla lavagna <b>2 + 2 = 5</b> e pretende che nessuno lo contesti e che tutti obbediscano. Chi alza la mano non gli manca di rispetto: sta facendo matematica.</p>
{fonte(("Rivoltella, Rossi, L'agire didattico", RIVOLTELLA), ("Knowles, The Adult Learner", KNOWLES), ("ESG 2015", ESG))}""")

# 15 · comunicato Teams
S.append('<h2>Il comunicato su Teams</h2>' + figura("5-teams-comunicazione-29ott.png", 1355, 792, "Teams · 29 ottobre 2026, 9:49"))

# 16 · la mia risposta
S.append('<h2>La mia risposta</h2>' + figura("6-teams-risposta-sciallato-29ott.png", 1355, 564, "Teams · 29 ottobre 2026, 21:41"))

# 17 · titolo
S.append('<div class="centrato"><h2 class="grande">Per rinfrescare la memoria</h2></div>')

# 18 · i punti problematici con gli articoli
S.append(f"""
<h2>I punti che contestiamo</h2>
<div class="due">
 <p class="punto"><span class="cit">«ripuliteli da tutte le schifezze!»</span> (Teams, 28 ott)<br><b>Codice Etico, Art. 2 c. 1</b> — «lealtà, collaborazione, rispetto reciproco, imparzialità».</p>
 <p class="punto"><span class="cit">«lei debba rispettare le scelte assunte dai docenti e dai tutor»</span> (email, 29 ott)<br><b>Carta, Art. 1 c. 4</b> — «libertà espressiva»; <b>Art. 1 c. 5</b> — «spirito critico».</p>
 <p class="punto">Obbligo di un PC e di una prova online su una rete instabile<br><b>Carta, Art. 2 c. 4</b> — accesso «alle strutture dell'Ateneo necessarie al supporto dei propri studi».</p>
 <p class="punto">La studentessa che non può permettersi un PC<br><b>Carta, Art. 1 c. 6</b> — «a prescindere dalle condizioni economiche e sociali»; <b>Codice Etico, Art. 3 c. 2</b> — «la condizione economica».</p>
 <p class="punto"><span class="cit">«Molti di voi non comprendono evidentemente né le battute, né il linguaggio delle emoticon»</span> (Teams, 29 ott)<br><b>Codice Etico, Art. 2 c. 1</b> — «rispetto reciproco».</p>
 <p class="punto"><span class="cit">«Speriamo di non proseguire il semestre in polemiche»</span> (Teams, 29 ott)<br><b>Carta, Art. 1 c. 4</b> — «libertà espressiva»; <b>Art. 8 c. 3</b> — diritto di segnalare le violazioni al Garante degli Studenti.</p>
</div>
{fonte(("Carta dei diritti e dei doveri UniMC", CARTA), ("Codice Etico UniMC", CODICE))}""")

# 19 · cosa possono fare gli studenti
S.append(f"""
<h2>Cosa possono fare gli studenti</h2>
<div class="due">
 <ul>
  <li>Segnalare le violazioni della Carta al <b>Garante degli Studenti</b> (Carta, Art. 8 c. 3); decide il Senato Accademico (Art. 8 c. 2).</li>
  <li>Segnalare per iscritto le violazioni del Codice Etico alla <b>Commissione di garanzia</b> (Codice Etico, Artt. 15–16; non si considerano le segnalazioni anonime).</li>
  <li>Segnalare al <b>Presidio della Qualità</b> di Ateneo.</li>
  <li>Segnalare al <b>Direttore di Dipartimento</b>.</li>
  <li>Segnalare al <b>Presidente del Consiglio degli Studenti</b>.</li>
  <li>Presentare <b>mozioni</b>.</li>
 </ul>
 <div style="display:grid;gap:.6em">
  <p><b>Conseguenze previste (Codice Etico, Art. 16 c. 10):</b></p>
  <ul>
   <li>richiamo formale;</li>
   <li>richiamo formale con deposito degli atti nel fascicolo personale; segnalazione alla comunità universitaria;</li>
   <li>esclusione dalla ripartizione dei fondi di ricerca di Ateneo fino a tre anni;</li>
   <li>esclusione dalle cariche accademiche o su nomina del Rettore fino a tre anni.</li>
  </ul>
  <p>Se la condotta è anche un illecito disciplinare, si procede in via disciplinare (Art. 17).</p>
 </div>
</div>
{fonte(("Carta dei diritti e dei doveri UniMC", CARTA), ("Codice Etico UniMC", CODICE))}""")

# 20 · fine
S.append('<div class="fine-lim"><div class="timbro-posto"></div><h2>Grazie e Arrivederci</h2></div>')

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
