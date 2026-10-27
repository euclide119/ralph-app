const C='ralph-v7',F=['./','./index.html','./manifest.json','./icon-180.png','./icon-192.png','./icon-512.png','./logo.png','./vault-bg.jpg','./data/trivia.json','./data/geo.json','./data/cars/index.json','./data/cars/2026.json','./data/cars/clasice.json','./geo/europa.json','./geo/asia.json','./geo/africa.json','./geo/america_nord.json','./geo/america_sud.json','./geo/oceania.json'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>Promise.all(F.map(f=>c.add(f).catch(()=>{})))));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim()});
// doar fișierele aplicației trec prin cache; pozele de pe Wikipedia și video-ul (cereri pe bucăți) le servește direct rețeaua
self.addEventListener('fetch',e=>{const u=new URL(e.request.url);if(e.request.method!=='GET'||u.origin!==location.origin||u.pathname.endsWith('.mp4'))return;
 e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request,{ignoreSearch:true}).then(r=>r||caches.match('./index.html'))))});
