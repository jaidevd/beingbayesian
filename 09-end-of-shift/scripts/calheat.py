import sys, os, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm, numpy as np, pandas as pd
from matplotlib.patches import FancyBboxPatch
D=sys.argv[1]; OUT=sys.argv[2]; sys.argv=[sys.argv[0],D,'none']
exec(open(os.path.dirname(os.path.abspath(__file__))+'/tab.py').read().split("if __name__")[0])
P=pd.read_pickle(D+'/P3.pkl').reset_index(drop=True)
P=P.merge(pd.read_parquet(D+'/employer.parquet'),on=k,how='left')
raw=pd.read_parquet('/home/jaidevd/src/time-use-survey-2024/clean/per-tus-2024.parquet',columns=['sub_round']).reset_index()
P=P.merge(raw.drop_duplicates(k)[k+['sub_round']],on=k,how='left')
mins=G.groupby(k+['g']).size().unstack(fill_value=0)*30
GRP=[c for c in mins.columns if c!='sleep']   # sleep is always the biggest block, so it is left out
P=P.merge(mins[GRP].reset_index(),on=k,how='left').fillna({c:0 for c in GRP})
for f in ['Bold','Regular']: fm.fontManager.addfont(f"/home/jaidevd/.local/share/fonts/Lora-{f}.ttf")
plt.rcParams['font.family']='Lora'; BG='papayawhip'
DAYS=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']; QL=['Q1','Q2','Q3','Q4']
NMIN=30; COVMIN=0.9
F=P.gender=='female'; M=P.gender=='male'
# employer type is recorded only on paid-work rows, so the public group is only usable where nearly everyone has a label
PUB=P.emp=='public'
COH=[('in knowledge work',P.kw_core,False),('in blue-collar work',P.blue,False),('in public employment',PUB,True)]
PANELS=[(f"{gn} {cn}",cm&gm,emp,gm) for gn,gm in [('Women',F),('Men',M)] for cn,cm,emp in COH]
REN={'domestic':'housework','eat/selfcare':'meals/self-care'}
COL={'paid work':'teal','commute':'orchid','housework':'maroon','care':'#C62828','leisure/media':'darkorange',
     'social/relig':'seagreen','meals/self-care':'darkgoldenrod'}
def grid(mask,emp,gm):
    top=np.full((7,4),None,dtype=object); m=np.full((7,4),np.nan); n=np.zeros((7,4),int); cov=np.ones((7,4))
    for i,dn in enumerate(DAYS):
        for q in range(4):
            cell=(P.day_of_week==dn)&(P.sub_round==q+1)
            c=P[mask&cell]; n[i,q]=len(c)
            if emp: cov[i,q]=P[gm&cell&P.emp.notna()].shape[0]/max(P[gm&cell].shape[0],1)
            if len(c)>=NMIN and cov[i,q]>=COVMIN:
                mm=(c[GRP].mul(c.w,axis=0)).sum()/c.w.sum(); g=mm.idxmax()
                top[i,q]=REN.get(g,g); m[i,q]=mm[g]
    return top,m,n
vals=[grid(m,e,gm) for _,m,e,gm in PANELS]
seen=sorted({t for top,_,_ in vals for t in top.ravel() if t is not None},key=list(COL).index)
fig,axs=plt.subplots(2,3,figsize=(8.4,8.5)); fig.patch.set_facecolor(BG)
for ax,(nm,_,_,_),(top,m,n) in zip(axs.ravel(),PANELS,vals):
    ax.set_facecolor(BG); ax.set_xlim(-0.75,4.1); ax.set_ylim(7.1,-0.1); ax.set_aspect('equal'); ax.axis('off')
    for i in range(7):
        for q in range(4):
            t=top[i,q]
            if t is None: c='#e6d9c3'; al=1
            else: c=COL[t]; al=0.35+0.65*float(np.clip((m[i,q]-120)/(480-120),0,1))
            ax.add_patch(FancyBboxPatch((q+0.06,i+0.06),0.88,0.88,boxstyle='round,pad=0,rounding_size=0.15',fc=c,ec='none',alpha=al))
            if t is not None: ax.text(q+0.5,i+0.5,f'{m[i,q]/60:.1f}h',ha='center',va='center',fontsize=7,color='white' if al>0.7 else '0.2')
    for i,dn in enumerate(DAYS): ax.text(-0.12,i+0.5,dn[:3],ha='right',va='center',fontsize=8,fontweight='bold',color='0.25')
    for q in range(4): ax.text(q+0.5,-0.08,QL[q],ha='center',va='bottom',fontsize=7.5,color='0.35')
    ax.set_title(nm,fontsize=10.5,fontweight='bold',pad=20)
ttl=fig.suptitle('What Salaried India Does Most, Day by Day',fontweight='bold',fontsize=15,y=1.0)
sub=fig.text(0.5,0.955,"Each square shows the activity that takes the most time on that day of the week, sleep aside,\nwith its average hours; blank squares have too little data.",
         ha='center',va='top',fontsize=8.5,color='0.3')
from matplotlib.patches import Patch
leg=fig.legend(handles=[Patch(color=COL[l],label=l) for l in seen],frameon=False,fontsize=9,ncol=len(seen),loc='lower center',bbox_to_anchor=(0.5,0.075))
fig.text(0.01,0.005,"Knowledge work and blue-collar work are approximated from NIC industry codes\n(knowledge work also requires a graduate degree). Public employment is the\nemployer type recorded for paid work, not an NIC code.",ha='left',va='bottom',fontsize=7,color='0.4',linespacing=1.4)
fig.text(0.99,0.005,'Source: NSO Time Use Survey 2024, salaried, weighted.',ha='right',fontsize=7,color='0.4')
fig.subplots_adjust(left=0.06,right=0.97,top=0.84,bottom=0.13,hspace=0.32,wspace=0.12)
# centre title, subtitle and legend on the block of grids (the panels are not symmetric about the figure centre)
fig.canvas.draw(); r=fig.canvas.get_renderer()
bb=[ax.get_tightbbox(r) for ax in axs.ravel()]
cx=(min(b.x0 for b in bb)+max(b.x1 for b in bb))/2/fig.bbox.width
ttl.set_x(cx); sub.set_x(cx); leg.set_bbox_to_anchor((cx,0.075),transform=fig.transFigure)
print('grid centre at',round(cx,3),'of figure width')
fig.savefig(OUT+'/calendar-activity.png',dpi=300,facecolor=BG,bbox_inches='tight')
for nm,(top,m,n) in zip([p[0] for p in PANELS],vals): print(nm,'shown',int((top!=None).sum()),'of 28',sorted({t for t in top.ravel() if t}))
