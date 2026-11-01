# Portrete rotunde pentru hărțile Eroi și Istorie (Ralph's Vault): sursă Wikipedia/Commons -> decupaj pătrat 256x256
import json,sys,io,os,urllib.request
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wikiimg import UA
from PIL import Image,ImageDraw
S=os.path.dirname(os.path.abspath(__file__));out=sys.argv[1] if len(sys.argv)>1 else None
src=json.load(open(f'{S}/src_hartiB.json'));alt=json.load(open(f'{S}/istorie_alt.json'))
src['istorie']['minoici']=alt['minoici'][0][1];src['istorie']['miceni']=alt['miceni'][2][1];src['istorie']['colonizare']=alt['colonizare'][0][1]
src['istorie']['clistene']=alt['clistene'][0][1];src['istorie']['corint']=alt['corint'][0][1];src['istorie']['cadere']=alt['cadere'][0][1];src['istorie']['revolutie']=alt['revolutie'][0][1]
# fracții (x0,y0,x1,y1) din imaginea întreagă; implicit: pătrat sus (portret) / centru (peisaj)
CR={'eroi':{'heracle':(0,0,1,.55),'hidra':(.25,.1,.95,.8),'cerber':(.3,.0,.9,.95),'tezeu':(.3,.2,.85,.8),'minotaur':(.15,.0,.85,.7),'ariadna':(.45,.05,1,.8),'perseu':(.15,.0,.85,.5),'meduza':(.15,.1,.85,.95),'andromeda':(.45,.15,.95,.7),'iason':(.1,0,.9,.4),'medeea':(.1,.1,.55,.7),'orfeu':(.3,.2,.75,.7),'ahile':(.0,.0,.8,.55),'patrocle':(.15,.0,.75,.5),'hector':(.35,.0,.9,.5),'paris':(.0,.2,.7,.85),'elena':(.2,.0,.9,.5),'menelau':(.15,.0,.9,.55),'agamemnon':(.0,.1,.9,.65),'odiseu':(.1,.2,.9,.9),'penelopa':(.15,.0,.85,.5),'telemah':(.0,.4,.7,1),'polifem':(.2,.05,.95,.8)},
 'istorie':{'homer':(.1,.0,.9,.6),'clistene':(.0,.25,1,.95),'socrate':(.1,.0,.95,.6),'alexandru':(.1,.0,.9,.7),'arhimede':(.05,.1,.95,.75),'revolutie':(.0,.15,1,.65),'troia':(.1,.0,.9,.9),'peloponesiac':(.05,.1,.85,.8),'alexandria':(.1,.1,.95,.8),'maraton':(.1,.05,.9,.8),'colonizare':(.0,.35,1,.98)}}
res={}
for name in src:
    for k,u in src[name].items():
        if not u:continue
        x=Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(u,headers=UA)).read())).convert('RGB');W,H=x.size
        c=CR.get(name,{}).get(k)
        if c:bx=[c[0]*W,c[1]*H,c[2]*W,c[3]*H]
        else:bx=[0,0,W,H]
        w=bx[2]-bx[0];h=bx[3]-bx[1];s=min(w,h) if not c else max(w,h)
        s=min(s,W,H) if not c else min(max(w,h),W,H)
        cx=(bx[0]+bx[2])/2;cy=(bx[1]+bx[3])/2 if c else ((bx[1]+bx[3])/2 if W>=H else s/2+H*.03)
        x0=min(max(0,cx-s/2),W-s);y0=min(max(0,cy-s/2),H-s)
        y=x.crop((int(x0),int(y0),int(x0+s),int(y0+s))).resize((256,256),Image.LANCZOS);res[(name,k)]=y
        if out:os.makedirs(f'{out}/{name}',exist_ok=True);y.save(f'{out}/{name}/{k}.jpg',quality=80)
for name in src:
    items=[(k,v) for (n,k),v in res.items() if n==name];sh=Image.new('RGB',(6*160,((len(items)+5)//6)*175),'white');d=ImageDraw.Draw(sh)
    for i,(k,y) in enumerate(items):
        m=Image.new('L',(150,150),0);ImageDraw.Draw(m).ellipse((0,0,149,149),fill=255);sh.paste(y.resize((150,150)),((i%6)*160,(i//6)*175),m);d.text(((i%6)*160+30,(i//6)*175+155),k,fill='black')
    sh.save(f'{S}/poze/{name}_cerc.jpg')
print('ok',len(res))
