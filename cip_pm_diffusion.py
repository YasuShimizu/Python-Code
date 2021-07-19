# coding: shift_jis

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from matplotlib._version import get_versions as mplv

fig=plt.figure()

xl=100; nx=201; u0=0.4
xb=30;xp=50;fp=0.5
etime=300;dt=0.2
tl=50
d=0.5

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
    u=u0*np.sin(2.*np.pi/tl*time)
#    u=u0
# Diffusion 
    for i in np.arange(2,nx-1):
        fn[i]=f[i]+d*(f[i+1]-2.*f[i]+f[i-1])*dt/dx**2

    for i in np.arange(2,nx-1):
        fdn[i]=fd[i]+(fn[i+1]-fn[i-1]-f[i+1]+f[i-1])*0.5/dx

    fd=fdn.copy()

# Advection
    for i in np.arange(2,nx-1):
       i1=int(np.sign(u))
       if i1==0:
           i1=1
       ix=i-i1 
       a=((fd[ix]+fd[i])*dx*i1-2*(fn[i]-fn[ix]))/(dx**3*i1)
       b=(3*(fn[ix]-fn[i])+(fd[ix]+2*fd[i])*dx*i1)/dx**2
       xi=-u*dt
       f[i]=((a*xi+b)*xi+fd[i])*xi+fn[i]
       fdn[i]=3*a*xi**2+2*b*xi+fd[i]

    for i in np.arange(2,nx-1):
        fdo=(f[i+1]-f[i-1])*.5/dx
        fd[i]=fdn[i]-(fdo*(f[i+1]-f[i-1]))

    time=time+dt
    im=plt.plot(x,f,'blue')
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=10)
plt.show()
#ani.save('cip_pm_dif.gif',writer='imagemagick')
#ani.save('cip_pm_dif.mp4',writer='ffmpeg')


        



