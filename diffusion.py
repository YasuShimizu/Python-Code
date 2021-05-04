# coding: shift_jis

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from matplotlib._version import get_versions as mplv
from scipy.stats import gaussian_kde

fig=plt.figure()

xl=100; nx=201; d=0.01
xb=5;xp=50;fp=0.5
etime=1000;dt=5

x=np.linspace(0,xl,nx)
dx=x[2]-x[1]
f=[0]*nx; fn=[0]*nx
ims=[]

for i in range(0,nx):
    if(x[i]>=(xp-xb) and x[i]<=xp):
        f[i]=fp/xb*(x[i]-xp+xb)
    elif(x[i]>xp and x[i]<(xp+xb)):
        f[i]=fp/xb*(xp+xb-x[i])
    else:
        f[i]=0

im=plt.title("Diffusion")
im=plt.xlabel("x")
im=plt.ylabel("f")

time=0
while(time<=etime):
    for i in range(1,nx-1):
        fn[i]=f[i]+d*(f[i+1]-2*f[i]+f[i-1])*dt/dx**2

    f=fn
    time=time+dt
    im=plt.plot(x,f,'r');
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=10)
#plt.show()
ani.save('diffusion.gif',writer='imagemagick')
ani.save('diffusion.mp4',writer='ffmpeg')
