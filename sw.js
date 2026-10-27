// Ralph's Vault — tot ce trebuie ca aplicația să meargă și fără internet
const C='ralph-v9',IMG='ralph-img-v1';
const F=['./','./index.html','./manifest.json','./icon-180.png','./icon-192.png','./icon-512.png','./logo.png','./vault-bg.jpg','./intro.mp4','./data/imagini.json','./data/trivia.json','./data/geo.json','./data/cars/index.json','./data/cars/2026.json','./data/cars/clasice.json','./geo/europa.json','./geo/asia.json','./geo/africa.json','./geo/america_nord.json','./geo/america_sud.json','./geo/oceania.json'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>Promise.all(F.map(f=>c.add(f).catch(()=>{})))));self.skipWaiting()});
// pozele stau într-un cache separat, care nu se golește la versiunile noi
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C&&x!==IMG).map(x=>caches.delete(x)))));self.clients.claim()});
async function video(req){const c=await caches.open(C);let r=await c.match(new URL('intro.mp4',self.registration.scope).href);
 if(!r){try{return await fetch(req)}catch(x){return new Response('',{status:404})}}
 const range=req.headers.get('range');if(!range)return r;
 // iPhone cere video-ul pe bucăți (Range); le tăiem din copia salvată
 const buf=await r.arrayBuffer(),m=/bytes=(\d+)-(\d*)/.exec(range)||[0,'0',''],s=+m[1],en=m[2]?Math.min(+m[2],buf.byteLength-1):buf.byteLength-1;
 return new Response(buf.slice(s,en+1),{status:206,headers:{'Content-Type':'video/mp4','Content-Range':`bytes ${s}-${en}/${buf.byteLength}`,'Content-Length':String(en-s+1),'Accept-Ranges':'bytes'}})}
self.addEventListener('fetch',e=>{const u=new URL(e.request.url);if(e.request.method!=='GET'||u.origin!==location.origin)return;
 if(u.pathname.endsWith('.mp4')){e.respondWith(video(e.request));return}
 if(u.pathname.includes('/img/')){e.respondWith(caches.open(IMG).then(c=>c.match(e.request).then(r=>r||fetch(e.request).then(n=>{if(n.ok)c.put(e.request,n.clone());return n}))));return}
 e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request,{ignoreSearch:true}).then(r=>r||caches.match('./index.html'))))});
