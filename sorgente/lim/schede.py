# Testi delle schede LIM. Viene letto da costruisci.py (che fornisce fonte, figura, regola, SOTT e i link).
S = []

# 1 · le regole di cui parliamo
S.append(f"""
<h2>Le regole di cui parleremo</h2>
<p>In queste schede citiamo tre testi. Ecco che cosa sono e a chi si applicano.</p>
<div class="tre">
 <div class="doc"><p class="doc-t">La Costituzione italiana</p>
  <p>È la legge fondamentale dello Stato: nessuna legge o regolamento può contraddirla. Citiamo due articoli:</p>
  <ul><li><b>art. 3</b>, sull'uguaglianza: lo Stato deve togliere gli ostacoli economici e sociali che impediscono alle persone di crescere;</li>
  <li><b>art. 34</b>, sul diritto allo studio: anche chi non ha soldi ha diritto di arrivare ai livelli più alti dell'istruzione.</li></ul></div>
 <div class="doc"><p class="doc-t">La Carta dei diritti e dei doveri della Comunità Studentesca</p>
  <p>È il documento di UniMC che elenca i <b>diritti</b> e i <b>doveri</b> di chi studia qui. L'ha approvata il <b>Senato Accademico il 25 marzo 2025</b>, su proposta del Consiglio degli Studenti, ed è emanata dal Rettore.</p>
  <p>Chi ne vede violato un articolo può rivolgersi al <b>Garante degli Studenti</b>; decide il Senato Accademico (Art. 8).</p></div>
 <div class="doc"><p class="doc-t">Il Codice Etico di Ateneo</p>
  <p>Adottato con <b>Decreto Rettorale n. 254 del 7 maggio 2012</b>, fissa i doveri di comportamento di «tutti gli appartenenti alla comunità accademica, quale che sia il loro status giuridico» (Art. 2 c. 1): <b>docenti, tutor, personale e studenti</b>.</p>
  <p>Le violazioni si segnalano alla <b>Commissione di garanzia</b> nominata dal Senato (Artt. 15–16).</p></div>
</div>
{fonte(("Carta dei diritti e dei doveri UniMC", CARTA), ("Codice Etico UniMC", CODICE), ("Costituzione artt. 3 e 34", COST))}""")

# 2 · 15 ottobre e domanda 1
S.append(f"""
<p class="data">15 ottobre 2026</p>
<div class="due">
 <div style="display:grid;gap:.8em">
  <p>Viene organizzato un colloquio introduttivo online atto ad illustrare le attività del Tirocinio.</p>
  <p>Viene comunicata la necessità per gli studenti di possedere un computer in grado di connettersi alla rete, e vengono banditi altri dispositivi come i tablet, nonostante abbiano in tutto e per tutto le stesse funzionalità dei PC. Il problema è il costante malfunzionamento della rete Wi‑Fi del Polo Bertelli, un problema strutturale che va avanti da anni.</p>
  <p><b>Iniziano i primi malumori…</b></p>
 </div>
 <div style="display:grid;gap:.8em">
  <p class="dom"><b>Domanda 1</b>Perché un problema strutturale dell'Ateneo, che garantisce agli studenti l'accesso alle strutture necessarie allo studio (e il Wi‑Fi lo è), viene fatto pagare agli studenti, chiedendo di spendere centinaia di euro per un dispositivo che non è necessario, visto che ne hanno già uno o che le prove si possono svolgere su carta?</p>
  {regola("Carta dei diritti e dei doveri · Art. 2 comma 4",
          "Gli studenti «hanno il diritto di accedere alle strutture dell'Ateneo necessarie al supporto dei propri studi».",
          "La rete dell'Ateneo è una struttura di supporto allo studio. Se non funziona, il problema è dell'Ateneo: non può essere risolto chiedendo a ogni studente di comprarsi un dispositivo nuovo.")}
 </div>
</div>
{fonte(("Carta dei diritti e dei doveri UniMC", CARTA))}""")

