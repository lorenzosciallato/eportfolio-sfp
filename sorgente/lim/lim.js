/* ===== LIM: schede temporanee (si aprono digitando L I M, o con #lim nell'indirizzo; Esc per uscire) ===== */
(function(){
  const SCHEDE = window.LIM_SCHEDE || [];
  if (!SCHEDE.length) return;
  let box = null, i = 0, aperta = false, seq = "";
  const N = SCHEDE.length;

  function costruisci(){
    box = document.createElement("div");
    box.id = "lim";
    box.setAttribute("role", "region");
    box.setAttribute("aria-label", "Schede");
    box.innerHTML = SCHEDE.map((s, k) => `<section class="lim-s" data-k="${k}"><div class="lim-in">${s}</div></section>`).join("")
      + `<div class="barra"><span id="lim-n"></span><span class="linea"><i id="lim-p"></i></span><span>← →</span></div>`;
    document.body.appendChild(box);
    if (typeof scorrimento === "function") scorrimento(box, () => vai(1), () => vai(-1));
  }
  /* il testo si rimpicciolisce finché la scheda entra tutta nello schermo: mai scorrere */
  function adatta(s){
    const inn = s.querySelector(".lim-in");
    let k = 1;
    inn.style.setProperty("--k", k);
    while (k > .45 && (inn.scrollHeight > inn.clientHeight + 1 || inn.scrollWidth > inn.clientWidth + 1)){
      k -= .04; inn.style.setProperty("--k", k.toFixed(2));
    }
  }
  function mostra(){
    box.querySelectorAll(".lim-s").forEach(s => s.classList.toggle("vista", +s.dataset.k === i));
    const s = box.querySelector(`.lim-s[data-k="${i}"]`);
    if (s.querySelector(".fine-lim")){
      const t = s.querySelector(".timbro-posto");
      if (t) t.innerHTML = `<div class="timbro">${typeof timbroSvg === "function" ? timbroSvg({ n:"lim" }) : ""}</div>`;
      if (typeof coriandoli === "function") setTimeout(coriandoli, 650);
      musica(true);
    } else musica(false);
    adatta(s);
    box.querySelector("#lim-n").textContent = `${i + 1} / ${N}`;
    box.querySelector("#lim-p").style.width = `${(i + 1) / N * 100}%`;
  }
  /* canzone di chiusura: assets/lim/canzone.mp3, se presente */
  let audio = null;
  function musica(su){
    try {
      if (su){
        if (!audio){ audio = new Audio("assets/lim/canzone.mp3"); audio.preload = "auto"; }
        audio.volume = 1; audio.currentTime = 0;
        const pr = audio.play(); if (pr && pr.catch) pr.catch(() => {});
      } else if (audio && !audio.paused){
        const a = audio, giu = setInterval(() => { a.volume = Math.max(0, a.volume - .1); if (a.volume <= 0){ clearInterval(giu); a.pause(); } }, 60);
      }
    } catch(e){}
  }
  function vai(d){
    if (d < 0 && i === 0) return chiudi();            /* dalla prima scheda, indietro torna al sito */
    const j = Math.max(0, Math.min(N - 1, i + d)); if (j !== i){ i = j; mostra(); }
  }
  /* dall'ultima schermata del tutorial, andando a destra si entra nelle schede */
  if (typeof vTutorial === "function" && typeof TUTORIAL !== "undefined"){
    const vTutorialOriginale = vTutorial;
    vTutorial = function(k, verso){
      const r = vTutorialOriginale(k, verso);
      if (k === TUTORIAL.length - 1 && typeof scenaCorrente !== "undefined" && scenaCorrente){
        const sc = scenaCorrente, prima = sc._frecce || {};
        sc._frecce = { avanti: () => { i = 0; apri(); }, indietro: prima.indietro || (() => {}) };
        if (typeof scorrimento === "function"){ const salva = sc._frecce; scorrimento(sc, () => { i = 0; apri(); }, () => {}); sc._frecce = salva; }
      }
      return r;
    };
  }
  function apri(){
    if (!box) costruisci();
    aperta = true; box.classList.add("on"); mostra();
    if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
  }
  function chiudi(){ aperta = false; musica(false); if (box) box.classList.remove("on"); }

  addEventListener("keydown", e => {
    if (aperta){
      const k = e.key;
      const avanti = ["ArrowRight","ArrowDown","PageDown"," ","Enter"].includes(k);
      const indietro = ["ArrowLeft","ArrowUp","PageUp","Backspace"].includes(k);
      if (avanti || indietro || k === "Home" || k === "End" || k === "Escape"){
        e.preventDefault(); e.stopImmediatePropagation();
        if (avanti) vai(1); else if (indietro) vai(-1);
        else if (k === "Home"){ i = 0; mostra(); } else if (k === "End"){ i = N - 1; mostra(); }
        else chiudi();
      }
      return;
    }
    const t = e.target;
    if (t && t.closest && t.closest("input,textarea,[contenteditable]")) return;
    if (e.ctrlKey || e.metaKey || e.altKey || !e.key || e.key.length !== 1){ return; }
    seq = (seq + e.key.toLowerCase()).slice(-3);
    if (seq === "lim"){ seq = ""; e.preventDefault(); apri(); }
  }, true);
  addEventListener("resize", () => { if (aperta) mostra(); });
  const daIndirizzo = () => { if (location.hash === "#lim") apri(); };
  addEventListener("hashchange", daIndirizzo);
  if (document.readyState === "complete") setTimeout(daIndirizzo, 400); else addEventListener("load", () => setTimeout(daIndirizzo, 400));
})();
