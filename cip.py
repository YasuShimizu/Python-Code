# coding: shift_jis

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from matplotlib._version import get_versions as mplv

fig=plt.figure()

xl=100; nx=201; c=0.5
xb=5;xp=5;fp=0.5
etime=50;dt=0.2

x=np.linspace(0,xl,nx)
dx=x[2]-x[1]
f=[0]*nx; fn=[0]*nx
fd=[0]*nx; fdn=[0]*nx
ims=[]

for i in range(0,nx):
    if(x[i]>=(xp-xb) and x[i]<=xp):
        f[i]=fp/xb*(x[i]-xp+xb)
    elif(x[i]>xp and x[i]<(xp+xb)):
        f[i]=fp/xb*(xp+xb-x[i])
    else:
        f[i]=0

im=plt.title("CIP Scheme")
im=plt.xlabel("x")
im=plt.ylabel("f")

for i in range(2,nx-1):
    fd[i]=(f[i+1]-f[i-1])/(2*dx)

time=0
while(time<=etime):
    for i in range(2,nx-1):
       a=-2*(f[i]-f[i-1])/dx**3+(fd[i]+fd[i-1])/dx**2
       b=3*(f[i]-f[i-1])/dx**2-(fd[i]+2*fd[i-1])/dx
       xi=dx-c*dt
       fn[i]=a*xi**3+b*xi**2+fd[i-1]*xi+f[i-1]
       fdn[i]=3*a*xi**2+2*b*xi+fd[i-1]

    f=fn
    fd=fdn
    time=time+dt
    im=plt.plot(x,f,'blue');
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=10)
plt.show()
#ani.save('cip.gif',writer='imagemagick')
#ani.save('cip.mp4',writer='ffmpeg')


        



