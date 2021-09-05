import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from matplotlib._version import get_versions as mplv
import copy,math,os
from mpl_toolkits.mplot3d import Axes3D
from numpy.core.arrayprint import dtype_is_implied
import subprocess

xl=100; yl=100; nx=200; ny=200; #計算領域
rb=20;fp=0.5 #初期円錐形の底面半径, ピーク
etime=500;dt=0.2 #計算終了時間, タイムステップ
ims=[]

# u,vの円運動
rt=30; theta0=0; t_cycle=100. #円運動半径, 初期位相, 周期
omega=2.*np.pi/t_cycle # 角速度
uv=rt*omega # 速度
xc=0.; yc=0. #円運動の中心点

nx1=nx+1; ny1=ny+1; nx2=nx+2; ny2=ny+2
xp=10;yp=10
xsize=10.;ysize=xsize/xl*yl

x = np.linspace(-xl/2., xl/2., nx1)
y = np.linspace(-yl/2., yl/2., ny1)
z = np.round(np.linspace(0,fp,6),2)
Y,X=np.meshgrid(x,y)
dx=xl/nx; dy=yl/ny

f=np.zeros([nx1,ny1]);fn=np.zeros([nx1,ny1])
f0=np.zeros([nx1,ny1])

# Initial f profile
theta=theta0
xp=xc+rt*np.cos(theta); yp=yc+rt*np.sin(theta)
for i in np.arange(0,nx):
    for j in np.arange(0,ny):
        r=math.sqrt((xp-x[i])**2+(yp-y[j])**2)
        if r<rb:
            f0[i,j]=(rb-r)/rb*fp
        else:
            f0[i,j]=0.
f=copy.copy(f0)
#fn=copy.copy(f)

levels=np.arange(0.,fp,fp/5.)
time=0.;icount=0;fskip=20
nfile=0
os.system("del /Q .\png\*.png")
os.system("del /Q animation*.*")

while time<=etime:
    theta=theta0+omega*time
    xp=xc+rt*np.cos(theta); yp=yc+rt*np.sin(theta)
    for i in np.arange(0,nx):
        for j in np.arange(0,ny):
            r=math.sqrt((xp-x[i])**2+(yp-y[j])**2)
            if r<rb:
                f0[i,j]=(rb-r)/rb*fp
            else:
                f0[i,j]=0.
#    while theta>2.*np.pi:
#        theta=theta-2.*np.pi
    u=-uv*np.sin(theta); v=uv*np.cos(theta)
#    print(time,theta,u,v)
#    for i in np.arange(0,nx):
#        for j in np.arange(0,ny): 
#            fn[i,j]=f[i,j]-dt/2.*(   \
#                ((u+abs(u))*(f[i,j]-f[i-1,j])+(u-abs(u))*(f[i+1,j]-f[i,j]))/dx  \
#               +((v+abs(v))*(f[i,j]-f[i,j-1])+(v-abs(v))*(f[i,j+1]-f[i,j]))/dy)
#    f=copy.copy(fn)
    if (icount % fskip) == 0:
        nfile=nfile+1
        fig = plt.figure(figsize=(25, 10), dpi=100)
        ax = fig.add_subplot(111, projection='3d')
        text1=ax.text(xl*.3,yl*.4,0.4,"Time="+str(np.round(time,3))+"sec",size='25')
        ax.set_title('Circular Movement of a Cone',size='40')
        for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(20) 
        for tick in ax.yaxis.get_major_ticks():
                tick.label.set_fontsize(20)  
        for tick in ax.zaxis.get_major_ticks():
                tick.label.set_fontsize(20)                        
        ax.set_xlabel('x',size='30',labelpad=30)
        ax.set_ylabel('y',size='30',labelpad=30)
        ax.set_zlabel('f',size='20',labelpad=20)
#        ax.set_zticklabels(z,size='20')
        ax.set_zlim(0, 0.5) 
        srf=ax.plot_surface(X,Y,f0,cmap="plasma")
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