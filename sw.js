const C="eportfolio-sfp-v7";
const FILE=["./","index.html","privacy.html","assets/tit-700.ttf","assets/txt-400.ttf","assets/txt-400i.ttf","assets/txt-600.ttf","assets/jspdf.min.js","manifest.webmanifest","icone/icona-192.png","icone/apple-touch-icon.png","icone/favicon-32.png","assets/k01.webp","assets/k02.webp","assets/k03.webp","assets/k04.webp","assets/k05.webp","assets/k06.webp","assets/k07.webp","assets/k08.webp","assets/k09.webp","assets/k10.webp","assets/k11.webp","assets/k12.webp","assets/k13.webp","assets/k14.webp","assets/k15.webp","assets/k16.webp"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(FILE)).catch(()=>{}));self.skipWaiting();});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim();});
self.addEventListener("fetch",e=>{if(e.request.method!=="GET")return;
  if(e.request.mode==="navigate"){e.respondWith(fetch(e.request).then(r=>{caches.open(C).then(c=>c.put("index.html",r.clone()));return r;}).catch(()=>caches.match("index.html")));return;}
  e.respondWith(caches.match(e.request).then(h=>h||fetch(e.request).then(r=>{if(r.ok){const k=r.clone();caches.open(C).then(c=>c.put(e.request,k));}return r;})));});