# 3 · domanda 2
S.append(f"""
<p class="dom"><b>Domanda 2</b>In che modo l'insistenza e la pressione ad acquistare questi dispositivi non rappresentano una discriminazione socioeconomica per studenti che in larga misura non sono indipendenti economicamente?</p>
<div class="due">
 {regola("Costituzione · art. 3 comma 2 e art. 34 comma 3",
         "«È compito della Repubblica rimuovere gli ostacoli di ordine economico e sociale» · «I capaci e meritevoli, anche se privi di mezzi, hanno diritto di raggiungere i gradi più alti degli studi.»",
         "La condizione economica non deve decidere chi può studiare. Una spesa obbligatoria di centinaia di euro è proprio un ostacolo di ordine economico.")}
 <div style="display:grid;gap:.8em">
 {regola("Carta dei diritti e dei doveri · Art. 1 comma 6",
         "Tutti hanno diritto ad accedere ai percorsi formativi «a prescindere dalle condizioni economiche e sociali».",
         "L'Ateneo stesso si impegna a non far pesare il reddito sullo studio.")}
 {regola("Codice Etico · Art. 3 comma 2",
         "L'Ateneo rifiuta le discriminazioni dirette e indirette basate, tra l'altro, su «condizioni personali e sociali» e su «la condizione economica».",
         "Una regola uguale per tutti che però pesa solo su chi non può pagare è una discriminazione <b>indiretta</b>.")}
 </div>
</div>
{fonte(("Costituzione artt. 3 e 34", COST), ("Carta dei diritti e dei doveri UniMC", CARTA), ("Codice Etico UniMC", CODICE))}""")

# 4 · episodio della studentessa
S.append(f"""
<p class="data">In una classe di tirocinio</p>
<p>Secondo quanto riferito da più studenti presenti, a una studentessa che obiettava di non potersi permettere l'acquisto di un PC la tutor ha risposto con tono alterato, richiamando l'obbligo di attenersi all'autorità.</p>
<div class="due">
 {regola("Codice Etico · Art. 3 comma 2",
         "L'Ateneo rifiuta le discriminazioni basate su «la condizione economica».",
         "La studentessa poneva un problema economico reale. Rispondere con un richiamo all'autorità non lo risolve: lo zittisce.")}
 {regola("Codice Etico · Art. 2 comma 1",
         "Tutti i membri della comunità universitaria si devono «lealtà, collaborazione, rispetto reciproco, imparzialità».",
         "Il dovere vale in entrambe le direzioni: anche da chi ha un ruolo di guida verso chi studia.")}
</div>
{fonte(("Codice Etico UniMC", CODICE))}""")

# 5 · post Teams 28 ottobre
S.append(figura("1-teams-avviso-28ott.png", 1374, 766, "Post su Teams · 28 ottobre 2026, 13:11"))

# 6 · il post e le reazioni
S.append(f"""
<p class="data">28 ottobre 2026</p>
<p>Viene scritto un post su Teams dal linguaggio poco professionale, condiscendente e con l'utilizzo di un'emoticon, che ad alcuni studenti sembra addirittura la prova che il messaggio non sia affidabile e non provenga effettivamente dalla professoressa.</p>
<p><b>Plot twist: proviene effettivamente dalla professoressa.</b></p>
<p>Gli studenti non la prendono bene: il problema del Wi‑Fi è strutturale, e attribuire la mancata connessione alle «schifezze» nei loro PC, accompagnando la frase con un'emoticon, scarica su di loro un disservizio che non hanno causato.</p>
{regola("Codice Etico · Art. 2 comma 1",
        "Tutti i membri della comunità universitaria si devono «lealtà, collaborazione, rispetto reciproco, imparzialità».",
        "Un avviso ufficiale di prova valutata è una comunicazione istituzionale a tutta la classe. Dire che i PC degli studenti sono pieni di «schifezze» li accusa di un problema che è della rete.")}
<p>Alcuni scrivono email in cerca di delucidazioni sul tono adottato e sulle motivazioni che spingono a svolgere una prova online, nonostante non se ne veda il bisogno: si può svolgere su carta, e i problemi di connessione sono noti, anche ai tutor stessi.</p>
{fonte(("Codice Etico UniMC", CODICE))}""")

# 7 · esempio di lettera
S.append('<h2>Ecco un esempio di lettera:</h2>' + figura("2-mail-sciallato-28ott.png", 972, 671, "Email · 28 ottobre 2026, 16:11"))

