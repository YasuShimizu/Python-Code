import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from matplotlib._version import get_versions as mplv
import copy,math,os
from mpl_toolkits.mplot3d import Axes3D
from numpy.core.arrayprint import dtype_is_implied
import subprocess

xl=100; yl=100; nx=100; ny=100; u=0.5; v=0.5
nx1=nx+1; ny1=ny+1; nx2=nx+2; ny2=ny+2
xp=10;yp=10;rb=10;fp=0.5
xsize=10.;ysize=xsize/xl*yl
etime=120;dt=0.5
ims=[]


x = np.linspace(0, xl, nx1)
y = np.linspace(0, yl, ny1)
z = np.round(np.linspace(0,fp,11),2)
X,Y=np.meshgrid(x,y)
dx=xl/nx; dy=yl/ny

f=np.zeros([nx1,ny1]);fn=np.zeros([nx1,ny1])

# Initial f profile
for i in np.arange(0,nx):
    for j in np.arange(0,ny):
        r=math.sqrt((xp-x[i])**2+(yp-y[j])**2)
        if r<rb:
            f[i,j]=(rb-r)/rb*fp
        else:
            f[i,j]=0.

fn=copy.copy(f)

levels=np.arange(0.,fp,fp/5.)
time=0.;icount=0;fskip=5
nfile=0
os.system("del /Q .\png\*.png")
os.system("del /Q animation*.*")

while time<=etime:
    for i in np.arange(0,nx):
        for j in np.arange(0,ny): 
            fn[i,j]=f[i,j]-(u*(f[i,j]-f[i-1,j])/dx+v*(f[i,j]-f[i,j-1])/dy)*dt
    f=copy.copy(fn)
    if (icount % fskip) == 0:
        nfile=nfile+1
        fig = plt.figure(figsize=(25, 10), dpi=100)
        ax = fig.add_subplot(111, projection='3d')
        text1=ax.text(xl*.6,yl*.9,0.25,"Time="+str(np.round(time,3))+"sec",size='25')
        ax.set_title('2D Backward 3D-Plot',size='32')
        ax.set_xlabel('x',size='20')
        ax.set_ylabel('y',size='20')
        ax.set_xticklabels(x,size='20')
        ax.set_yticklabels(y,size='20')
        ax.set_zlabel('f',size='20')
        ax.set_zticklabels(z,size='20')
        ax.set_zlim(0, 0.3) 
        srf=ax.plot_surface(X,Y,f,cmap="plasma")
#        fig.colorbar(srf)
        fname="./png/" + 'f%04d' % nfile + '.png'
        print(fname)
        im=plt.savefig(fname)
        plt.clf()
        plt.close()

#  
    time=time+dt
    icount=icount+1

subprocess.call('ffmpeg -framerate 30 -i png/f%4d.png -r 60 -an -vcodec libx264 -pix_fmt yuv420p animation.mp4', shell=True)
os.system("ffmpeg -i animation.mp4 animation.gif -loop 0")