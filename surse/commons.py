import json,urllib.request,urllib.parse,time
UA={'User-Agent':'RalphApp/1.0 (euclide.run@gmail.com)'}
BAD=('interior','engine','motor','badge','logo','dash','rear','heck','cockpit','wheel','detail','emblem','seat','.svg','.png','.tif','ad.','brochure','advert','model','toy','lego','hot wheels','diecast','scale')
def find(q,n=12):
    u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','generator':'search','gsrsearch':q,'gsrnamespace':6,'gsrlimit':n,'prop':'imageinfo','iiprop':'url','iiurlwidth':500,'format':'json'})
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA)))
    pages=sorted(d.get('query',{}).get('pages',{}).values(),key=lambda p:p.get('index',99))
    for p in pages:
        t=p['title'].lower()
        if any(b in t for b in BAD):continue
        if not t.endswith(('.jpg','.jpeg')):continue
        return p['title'],p['imageinfo'][0]['thumburl']
    return None