# 8 · nel rispetto della Carta
S.append(f"""
<h2>Le lettere scritte da me e dai colleghi sono scritte nel pieno rispetto della Carta dei diritti e dei doveri della Comunità Studentesca</h2>
<div class="tre">
 {regola("Art. 1 comma 4 · Libertà espressiva",
         "La Carta riconosce agli studenti «i diritti di partecipazione, di libertà espressiva e di autonomia culturale».",
         "Scrivere a una tutor per chiedere spiegazioni su un tono e su una scelta organizzativa è esercitare questo diritto.")}
 {regola("Art. 1 comma 5 · Spirito critico",
         "«È richiesta costanza nell'applicazione, rigore nello studio, spirito critico, dedizione e curiosità scientifica».",
         "Lo spirito critico non è solo permesso: è un <b>dovere</b> che l'Ateneo chiede agli studenti.")}
 {regola("Art. 1 comma 14 · Rispetto reciproco",
         "Gli studenti partecipano responsabilmente alla vita accademica, condividendo «regole di civile convivenza e di rispetto reciproco».",
         "Le lettere sono formali, motivate e senza offese: chiedono chiarimenti, non attaccano le persone.")}
</div>
{fonte(("Carta dei diritti e dei doveri UniMC", CARTA))}""")

# 9 · titolo
S.append('<div class="centrato"><h2 class="grande">La risposta della professoressa alla mia domanda</h2></div>')

# 10 · la risposta, con le sottolineature
S.append(figura("3-mail-rucci-29ott.png", 972, 564, "Email della prof.ssa Rucci · 29 ottobre 2026, 9:45 · sottolineature aggiunte", SOTT))

# 11 · problematiche 1 e 2
S.append(f"""
<h2>Le problematiche oggettive</h2>
<div class="punto"><p><b class="n">1</b><span class="cit">«La parola schifezze, accompagnata da un'emoticon, era evidentemente una battuta»</span></p>
<p>La frase compare in un avviso ufficiale di prova valutata, rivolto a tutta la classe. Il Codice Etico, che vale per tutta la comunità universitaria, chiede a ciascuno «lealtà, collaborazione, rispetto reciproco, imparzialità» <b>(Art. 2 c. 1)</b>. Una battuta che attribuisce agli studenti un problema strutturale della rete non è coerente con questo dovere, e chiamarla battuta non cambia il suo effetto su chi la riceve.</p></div>
<div class="punto"><p><b class="n">2</b><span class="cit">«Credo anche che lei debba rispettare le scelte assunte dai docenti e dai tutor»</span></p>
<p>Chiedere un chiarimento su una scelta organizzativa non è mancanza di rispetto. La Carta dei diritti e dei doveri riconosce agli studenti la «libertà espressiva» <b>(Art. 1 c. 4)</b> e chiede loro «spirito critico» <b>(Art. 1 c. 5)</b>. Rispettare un'istituzione non significa obbedire senza fare domande: significa fare le domande nei modi e nei canali corretti, come è stato fatto.</p></div>
{fonte(("Codice Etico UniMC", CODICE), ("Carta dei diritti e dei doveri UniMC", CARTA))}""")

# 12 · problematica 3
S.append(f"""
<h2>Le problematiche oggettive</h2>
<div class="punto"><p><b class="n">3</b><span class="cit">«Quello che avete imparato a didattica non vale evidentemente per degli adulti, ma per classi di bambini»</span></p></div>
<p>La Didattica Generale non è una materia "per bambini": è il sapere su come si progetta e si conduce <b>qualunque</b> processo di insegnamento‑apprendimento, compreso il tirocinio universitario che stiamo svolgendo.</p>
{regola("Codice Etico · Art. 2 comma 2",
        "A professori e ricercatori sono affidati «i compiti didattici e di assistenza agli studenti», da svolgere con diligenza.",
        "Anche un'attività universitaria va progettata e condotta con cura: è un dovere di chi insegna, non una scelta.")}
<p><b>Perché è grave:</b> il tirocinio serve proprio a mettere in pratica la didattica che studiamo. Se a negarne il valore è chi ci accompagna nel tirocinio, viene negato il senso stesso del percorso e del ruolo di chi lo guida.</p>
{fonte(("Codice Etico UniMC", CODICE))}""")

# 13 · problematica 4
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

