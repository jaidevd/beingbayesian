import sys, os, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm, numpy as np, pandas as pd
from matplotlib.patches import Patch, Circle, Wedge
D=sys.argv[1]; OUT=sys.argv[2]; sys.argv=[sys.argv[0],D,'none']
exec(open(os.path.dirname(os.path.abspath(__file__))+'/tab.py').read().split("if __name__")[0])
P=pd.read_pickle(D+'/P3.pkl').reset_index(drop=True)
P=P.merge(pd.read_parquet(D+'/employer.parquet'),on=k,how='left')
for f in ['Bold','Regular']: fm.fontManager.addfont(f"/home/jaidevd/.local/share/fonts/Lora-{f}.ttf")
plt.rcParams['font.family']='Lora'; BG='papayawhip'; FACE='#fffaf0'
COL={'paid work':'teal','commute':'orchid','housework':'maroon','care':'#C62828','leisure/media':'darkorange',
     'social/relig':'seagreen','meals/self-care':'darkgoldenrod','sleep':'#5b5b7a'}
# care and social/relig are never the top activity in any slot, so they are left out of the legend
REN={'domestic':'housework','eat/selfcare':'meals/self-care'}
def coarse(g):
    g=REN.get(g,g)
    return g if g in COL else 'meals/self-care'
G['g2']=G.g.map(coarse)
PM=range(16,40)  # slot 0 = 04:00, so 16 = 12:00 and 40 = 24:00
def modal(mask):
    ids=P[mask]; x=G.merge(ids[k+['w']],on=k)
    z=x[x.slot.isin(PM)]; t=z.groupby(['slot','g2']).w.sum().unstack(fill_value=0); t=t.div(t.sum(1),axis=0)
    at5=x[(x.slot==26)&(x.g=='paid work')].w.sum()/ids.w.sum()*100
    pw=x[(x.g=='paid work')&(x.slot>=16)].groupby(k).slot.max().rename('last').reset_index().merge(ids[k+['w']],on=k).sort_values('last')
    fin=(pw['last'].iloc[(pw.w.cumsum()<pw.w.sum()/2).sum()]+1-16)/2   # hours after noon at which the median person's last paid-work slot ends
    return t.idxmax(1), t.max(1), len(ids), at5, fin
def clock(ax,mask,title,stat):
    ax.set_xlim(-1.08,1.08); ax.set_ylim(-1.08,1.08); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Circle((0,0),1.0,fc=FACE,ec='0.25',lw=1.6)); ax.add_patch(Circle((0,0),0.985,fc='none',ec='0.6',lw=0.5))
    g,sh,n,at5,fin=modal(mask)
    ah=np.pi/2-fin/12*2*np.pi
    ax.add_patch(Wedge((0,0),0.81,np.degrees(ah),90,fc='teal',alpha=0.16,ec='none'))
    for s in PM:   # clock angle measured clockwise from 12
        a0=90-(s-16)*30/720*360
        ax.add_patch(Wedge((0,0),0.93,a0-15,a0,width=0.12,fc=COL[g[s]],alpha=0.4+0.6*float(sh[s]),ec=FACE,lw=0.8))
    for m in range(60):
        a=np.pi/2-m/60*2*np.pi; r0,r1=(0.94,0.985) if m%5==0 else (0.96,0.98)
        ax.plot([r0*np.cos(a),r1*np.cos(a)],[r0*np.sin(a),r1*np.sin(a)],color='0.3',lw=1.1 if m%5==0 else 0.4)
    for h in range(1,13):
        a=np.pi/2-h/12*2*np.pi
        ax.text(0.68*np.cos(a),0.68*np.sin(a),str(h),ha='center',va='center',fontsize=9.5,color='0.25',fontweight='normal')
    ax.text(0,0.55,'pm',ha='center',va='center',fontsize=8,color='0.25')
    ax.text(-0.60,0,'pm',ha='left',va='center',fontsize=8,color='0.25')
    a5=ah   # hour hand points to the median end of paid work
    ax.plot([0,0.5*np.cos(a5)],[0,0.5*np.sin(a5)],color='black',lw=3.5,solid_capstyle='round')
    ax.add_patch(Circle((0,0),0.045,fc='black',zorder=5))
    hh=12+fin; tm=f"{int(hh)%12 or 12}:{int(round((hh%1)*60)):02d} {'pm' if hh<24 else 'am'}"
    ax.text(0,-1.07,f"For {title},\npaid work ends at {tm}.",ha='center',va='top',fontsize=11,fontweight='bold',color='0.15',linespacing=1.4)
F=P.gender=='female'; M=P.gender=='male'
cohorts=[('in knowledge work',P.kw_core),('in blue-collar work',P.blue),('in public employment',P.emp=='public')]
fig,axs=plt.subplots(2,3,figsize=(9.6,7.7)); fig.patch.set_facecolor(BG)
for j,(cn,cm) in enumerate(cohorts):
    for i,(gn,gm) in enumerate([('women',F),('men',M)]):
        clock(axs[i,j],cm&gm&(P.dtype=='work'),f"{gn} {cn}",None)
fig.suptitle('What Salaried India Does From Noon to Midnight',fontweight='bold',fontsize=15,y=0.99)
fig.text(0.5,0.925,'Normal work day. Rim colour = most common activity in each half hour (paler = less agreement).\nThe hand points to when paid work ends for the median worker. 12 at the top is noon.',
         ha='center',va='top',fontsize=9,color='0.3')
fig.legend(handles=[Patch(color=c,label=l) for l,c in COL.items() if l not in ('care','social/relig')],frameon=False,fontsize=9,ncol=6,loc='lower center',bbox_to_anchor=(0.5,0.075))
fig.text(0.01,0.005,"Knowledge work and blue-collar work are approximated from NIC industry codes\n(knowledge work also requires a graduate degree). Public employment is the\nemployer type recorded for paid work, not an NIC code.",ha='left',va='bottom',fontsize=7,color='0.4',linespacing=1.4)
fig.text(0.99,0.005,'Source: NSO Time Use Survey 2024, salaried, weighted.',ha='right',fontsize=7,color='0.4')
fig.subplots_adjust(left=0.02,right=0.98,top=0.855,bottom=0.2,hspace=0.5,wspace=0.04)
fig.savefig(OUT+'/clock-faces.png',dpi=300,facecolor=BG,bbox_inches='tight')
