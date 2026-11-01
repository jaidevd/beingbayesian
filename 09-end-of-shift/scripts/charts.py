import sys, pickle, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm, numpy as np
D=sys.argv[1]; OUT=sys.argv[2]
for f in ['Bold','Regular']: fm.fontManager.addfont(f"/home/jaidevd/.local/share/fonts/Lora-{f}.ttf")
plt.rcParams['font.family']='Lora'
R=pickle.load(open(D+'/boot.pkl','rb'))
BG='papayawhip'
def style(ax):
    ax.set_facecolor(BG); ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y',color='gray',linewidth=0.3,linestyle='dashed')
def lab(s): h=(s*30+240)//60%24; m=(s*30+240)%60; return f'{h}:{m:02d}'
# 1. still at work
fig,ax=plt.subplots(figsize=(12,5)); fig.patch.set_facecolor(BG); style(ax)
cols={'all salaried':'0.5','KW core':'maroon','KW broad':'darkorange','blue-collar':'teal'}
xs=list(range(22,40))
for cn,c in cols.items():
    y=np.array([R['slots'][(cn,s)] for s in xs])
    ax.plot(xs,y[:,0],color=c,lw=2.5,label=cn); ax.fill_between(xs,y[:,1],y[:,2],color=c,alpha=0.18,lw=0)
ax.axvline(26,color='black',lw=1,ls=':'); ax.text(26.1,88,'5 pm',fontweight='bold')
ax.set_xticks(xs[::2]); ax.set_xticklabels([lab(s) for s in xs[::2]]); ax.set_ylim(0,100)
ax.set_ylabel('% in paid work',fontweight='bold'); ax.legend(frameon=False)
ax.set_title('Who is still working? Salaried Indians on a normal working day',fontweight='bold',loc='left')
fig.text(0.01,0.01,'Source: NSO Time Use Survey 2024, weighted. Bands: 95% cluster bootstrap by FSU.',fontsize=8,color='0.4')
fig.savefig(OUT+'/still-working.png',dpi=300,facecolor=BG,bbox_inches='tight')
# 2/3 stacked bars women vs men
G_=['paid work','commute','domestic','care','leisure/media','social/relig','eat/selfcare']
GC=['teal','0.6','maroon','#C62828','darkorange','seagreen','darkgoldenrod']
def stack(key,title,fname,note):
    cs=['all salaried','KW core','KW broad','blue-collar']
    fig,axs=plt.subplots(1,2,figsize=(12,5),sharey=True); fig.patch.set_facecolor(BG)
    for ax,gn,gt in zip(axs,'FM',['Women','Men']):
        style(ax); ax.grid(axis='x',color='gray',linewidth=0.3,linestyle='dashed'); ax.grid(axis='y',visible=False)
        for j,cn in enumerate(cs[::-1]):
            left=0
            for g_,c in zip(G_,GC):
                v=R[key][(cn,gn,g_)][0]/60
                ax.barh(j,v,left=left,color=c,height=0.6,label=g_ if j==0 and gn=='F' else None)
                if v>0.35: ax.text(left+v/2,j,f'{v:.1f}',ha='center',va='center',fontsize=8,color='white',fontweight='bold')
                left+=v
        ax.set_yticks(range(4)); ax.set_yticklabels(cs[::-1],fontweight='bold'); ax.set_title(gt,fontweight='bold'); ax.set_xlabel('hours')
    h,l=axs[0].get_legend_handles_labels(); fig.legend(h,l,frameon=False,fontsize=9,ncol=7,loc='lower center',bbox_to_anchor=(0.5,-0.04))
    fig.suptitle(title,fontweight='bold',x=0.01,ha='left'); fig.text(0.01,-0.09,note,fontsize=8,color='0.4')
    fig.savefig(OUT+'/'+fname,dpi=300,facecolor=BG,bbox_inches='tight')
stack('eve','After 5 pm on a working day: the second shift (17:00 to midnight)','evening.png','Source: NSO TUS 2024, major activities, weighted. Sleep and other time not shown.')
stack('off','On an off day (weekly off, leave, festival), all waking activities','off-day.png','Source: NSO TUS 2024, major activities, weighted. Sleep and other time not shown; off-day cells for KW core women are small (n=230).')