# 13b · altre scelte organizzative (1/2)
S.append(f"""
<h2>Altre scelte organizzative · 1</h2>
<div class="tre">
 <div class="doc"><p class="doc-t">L'e-portfolio compilato di corsa</p>
  <p>Invece di essere preparato con calma e in anticipo, a casa, l'e-portfolio viene fatto compilare in fretta in classe. E chi non finisce deve completarlo comunque a casa.</p>
  <p><b>Se alla fine si completa a casa, che senso ha la compilazione affrettata in classe?</b></p></div>
 <div class="doc"><p class="doc-t">Gli attestati sulla sicurezza</p>
  <p>Su Teams, il 10 ottobre, gli studenti vengono pregati di non scrivere ai tutor: «Controllate i vostri attestati da soli perché non possiamo farlo per tutti voi».</p>
  <p>Capire se un attestato è valido è una condizione per accedere al tirocinio: un aspetto organizzativo su cui gli studenti vengono lasciati soli, mentre il Codice Etico parla di «assistenza agli studenti» <b>(Art. 2 c. 2)</b>.</p></div>
 <div class="doc"><p class="doc-t">Il corso sulla sicurezza</p>
  <p>Perché non viene fatto svolgere nel secondo semestre del primo anno, invece di sovrapporlo all'avvio del tirocinio?</p>
  <p>Un esempio concreto: alla mia richiesta di tirocinio, la scuola ha risposto che accoglierà <b>soltanto</b> le richieste di chi ha già completato la formazione sulla sicurezza di 12 ore. Senza attestato, il tirocinio non parte.</p></div>
</div>
{fonte(("Codice Etico UniMC", CODICE))}""")

# 13c · altre scelte organizzative (2/2)
S.append(f"""
<h2>Altre scelte organizzative · 2</h2>
<div class="punto"><p class="cit">Gli studenti lavoratori</p></div>
<p>Agli studenti lavoratori è stato detto che <b>non sono permesse assenze</b> e che devono essere grati per i giorni di laboratorio al sabato.</p>
<div class="due">
 {regola("Piano di studio LM-85bis UniMC · laboratori e tirocinio",
         "Per laboratori e tirocinio «è previsto un OBBLIGO DI FREQUENZA, pari al 70% del monte ore».",
         "L'obbligo è del 70%: entro il restante 30% le assenze sono consentite. Dire che non sono permesse è un'informazione non corretta.")}
 {regola("Carta dei diritti e dei doveri · Art. 1 comma 6",
         "Tra le tutele previste anche per gli studenti lavoratori, l'Università «si impegna a rimuovere gli ostacoli nelle attività didattiche per il conseguimento dei titoli accademici».",
         "Chi lavora per mantenersi agli studi va tutelato, non messo in difficoltà con regole più severe di quelle reali.")}
</div>
{fonte(("Piano di studio LM-85bis UniMC", PIANO), ("Carta dei diritti e dei doveri UniMC", CARTA))}""")

# 14 · il tutor
S.append(f"""
<h2>Il paradosso del tutor</h2>
<p><b>Tutor</b> viene dal latino <i>tutor</i>, «tutore, guardiano», dal verbo <i>tueri</i>: <b>proteggere, sorvegliare</b>. È la stessa radice di <i>tutela</i>.</p>
{regola("Codice Etico · Art. 2 comma 2",
        "A professori e ricercatori sono affidati, tra gli altri, «i compiti didattici e di assistenza agli studenti».",
        "Per il Codice Etico l'assistenza agli studenti fa parte del ruolo di chi insegna, non è un favore.")}
<p>Lasciare agli studenti il compito di cavarsela da soli con problemi creati dall'organizzazione rovescia il senso stesso della parola.</p>
{fonte(("Etymonline, «tutor»", ETIMO), ("Codice Etico UniMC", CODICE))}""")

# 15 · la mia controrisposta
S.append('<h2>La mia controrisposta</h2>' + figura("4-mail-sciallato-29ott.png", 972, 564, "Email · 29 ottobre 2026, 21:00"))

# 16 · perché non regge (1/2)
S.append(f"""
<h2>Perché quell'affermazione non regge · 1</h2>
<p>Lo dice la didattica che abbiamo studiato. Per Pier Giuseppe Rossi, docente di UniMC e coautore de <i>L'agire didattico</i>, progettare è un'<b>azione simulata</b>: «il docente mentre progetta immagina mentalmente come evolverà il sistema-classe».</p>
<div class="tab">
 <p class="th">Cosa insegna la didattica</p><p class="th">Nel nostro caso</p>
 <p><b>Progettare</b> = simulare in anticipo l'azione, prima di svolgerla.</p><p>Una prova online va "provata con la mente" nel luogo dove si svolgerà.</p>
 <p><b>Analizzare il contesto</b> in cui l'azione avverrà.</p><p>Il contesto è il Polo Bertelli, con una rete Wi‑Fi instabile da anni.</p>
 <p><b>Prevedere gli imprevisti prevedibili.</b></p><p>Una rete che non regge non è un imprevisto: è un dato noto, anche ai tutor.</p>
 <p><b>Pensare un piano B in anticipo.</b></p><p>Il piano B esisteva già: la prova su carta.</p>
</div>
{fonte(("Rossi, Pentucci, Progettazione come azione simulata (FrancoAngeli 2021)", ROSSI), ("Rivoltella, Rossi, L'agire didattico (Scholé 2017)", RIVOLTELLA))}""")

