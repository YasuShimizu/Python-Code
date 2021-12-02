import numpy as np
import matplotlib.pyplot as plt
import copy
from matplotlib import rc

#rc('font', **{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)

tbox=[100] # プロットする最大編角


l=2.8; nx0=41; wn=3; ny=10 # 波長, 格子数/1波長, 波数, 横断方向格子数
js=1./32.; jf=1./192.

b=0.2 # 河幅
xsize=20. # plotのサイズ

ds=l/(nx0-1); dds=ds/10.
#print(ds,dds)
#exit()
s0=0.; x0=0.; y0=-0.2
nx=(nx0-1)*wn+1
xpos=np.zeros([nx+1]); ypos=np.zeros([nx+1]); thepos=np.zeros([nx+1])
xr=np.zeros([nx+1]); xl=np.zeros([nx+1]); yr=np.zeros([nx+1]); yl=np.zeros([nx+1])
xgrid=np.zeros([nx+1,ny+1]); ygrid=np.zeros([nx+1,ny+1])
xmin=-0.2; xmax=3.5
ymin=-0.4; ymax=1.3

ylen=ymax-ymin; xlen=xmax-xmin
ysize=xsize/xlen*ylen

fig,ax=plt.subplots(figsize = (xsize, ysize))

im=ax.set_title("Kinoshita Meandering Curve",size='25')
im=ax.set_xlabel("x(m)",size='20')
im=ax.set_ylabel("y(m)",size='20')
im=ax.set_ylim(ymin,ymax)
im=ax.set_xlim(xmin,xmax)


for t0 in tbox:
    theta0=np.radians(t0)
    s=s0; x=x0; y=y0
    xpos[0]=x; ypos[0]=y
    thepos[0]=theta0*np.sin(2.*np.pi*s/l)+theta0**3*(js*np.cos(6.*np.pi*s/l)-jf*np.sin(6.*np.pi*s/l))
    for i in np.arange(1,nx+1):
        for j in np.arange(1,11):
            s=s+dds
            theta=theta0*np.sin(2.*np.pi*s/l)+theta0**3*(js*np.cos(6.*np.pi*s/l)-jf*np.sin(6.*np.pi*s/l))
            x=x+dds*np.cos(theta)
            y=y+dds*np.sin(theta)
        xpos[i]=x; ypos[i]=y; thepos[i]=theta

    for i in np.arange(0,nx+1):
        xr[i]=xpos[i]+b/2.*np.sin(thepos[i])
        yr[i]=ypos[i]-b/2.*np.cos(thepos[i])
        xl[i]=xpos[i]-b/2.*np.sin(thepos[i])
        yl[i]=ypos[i]+b/2.*np.cos(thepos[i])


        for j in np.arange(0,ny+1):
            ss=float(j)/float(ny)
            xgrid[i,j]=xr[i]+ss*(xl[i]-xr[i])
            ygrid[i,j]=yr[i]+ss*(yl[i]-yr[i])
            

    for i in np.arange(0,nx):
        xline=np.zeros([ny+1])
        yline=np.zeros([ny+1])
        for j in np.arange(0,ny+1):
            xline[j]=xgrid[i,j]
            yline[j]=ygrid[i,j]
        im=ax.plot(xline,yline,color='black')

    for j in np.arange(0,ny+1):
        xline=np.zeros([nx])
        yline=np.zeros([nx])
        for i in np.arange(0,nx):
            xline[i]=xgrid[i,j]
            yline[i]=ygrid[i,j]
        im=ax.plot(xline,yline,color='black')

text1=ax.text(xmin+xlen*.4,ymin+ylen*.95,\
    "$\\theta_0$="+str(t0)+"$^\\bigcirc$ L="+str(l)+"m "+\
        "B="+str(b)+"m",size=20)

plt.show()
fig.savefig("img.png")
