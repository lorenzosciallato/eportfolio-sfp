import os, re, base64
root=os.path.dirname(os.path.abspath(__file__))
A=f'{root}/out/site/assets'
s=open(f'{root}/src/app.html').read()
b64=lambda f: base64.b64encode(open(f,'rb').read()).decode()
# caratteri dell'interfaccia incorporati: niente attesa del font
s=re.sub(r'url\(assets/([\w-]+)\.woff2\)', lambda m: f'url(data:font/woff2;base64,{b64(f"{A}/{m.group(1)}.woff2")})', s)
# illustrazioni incorporate: compaiono tutte insieme, anche con connessione lenta
nomi=[f'f{i}' for i in range(1,8)]+[f'q{i}' for i in range(1,8)]+['t-libri','q-accesso']
img=",".join(f'"{n}":"data:image/webp;base64,{b64(f"{A}/{n}.webp")}"' for n in nomi)
assert '/*IMG*/' in s; s=s.replace('/*IMG*/', img)
import os
api=open(f'{root}/api.txt').read().strip() if os.path.exists(f'{root}/api.txt') else ''
assert '/*API*/' in s; s=s.replace('/*API*/', api)
assert '{{' not in s
open(f'{root}/out/site/app.html','w').write(s)
full='<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<link rel="manifest" href="manifest.webmanifest">\n<meta name="theme-color" content="#faf8f4">\n<link rel="icon" type="image/png" sizes="32x32" href="icone/favicon-32.png">\n<link rel="icon" type="image/png" sizes="64x64" href="icone/favicon-64.png">\n<link rel="apple-touch-icon" href="icone/apple-touch-icon.png">\n<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-title" content="E-Portfolio">\n<meta name="apple-mobile-web-app-status-bar-style" content="default">\n<style>[hidden]{display:none!important}</style>\n</head>\n<body>\n'+s+'\n</body>\n</html>\n'
open(f'{root}/out/site/index.html','w').write(full)
# copia per l'uso senza connessione dopo la prima visita
open(f'{root}/out/site/sw.js','w').write('''const C="eportfolio-sfp-v4";
const FILE=["./","index.html","privacy.html","assets/tit-700.ttf","assets/txt-400.ttf","assets/txt-400i.ttf","assets/txt-600.ttf","assets/jspdf.min.js","manifest.webmanifest","icone/icona-192.png","icone/apple-touch-icon.png","icone/favicon-32.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(FILE)).catch(()=>{}));self.skipWaiting();});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim();});
self.addEventListener("fetch",e=>{if(e.request.method!=="GET")return;
  if(e.request.mode==="navigate"){e.respondWith(fetch(e.request).then(r=>{caches.open(C).then(c=>c.put("index.html",r.clone()));return r;}).catch(()=>caches.match("index.html")));return;}
  e.respondWith(caches.match(e.request).then(h=>h||fetch(e.request).then(r=>{if(r.ok){const k=r.clone();caches.open(C).then(c=>c.put(e.request,k));}return r;})));});
''')
print(len(s)//1024,'KB html')

# informativa privacy
import shutil
shutil.copy(f'{root}/src/privacy.html', f'{root}/out/site/privacy.html')