# 16b · perché non regge (2/2)
S.append(f"""
<h2>Perché quell'affermazione non regge · 2</h2>
<p class="dom"><b>Un esempio</b>Un professore di matematica entra in classe, scrive alla lavagna <b>2 + 2 = 5</b> e pretende che nessuno lo contesti e che tutti obbediscano. Chi alza la mano non gli manca di rispetto: sta facendo matematica.</p>
<p>Allo stesso modo, chi chiede una prova progettata secondo i principi della didattica non manca di rispetto: sta applicando ciò che il corso di laurea gli ha insegnato. E ha diritto a una didattica di qualità:</p>
<div class="due">
 {regola("Standard europei di qualità (ESG 2015) · standard 1.3",
         "Le istituzioni devono garantire che i corsi siano erogati in modo da incoraggiare gli studenti ad assumere un ruolo attivo (traduzione nostra).",
         "Sono gli standard con cui si valuta la qualità delle università europee, Italia compresa. Uno studente che chiede spiegazioni è uno studente attivo.")}
 {regola("Carta dei diritti e dei doveri · Art. 2 comma 14",
         "«I risultati delle schede di valutazione devono essere utilizzati per vigilare sul rispetto della presente Carta.»",
         "La qualità della didattica non è lasciata al caso: la valutano anche gli studenti, e l'Ateneo deve tenerne conto.")}
</div>
{fonte(("ESG 2015", ESG), ("Carta dei diritti e dei doveri UniMC", CARTA))}""")

# 17 · comunicato Teams
S.append('<h2>Il comunicato su Teams</h2>' + figura("5-teams-comunicazione-29ott.png", 1355, 792, "Teams · 29 ottobre 2026, 9:49"))

# 18 · la mia risposta
S.append('<h2>La mia risposta</h2>' + figura("6-teams-risposta-sciallato-29ott.png", 1355, 564, "Teams · 29 ottobre 2026, 21:41"))

# 19 · titolo
S.append('<div class="centrato"><h2 class="grande">Per rinfrescare la memoria</h2></div>')

# 20 · punti contestati (1/2)
S.append(f"""
<h2>I punti che contestiamo · 1</h2>
<div class="tre">
 {contesta("«Fate controllare i vostri PC e ripuliteli da tutte le schifezze!»", "Teams, 28 ottobre",
           "Codice Etico · Art. 2 c. 1", "«lealtà, collaborazione, rispetto reciproco, imparzialità»",
           "Un problema della rete viene presentato come colpa degli studenti, in un avviso ufficiale.")}
 {contesta("«Credo anche che lei debba rispettare le scelte assunte dai docenti e dai tutor»", "email, 29 ottobre",
           "Carta · Art. 1 c. 4 e c. 5", "«libertà espressiva» · «spirito critico»",
           "Una richiesta di chiarimento viene trattata come mancanza di rispetto, mentre la Carta la riconosce come diritto e la chiede come dovere.")}
 {contesta("Obbligo di un PC e di una prova online su una rete instabile", "15 e 28 ottobre",
           "Carta · Art. 2 c. 4", "diritto di accedere «alle strutture dell'Ateneo necessarie al supporto dei propri studi»",
           "Il costo di una struttura che non funziona viene spostato sugli studenti.")}
</div>
{fonte(("Carta dei diritti e dei doveri UniMC", CARTA), ("Codice Etico UniMC", CODICE))}""")

# 21 · punti contestati (2/2)
S.append(f"""
<h2>I punti che contestiamo · 2</h2>
<div class="tre">
 {contesta("La studentessa che non può permettersi un PC", "secondo quanto riferito da più studenti presenti",
           "Carta · Art. 1 c. 6 · Codice Etico · Art. 3 c. 2", "«a prescindere dalle condizioni economiche e sociali» · «la condizione economica»",
           "A un problema economico reale si risponde con un richiamo all'autorità.")}
 {contesta("«Molti di voi non comprendono evidentemente né le battute, né il linguaggio delle emoticon»", "Teams, 29 ottobre",
           "Codice Etico · Art. 2 c. 1", "«rispetto reciproco»",
           "Chi ha chiesto chiarimenti viene descritto, davanti a tutti, come incapace di capire.")}
 {contesta("«Speriamo di non proseguire il semestre in polemiche»", "Teams, 29 ottobre",
           "Carta · Art. 1 c. 4 · Art. 8 c. 3", "«libertà espressiva» · diritto di segnalare le violazioni al Garante degli Studenti",
           "Le domande degli studenti vengono chiamate «polemiche». Per la Carta sono un diritto.")}
</div>
{fonte(("Carta dei diritti e dei doveri UniMC", CARTA), ("Codice Etico UniMC", CODICE))}""")

