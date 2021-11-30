import numpy as np
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import copy

tbox=[30,60,90,120] # プロットする最大編角群


l=1.0; nx0=51; wn=3 # 波長, 格子数/1波長, 波数
xsize=20. # plotのサイズ

ds=l/(nx0-1); dds=ds/10.
#print(ds,dds)
#exit()
s0=0.; x0=0.; y0=-0.2
nx=(nx0-1)*wn+1
xpos=np.zeros([nx+1]); ypos=np.zeros([nx+1])
xmin=0.; xmax=l*wn
ymin=-0.3; ymax=0.4

yl=ymax-ymin; xl=xmax-xmin
ysize=xsize/xl*yl

fig,ax=plt.subplots(figsize = (xsize, ysize))

im=ax.set_title("Sin-Generated Curve",size='25')
im=ax.set_xlabel("x(m)",size='20')
im=ax.set_ylabel("y(m)",size='20')
im=ax.set_ylim(ymin,ymax)
im=ax.set_xlim(xmin,xmax)

for t0 in tbox:
    theta0=np.radians(t0)
    s=s0; x=x0; y=y0
    xpos[0]=x; ypos[0]=y
    for i in np.arange(1,nx+1):
        for j in np.arange(1,11):
            s=s+dds
            theta=theta0*np.sin(2.*np.pi*s/l)
            x=x+dds*np.cos(theta)
            y=y+dds*np.sin(theta)
        xpos[i]=x; ypos[i]=y
#       print(i,s,xpos[i],ypos[i])
    im=ax.plot(xpos,ypos,label='theta0='+str(t0)+' degree',linewidth=4)
    lg=ax.legend(fontsize=20)

plt.show()
fig.savefig("img.png")
