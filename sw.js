const C='ralph-v5',F=['./data/cars/index.json','./data/cars/2026.json','./','./index.html','./manifest.json','./icon-180.png','./icon-192.png','./icon-512.png','./data/trivia.json','./data/geo.json','./geo/europa.json','./geo/asia.json','./geo/africa.json','./geo/america_nord.json','./geo/america_sud.json','./geo/oceania.json'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>Promise.all(F.map(f=>c.add(f).catch(()=>{})))));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim()});
// doar fișierele aplicației trec prin cache; pozele de pe Wikipedia le ține browserul
self.addEventListener('fetch',e=>{if(e.request.method!=='GET'||new URL(e.request.url).origin!==location.origin)return;
 e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request,{ignoreSearch:true}).then(r=>r||caches.match('./index.html'))))});
