import os,json,urllib.request,random
P,N,B,R,Q,K=1,2,3,4,5,6
V=(0,100,320,330,500,900,20000)
PA=(0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,50,10,10,20,30,30,20,10,10,5,5,10,25,25,10,5,5,0,0,0,20,20,0,0,0,5,-5,-10,0,0,-10,-5,5,5,10,10,-20,-20,10,10,5,0,0,0,0,0,0,0,0)
KN=(-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,0,15,20,20,15,0,-30,-30,5,10,15,15,10,5,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50)
BI=(-20,-10,-10,-10,-10,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-20,-10,-10,-10,-10,-10,-10,-20)
RO=(0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,0,0,0,5,5,0,0,0)
QU=(-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,5,5,5,0,-10,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,-5,-10,5,5,5,5,5,0,-10,-10,0,5,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20)
KI=(-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20,20,0,0,0,0,20,20,20,30,10,0,0,10,30,20)
PS=(0,PA,KN,BI,RO,QU,KI)
KD=(31,33,14,18,-31,-33,-14,-18)
GD=(1,-1,16,-16,15,17,-15,-17)
BD=(15,17,-15,-17)
RD=(1,-1,16,-16)
INF=10**6
MATE=100000
BUD=120000
ND=0
KP=[4,116]
KL=[[0,0] for _ in range(128)]
_R=random.Random(20261116)
ZK=[_R.getrandbits(64) for _ in range(1562)]
TT={}
HS=[]
H=0
def zk(p,s):return ZK[(p+6 if p<0 else p+5)*128+s]
ZS=ZK[1536];ZC=ZK[1537:1553];ZE=ZK[1553:1562]
def hh(b,t,c,e):
    h=ZS if t==1 else 0
    h^=ZC[c]
    if e>=0:h^=ZE[e&7]
    for i in range(128):
        p=b[i]
        if p:h^=zk(p,i)
    return h
class AB(Exception):pass
def atk(b,s,by):
    if by==1:
        for d in (-15,-17):
            u=s+d
            if not u&0x88 and b[u]==P:return 1
    else:
        for d in (15,17):
            u=s+d
            if not u&0x88 and b[u]==-P:return 1
    for d in KD:
        u=s+d
        if not u&0x88 and b[u]==by*N:return 1
    for d in GD:
        u=s+d
        if not u&0x88 and b[u]==by*K:return 1
    for d in BD:
        u=s+d
        while not u&0x88:
            q=b[u]
            if q:
                if q==by*B or q==by*Q:return 1
                break
            u+=d
    for d in RD:
        u=s+d
        while not u&0x88:
            q=b[u]
            if q:
                if q==by*R or q==by*Q:return 1
                break
            u+=d
    return 0
def gen(b,t,c,e,cp=False):
    ms=[]
    for f in range(128):
        if f&0x88:continue
        p=b[f]
        if p*t<=0:continue
        a=abs(p)
        if a==P:
            d=16*t;u=f+d
            if not u&0x88 and not b[u]:
                r=u>>4
                if r==7 or r==0:
                    for pr in (Q,R,B,N):ms.append((f,u,pr))
                elif not cp:
                    ms.append((f,u,0))
                    if (t==1 and (f>>4)==1) or (t==-1 and (f>>4)==6):
                        u2=f+2*d
                        if not b[u2]:ms.append((f,u2,0))
            for dd in (d-1,d+1):
                u=f+dd
                if u&0x88:continue
                q=b[u]
                if q*t<0 or u==e:
                    r=u>>4
                    if r==7 or r==0:
                        for pr in (Q,R,B,N):ms.append((f,u,pr))
                    else:ms.append((f,u,0))
        elif a==N or a==K:
            for dd in (KD if a==N else GD):
                u=f+dd
                if u&0x88:continue
                q=b[u]
                if q*t<0 or (not cp and not q):ms.append((f,u,0))
            if a==K and not cp:
                o=0 if t==1 else 112
                if c&(1 if t==1 else 4) and not b[o+5] and not b[o+6] and b[o+7]==t*R and b[o+4]==t*K and not atk(b,o+4,-t) and not atk(b,o+5,-t) and not atk(b,o+6,-t):ms.append((o+4,o+6,0))
                if c&(2 if t==1 else 8) and not b[o+3] and not b[o+2] and not b[o+1] and b[o]==t*R and b[o+4]==t*K and not atk(b,o+4,-t) and not atk(b,o+3,-t) and not atk(b,o+2,-t):ms.append((o+4,o+2,0))
        else:
            for dd in (BD if a==B else RD if a==R else BD+RD):
                u=f+dd
                while not u&0x88:
                    q=b[u]
                    if q:
                        if q*t<0:ms.append((f,u,0))
                        break
                    if not cp:ms.append((f,u,0))
                    u+=dd
    return ms