# 22 · a chi rivolgersi
S.append(f"""
<h2>Cosa possono fare gli studenti · a chi rivolgersi</h2>
<div class="tre">
 <div class="doc"><p class="doc-t">Garante degli Studenti</p>
  <p>È la figura prevista dalla Carta per le sue violazioni. Ogni studente può segnalargliele (Art. 8 c. 3). Opera «in piena indipendenza di giudizio e di valutazione» ed è tenuto alla riservatezza sulle segnalazioni; poi decide il Senato Accademico (Art. 8 c. 2).</p></div>
 <div class="doc"><p class="doc-t">Commissione di garanzia del Codice Etico</p>
  <p>Cinque membri nominati dal Senato. «Riceve le segnalazioni delle infrazioni e propone al Rettore» i provvedimenti (Art. 15 c. 5). Servono segnalazioni <b>scritte e firmate</b>: quelle anonime non vengono considerate (Art. 16). La persona segnalata può difendersi ed essere ascoltata.</p></div>
 <div class="doc"><p class="doc-t">Presidio della Qualità</p>
  <p>Riceve le segnalazioni di disservizi tramite il <b>modulo online</b> «Segnalazioni e reclami» sul sito UniMC, sezione Qualità. Deve rispondere <b>entro 35 giorni</b>. Toglie il nome di chi segnala quando inoltra la pratica; per la didattica la inoltra al Direttore di Dipartimento.</p></div>
</div>
<div class="due">
 <div class="doc"><p class="doc-t">Direttore di Dipartimento</p>
  <p>Secondo le linee guida di Ateneo, è il Direttore o la Direttrice a gestire le segnalazioni sulla didattica, sentiti il Presidente del corso di studio e la persona interessata.</p></div>
 <div class="doc"><p class="doc-t">Presidente del Consiglio degli Studenti e mozioni</p>
  <p>I rappresentanti degli studenti partecipano «attivamente agli organi e alle commissioni dell'Università» (Carta, Art. 5 c. 5): possono portare il problema negli organi e presentare <b>mozioni</b>.</p></div>
</div>
{fonte(("Carta dei diritti e dei doveri UniMC", CARTA), ("Codice Etico UniMC", CODICE), ("Linee guida UniMC su segnalazioni e reclami", LINEE))}""")

# 23 · conseguenze
S.append(f"""
<h2>Cosa possono fare gli studenti · cosa succede dopo</h2>
<p>Se la Commissione di garanzia accerta una violazione del Codice Etico, il Senato Accademico, su proposta del Rettore, può adottare, in proporzione alla gravità e con gradualità, uno di questi provvedimenti <b>(Art. 16 c. 10)</b>:</p>
<ol>
 <li><b>richiamo formale</b>;</li>
 <li>richiamo formale con <b>deposito degli atti nel fascicolo personale</b>; segnalazione alla comunità universitaria;</li>
 <li>esclusione dalla ripartizione dei fondi di ricerca di Ateneo, fino a tre anni;</li>
 <li>esclusione dalle cariche accademiche o da quelle su nomina del Rettore, fino a tre anni.</li>
</ol>
<p>Se il comportamento è anche un illecito disciplinare, la Commissione passa il caso al Rettore e si segue il procedimento disciplinare <b>(Art. 17)</b>.</p>
<p>Inoltre, per la Carta i risultati delle schede di valutazione della didattica «devono essere utilizzati per vigilare sul rispetto della presente Carta» <b>(Art. 2 c. 14)</b>: compilarle con cura è già una forma di segnalazione.</p>
{fonte(("Codice Etico UniMC", CODICE), ("Carta dei diritti e dei doveri UniMC", CARTA))}""")

# 24 · fine
S.append('<div class="fine-lim"><div class="timbro-posto"></div><h2>Grazie e Arrivederci</h2></div>')
