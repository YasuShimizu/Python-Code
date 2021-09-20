# coding: shift_jis

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from matplotlib._version import get_versions as mplv
import copy

#fig=plt.figure()
fig, ax = plt.subplots()

xl=100; nx=201; u=0.5
xb=10;xp=xb;fp=0.5
etime=180;dt=0.1

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

im=ax.set_title("CIP Scheme",size='25')
im=ax.set_xlabel("x",size='20')
im=ax.set_ylabel("f",size='20')
im=ax.set_ylim(0,0.6)

for i in range(2,nx-1):
    fd[i]=(f[i+1]-f[i-1])/(2*dx)

time=0
icount=0; fskip=10
while(time<=etime):
    for i in range(2,nx-1):
       a=(fd[i]+fd[i-1])/dx**2+2*(f[i]-f[i-1])/dx**3
       b=3*(f[i-1]-f[i])/dx**2-(fd[i-1]+2*fd[i])/dx
       xi=u*dt
       fn[i]=a*xi**3+b*xi**2+fd[i]*xi+f[i]
       fdn[i]=3*a*xi**2+2*b*xi+fd[i]

    f=copy.copy(fn)
    fd=copy.copy(fdn)
    icount=icount+1
    if (icount % fskip) == 0:
        text=ax.text(55.,0.55,"Time="+str(np.round(time,3))+"sec",size='20')
        im=ax.plot(x,f,'r')
        ims.append(im+[text])

    time=time+dt

ani = animation.ArtistAnimation(fig, ims, interval=10)
plt.show()
ani.save('cip.gif',writer='imagemagick')
ani.save('cip.mp4',writer='ffmpeg')


        



