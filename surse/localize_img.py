# Descarcă pozele (Wikipedia/Commons) folosite în date, le micșorează și le pune în aplicație, ca să meargă fără internet.
import json,os,sys,hashlib,io,urllib.request,time
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
APP=sys.argv[1];UA={'User-Agent':'RalphApp/1.0 (euclide.run@gmail.com)'}
def local(url,sub):
    h=hashlib.md5(url.encode()).hexdigest()[:12];rel=f'img/{sub}/{h}.jpg';fp=os.path.join(APP,rel)
    if os.path.exists(fp):return rel
    for k in range(4):
        try:
            b=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=30).read()
            im=Image.open(io.BytesIO(b)).convert('RGB');im.thumbnail((480,480))
            os.makedirs(os.path.dirname(fp),exist_ok=True);im.save(fp,'JPEG',quality=74,optimize=True);return rel
        except Exception as e:
            time.sleep(2+k*3);err=e
    print('EȘEC',url[:90],err);return url
jobs=[]
geo=json.load(open(f'{APP}/data/geo.json'))
for iso,t in geo['tari'].items():
    if t.get('capImg','').startswith('http'):jobs.append((t,'capImg','cap'))
for iso,L in geo['det'].items():
    for x in L:
        if x.get('img','').startswith('http'):jobs.append((x,'img','geo'))
cars={}
for f in os.listdir(f'{APP}/data/cars'):
    if f!='index.json':
        cars[f]=json.load(open(f'{APP}/data/cars/{f}'))
        for c in cars[f]:
            if c.get('img','').startswith('http'):jobs.append((c,'img','cars'))
print('de descărcat',len(jobs))
with ThreadPoolExecutor(6) as ex:
    res=list(ex.map(lambda j:local(j[0][j[1]],j[2]),jobs))
for (o,k,_),r in zip(jobs,res):o[k]=r
json.dump(geo,open(f'{APP}/data/geo.json','w'),ensure_ascii=False,separators=(',',':'))
for f,L in cars.items():json.dump(L,open(f'{APP}/data/cars/{f}','w'),ensure_ascii=False,separators=(',',':'))
# lista tuturor pozelor locale, pentru descărcarea offline din aplicație
allimg=sorted({r for r in res if not r.startswith('http')})
json.dump(allimg,open(f'{APP}/data/imagini.json','w'))
tot=sum(os.path.getsize(os.path.join(APP,r)) for r in allimg)
print('locale',len(allimg),'rămase online',sum(r.startswith('http') for r in res),f'{tot/1e6:.1f} MB')
