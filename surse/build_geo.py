import json,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from wikiimg import thumbs
T=json.load(open('data/tari.json'));CI=json.load(open('data/cap_img.json'))
for k,v in T.items():
    if v['cap'] in CI:v['capImg']=CI[v['cap']]
det={}
if os.path.exists('data/detalii.json'):
    D=json.load(open('data/detalii.json'))
    titles=sorted({x['wiki'] for L in D.values() for x in L if x.get('wiki')})
    im=thumbs(titles,'en',400)
    miss=[]
    for iso,L in D.items():
        det[iso]=[]
        for x in L:
            y={'cat':x['cat'],'nume':x['nume'],'info':x['info']}
            if x.get('wiki') in im:y['img']=im[x['wiki']]
            else:miss.append(f"{iso}:{x['nume']}")
            det[iso].append(y)
    print('detalii',sum(len(v) for v in det.values()),'fără poză',len(miss),miss[:40])
json.dump({'tari':T,'det':det},open(sys.argv[1],'w'),ensure_ascii=False,separators=(',',':'))
print('scris',os.path.getsize(sys.argv[1])//1024,'KB')
