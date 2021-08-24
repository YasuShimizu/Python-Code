import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from matplotlib._version import get_versions as mplv
import copy
#from scipy.stats import gaussian_kde

fig=plt.figure()

xl=100; nx=201; c=0.5
xb=10;xp=xb;fp=0.5
etime=180;dt=0.05

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

im=plt.title("5th Order Scheme",size='25')
im=plt.xlabel("x",size='20')
im=plt.ylabel("f",size='20')
im=plt.ylim(0,0.6)

time=0
icount=0; fskip=10
while(time<=etime):
    for i in range(2,nx-3):
#        fn[i]=f[i]-c*(f[i]-f[i-1])*dt/dx
#        fn[i]=f[i]-c*(f[i+1]-f[i-1])/(2.*dx)*dt \
#            -abs(c)*(-f[i+1]+2.*f[i]-f[i-1])/(2.*dx)*dt # 1st order upwind

# 5th Order Scheme 
        fn[i]=f[i]-c*(f[i+3]-9.*f[i+2]+45.*(f[i+1]-f[i-1])+9.*f[i-2]-f[i-3])/(60.*dx)*dt \
            -abs(c)*(-f[i+3]+6.*f[i+2]-15.*f[i+1]+20.*f[i]-15.*f[i-1]+6.*f[i-2]-f[i-3])/(60.*dx)*dt 



    f=copy.copy(fn)
    icount=icount+1

    if (icount % fskip) == 0:
        text1=plt.text(60.,0.9,"Time="+str(np.round(time,3))+"sec",size='20')
        im=plt.plot(x,f,'r')
        ims.append(im+[text1])
    time=time+dt

ani = animation.ArtistAnimation(fig, ims, interval=10)
#plt.show(); #PC画面アニメ出力
ani.save('5th.gif',writer='imagemagick'); #gifファイル出力
#ani.save('upwind.mp4',writer='ffmpeg'); #mp4ファイル出力