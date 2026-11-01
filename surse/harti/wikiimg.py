# Poze de pe Wikipedia/Commons pentru Ralph's Vault (titluri exacte de articol -> miniatură)
import json,urllib.request,urllib.parse,time
UA={'User-Agent':'RalphApp/1.0 (euclide.run@gmail.com)'}
def thumbs(titles,lang='en',size=640):
    out={}
    for i in range(0,len(titles),40):
        ch=titles[i:i+40]
        q=urllib.parse.urlencode({'action':'query','titles':'|'.join(ch),'prop':'pageimages|pageprops','piprop':'thumbnail','pithumbsize':size,'redirects':1,'format':'json','ppprop':'disambiguation'})
        d=json.load(urllib.request.urlopen(urllib.request.Request(f'https://{lang}.wikipedia.org/w/api.php?{q}',headers=UA)))['query']
        m={}
        for k in ('normalized','redirects'):
            for x in d.get(k,[]):m[x['from']]=x['to']
        pages={p['title']:p for p in d['pages'].values()}
        for t in ch:
            tt=t
            for _ in range(3):tt=m.get(tt,tt)
            p=pages.get(tt)
            if p and 'thumbnail' in p and 'disambiguation' not in p.get('pageprops',{}):out[t]=p['thumbnail']['source']
        time.sleep(.3)
    return out
def commons(q,n=10,size=640):
    u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','generator':'search','gsrsearch':q,'gsrnamespace':6,'gsrlimit':n,'prop':'imageinfo','iiprop':'url','iiurlwidth':size,'format':'json'})
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA)))
    ps=sorted(d.get('query',{}).get('pages',{}).values(),key=lambda p:p.get('index',99))
    return [(p['title'],p['imageinfo'][0]['thumburl']) for p in ps if p['title'].lower().endswith(('.jpg','.jpeg'))]