def mk(b,t,c,e,m):
    global H
    f,u,pr=m;p=b[f];cap=b[u];ec=-1;ok=-1
    HS.append(H)
    if abs(p)==P and u==e and not cap:
        ec=u-16*t;cap=b[ec];b[ec]=0
    np=pr*t if pr else p
    b[u]=np;b[f]=0
    if abs(p)==K:
        ok=KP[0 if t==1 else 1];KP[0 if t==1 else 1]=u
        if u-f==2:b[f+1]=b[f+3];b[f+3]=0
        elif f-u==2:b[f-1]=b[f-4];b[f-4]=0
    nc=c
    if abs(p)==K:
        if t==1:nc&=~3
        else:nc&=~12
    if f==0 or u==0:nc&=~2
    if f==7 or u==7:nc&=~1
    if f==112 or u==112:nc&=~8
    if f==119 or u==119:nc&=~4
    ne=-1
    if abs(p)==P and abs(u-f)==32:ne=(f+u)//2
    H^=zk(p,f)^zk(np,u)
    if cap:H^=zk(cap,ec if ec>=0 else u)
    if abs(p)==K:
        if u-f==2:H^=zk(t*R,f+3)^zk(t*R,f+1)
        elif f-u==2:H^=zk(t*R,f-4)^zk(t*R,f-1)
    H^=ZS^ZC[c]^ZC[nc]
    if e>=0:H^=ZE[e&7]
    if ne>=0:H^=ZE[ne&7]
    return cap,ec,ok,nc,ne
def un(b,t,m,cap,ec,ok):
    global H
    f,u,pr=m;p=b[u]
    b[f]=t*P if pr else p;b[u]=0
    if ec>=0:b[ec]=cap
    elif cap:b[u]=cap
    if abs(p)==K:
        if ok>=0:KP[0 if t==1 else 1]=ok
        if u-f==2:b[f+3]=b[f+1];b[f+1]=0
        elif f-u==2:b[f-4]=b[f-1];b[f-1]=0
    H=HS.pop()
def ev(b):
    s=0;wb=0;bb=0
    for i in range(128):
        if i&0x88:continue
        p=b[i]
        if not p:continue
        a=abs(p)
        if a==B:
            if p>0:wb+=1
            else:bb+=1
        v=V[a]+PS[a][(7-(i>>4))*8+(i&7) if p>0 else (i>>4)*8+(i&7)]
        s+=v if p>0 else -v
    if wb>=2:s+=30
    if bb>=2:s-=30
    return s
def ms(b,t,m,pl,tm=None):
    f,u,pr=m;q=b[u];s=0
    if q:s+=10*V[abs(q)]-V[abs(b[f])]//32
    if pr:s+=900
    if tm is not None and m==tm:s+=20000
    if pl<128:
        k=KL[pl]
        if m==k[0]:s+=9000
        elif m==k[1]:s+=4000
    return s
def qs(b,t,c,e,al,be,pl):
    global ND
    ND+=1
    if ND>=BUD:raise AB
    if pl>40:return ev(b)*t
    ch=atk(b,KP[0 if t==1 else 1],-t)
    if not ch:
        st=ev(b)*t
        if st>=be:return be
        if st>al:al=st
    mvs=gen(b,t,c,e,not ch)
    mvs.sort(key=lambda m:-ms(b,t,m,pl))
    lg=0
    for m in mvs:
        cap,ec,ok,nc,ne=mk(b,t,c,e,m)
        if atk(b,KP[0 if t==1 else 1],-t):
            un(b,t,m,cap,ec,ok);continue
        lg+=1
        sc=-qs(b,-t,nc,ne,-be,-al,pl+1)
        un(b,t,m,cap,ec,ok)
        if sc>al:al=sc
        if al>=be:break
    if ch and not lg:return -MATE+pl
    return al
