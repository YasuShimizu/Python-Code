import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from matplotlib._version import get_versions as mplv
import copy

fig=plt.figure()

xl=100; nx=201; c=0.5
xb=10;xp=xb;fp=0.5
etime=120;dt=0.1

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

im=plt.title("Upwind Scheme")
im=plt.xlabel("x")
im=plt.ylabel("f")
im=plt.xlim(0,100)
im=plt.ylim(0,1.0)


time=0
while(time<=etime):
    for i in range(1,nx-1):
        fn[i]=f[i]-c*(f[i+1]-f[i-1])*dt/(2.*dx)

    f=copy.copy(fn)
    text1=plt.text(60.,0.92,"Time="+str(np.round(time,3))+"sec",size='20')
    im=plt.plot(x,f,'r')
    ims.append(im+[text1])
    time=time+dt

ani = animation.ArtistAnimation(fig, ims, interval=1)
plt.show(); #PC画面アニメ出力
ani.save('central.gif',writer='imagemagick'); #gifファイル出力
#ani.save('backward.mp4',writer='ffmpeg'); #mp4ファイル出力