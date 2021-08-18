import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from matplotlib._version import get_versions as mplv
import copy
#from scipy.stats import gaussian_kde

fig=plt.figure()

xl=100; nx=201; d=0.5
xb=10;xp=xl/2;fp=0.5
etime=150;dt=0.1

x=np.linspace(0,xl,nx)
dx=x[ 2]-x[ 1]
f=[0]*nx; fn=[0]*nx
ims=[]

for i in range(0,nx):
    if(x[i]>=(xp-xb) and x[i]<=xp): 
        f[i]=fp/xb*(x[i]-xp+xb) 
    elif(x[i]>xp and x[i]<(xp+xb)):
        f[i]=fp/xb*(xp+xb-x[i])
    else:
        f[i]=0

im=plt.title("Diffusion",size='25')
im=plt.xlabel("x")
im=plt.ylabel("f")
im=plt.ylim(0,1.0)

time=0
icount=0; fskip=10
while(time<=etime):
    if (icount % fskip) == 0:
        text1=plt.text(60.,0.9,"Time="+str(np.round(time,3))+"sec",size='20')
        im=plt.plot(x,f,'r')
        ims.append(im+[text1])

    for i in range(1,nx-1):
        fn[i]=f[i]+d*(f[i+1]-2.*f[i]+f[i-1])*dt/dx**2

    f=copy.copy(fn)
    time=time+dt
    icount=icount+1

ani = animation.ArtistAnimation(fig, ims, interval=10)
#plt.show(); #PC画面アニメ出力
ani.save('diffusion.gif',writer='imagemagick'); #gifファイル出力
#ani.save('backward.mp4',writer='ffmpeg'); #mp4ファイル出力