def sr(b,t,c,e,d,al,be,pl):
    global ND
    ND+=1
    if ND>=BUD:raise AB
    if d<=0:return qs(b,t,c,e,al,be,pl)
    a0=al;bm=None;ent=TT.get(H)
    if ent and ent[0]>=d:
        sc,fl,_,_=ent
        if fl==0:return sc
        if fl==1 and sc>=be:return sc
        if fl==2 and sc<=al:return sc
    tm=ent[3] if ent else None
    mvs=gen(b,t,c,e)
    mvs.sort(key=lambda m:-ms(b,t,m,pl,tm))
    lg=0
    for m in mvs:
        cap,ec,ok,nc,ne=mk(b,t,c,e,m)
        if atk(b,KP[0 if t==1 else 1],-t):
            un(b,t,m,cap,ec,ok);continue
        lg+=1
        sc=-sr(b,-t,nc,ne,d-1,-be,-al,pl+1)
        un(b,t,m,cap,ec,ok)
        if sc>al:al=sc;bm=m
        if al>=be:
            if pl<128 and not b[m[1]] and not m[2]:
                if KL[pl][0]!=m:KL[pl][1]=KL[pl][0];KL[pl][0]=m
            break
    if not lg:
        if atk(b,KP[0 if t==1 else 1],-t):return -MATE+pl
        return 0
    if abs(al)<MATE-1000:
        if len(TT)>250000:TT.clear()
        TT[H]=(d,al,1 if al>=be else 2 if al<=a0 else 0,bm)
    return al
def pf(fn):
    global H
    p=fn.split();b=[0]*128;rs=p[0].split('/')
    for r in range(8):
        f=0
        for ch in rs[r]:
            if ch.isdigit():f+=int(ch)
            else:
                b[(7-r)*16+f]='PNBRQK'.index(ch.upper())+1 if ch.isupper() else -('PNBRQK'.index(ch.upper())+1)
                f+=1
    t=1 if p[1]=='w' else -1
    c=0
    if len(p)>2:
        if 'K' in p[2]:c|=1
        if 'Q' in p[2]:c|=2
        if 'k' in p[2]:c|=4
        if 'q' in p[2]:c|=8
    e=-1
    if len(p)>3 and p[3]!='-':e=(int(p[3][1])-1)*16+ord(p[3][0])-97
    for i in range(128):
        if b[i]==K:KP[0]=i
        elif b[i]==-K:KP[1]=i
    H=hh(b,t,c,e)
    return b,t,c,e
def tu(m):
    f,u,pr=m
    s=chr(97+(f&7))+str((f>>4)+1)+chr(97+(u&7))+str((u>>4)+1)
    return s+({Q:'q',R:'r',B:'b',N:'n'}.get(pr,'') if pr else '')
def fu(s):
    f=(ord(s[0])-97)+(int(s[1])-1)*16;u=(ord(s[2])-97)+(int(s[3])-1)*16
    pr={'q':Q,'r':R,'b':B,'n':N}.get(s[4],0) if len(s)>4 else 0
    return (f,u,pr)
def rp(ms):
    # Replay the game so far; return hashes of positions already seen
    # twice (a move into one of them draws at once by threefold).
    b,t,c,e=pf('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    s={H:1}
    for u in ms:
        _,_,_,c,e=mk(b,t,c,e,fu(u));t=-t;s[H]=s.get(H,0)+1
    del HS[:]
    return {h for h,n in s.items() if n>1}
def th(b,t,c,e,legal,bn=None):
    global ND
    mvs=[fu(s) for s in legal]
    if bn and ev(b)*t>0:
        # Ahead: refuse a move that repeats a position a third time
        # (instant draw); take the draw only when behind or equal.
        f=[]
        for m in mvs:
            cap,ec,ok,nc,ne=mk(b,t,c,e,m)
            if H not in bn:f.append(m)
            un(b,t,m,cap,ec,ok)
        if f:mvs=f
    mvs.sort(key=lambda m:-ms(b,t,m,0))
    ND=0;best=mvs[0]
    try:
        d=1
        while d<64:
            cur=None;a=-INF
            for m in mvs:
                cap,ec,ok,nc,ne=mk(b,t,c,e,m)
                sc=-sr(b,-t,nc,ne,d-1,-INF,-a,1)
                un(b,t,m,cap,ec,ok)
                if sc>a:a=sc;cur=m
            if cur is None:break
            best=cur
            mvs.remove(best);mvs.insert(0,best)
            d+=1
    except AB:pass
    return best
def po(u,o):
    q=urllib.request.Request(u,data=json.dumps(o).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(q,timeout=120) as r:return json.load(r)
def main():
    base=os.environ['MAKEFUN_ENV_URL']
    while 1:
        g=po(base+'/game',{})
        if g.get('status')=='done':return
        while g.get('status')=='your_move':
            lg=g.get('legal_moves') or []
            if not lg:
                po(base+'/resign',{'game':g['game']});break
            bn=rp(g.get('moves') or [])
            b,t,c,e=pf(g['fen'])
            g=po(base+'/move',{'game':g['game'],'move':tu(th(b,t,c,e,lg,bn))})
if __name__=='__main__':main()
