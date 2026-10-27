# Unește fișele de mașini, verifică câmpurile, ia pozele de pe Wikipedia și scrie modulul anului în aplicație.
import json,sys,os,re,unicodedata
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wikiimg import thumbs
an,out=sys.argv[1],sys.argv[2];src=sys.argv[3:]
cars=[c for f in src for c in json.load(open(f))]
def slug(s):return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip('-')
need=['marca','model','tara','continent','an','tip','caroserie','versiune','motor','vmax','poveste','wiki']
err=[]
for c in cars:
    c['id']=slug(c['marca']+' '+c['model'])
    for k in need:
        if c.get(k) in (None,''):err.append(f"{c['id']}: lipsește {k}")
    if c.get('tip') not in ('electric','hibrid','benzină','diesel'):err.append(f"{c['id']}: tip {c.get('tip')}")
    if c.get('continent') not in ('europa','asia','america'):err.append(f"{c['id']}: continent {c.get('continent')}")
ids=[c['id'] for c in cars];dup={i for i in ids if ids.count(i)>1}
im=thumbs(sorted({c['wiki'] for c in cars}),'en',500)
miss=[]
for c in cars:
    if c['wiki'] in im:c['img']=im[c['wiki']]
    else:
        r=thumbs([c.get('img_ro') or c['wiki']],'ro',500)
        if r:c['img']=list(r.values())[0]
        else:miss.append(c['id'])
    c.pop('img_ro',None)
# poze alese de mână (generația corectă), dacă există
fp=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data',f'poze_{an}.json')
if os.path.exists(fp):
    P=json.load(open(fp))
    for c in cars:
        if c['id'] in P:c['img']=P[c['id']]
os.makedirs(os.path.join(out,'cars'),exist_ok=True)
json.dump(cars,open(os.path.join(out,'cars',f'{an}.json'),'w'),ensure_ascii=False,separators=(',',':'))
idx=os.path.join(out,'cars','index.json')
M=json.load(open(idx))['module'] if os.path.exists(idx) else [{'id':'2026','titlu':'Mașinile din 2026','emoji':'🚀'},{'id':'2025','titlu':'Mașinile din 2025','emoji':'⚡'},{'id':'2024','titlu':'Mașinile din 2024','emoji':'🏁'},{'id':'clasice','titlu':'Mașini clasice','emoji':'🏆'}]
for m in M:
    if m['id']==an:m['file']=f'cars/{an}.json';m['n']=len(cars)
json.dump({'module':M},open(idx,'w'),ensure_ascii=False,indent=1)
print('mașini',len(cars),'| erori',err,'| dubluri',dup,'| fără poză',miss)
