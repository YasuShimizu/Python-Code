import numpy as np
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import copy

f = open('res.txt', 'w')

t0=110. # 最大偏角
l=1.0; nx0=51; wn=3 # 波長, 格子数/1波長, 波数

ds=l/(nx0-1); dds=ds/10.
#print(ds,dds)
#exit()
s0=0.; x0=0.; y0=-0.2
nx=(nx0-1)*wn+1
xpos=np.zeros([nx+1]); ypos=np.zeros([nx+1]); spos=np.zeros([nx+1])
radius=np.zeros([nx+1]);radius_s=np.zeros([nx+1]);tpos=np.zeros([nx+1])
dx=np.zeros([nx+1]);dy=np.zeros([nx+1]);ds=np.zeros([nx+1])
coss=np.zeros([nx+1]);sins=np.zeros([nx+1])

fig,ax=plt.subplots(figsize = (20, 10))

ax.set_title("Distribution of Curvature in a Sin-Generated Curve",size='25')
ax.set_xlabel("s(m)",size='20')
ax.set_ylabel("1/r (1/m)",size='20')

theta0=np.radians(t0)
s=s0; x=x0; y=y0
xpos[0]=x; ypos[0]=y; spos[0]=s0; tpos[0]=0
radius[0]=2.*np.pi/l*theta0*np.cos(2.*np.pi*s/l)
coss[0]=np.cos(0); sins[0]=np.sin(0)
for i in np.arange(1,nx+1):
    for j in np.arange(1,11):
        s=s+dds
        theta=theta0*np.sin(2.*np.pi*s/l)
        x=x+dds*np.cos(theta)
        y=y+dds*np.sin(theta)
    xpos[i]=x; ypos[i]=y; spos[i]=s; tpos[i]=np.rad2deg(theta)
    radius[i]=2.*np.pi/l*theta0*np.cos(2.*np.pi*s/l)

for i in np.arange(1,nx+1):
    dx[i]=xpos[i]-xpos[i-1]; dy[i]=ypos[i]-ypos[i-1]
    ds[i]=np.sqrt(dx[i]**2+dy[i]**2)
    coss[i]=dx[i]/ds[i]
    sins[i]=dy[i]/ds[i]

ds[0]=ds[1]; coss[0]=coss[1]; sins[0]=sins[1]

for i in np.arange(1,nx):

#    radius_s[i]=(coss[i]*(sins[i]-sins[i-1])-sins[i]*(coss[i]-coss[i-1]))/ds[i]
    radius_s[i]=(coss[i]*(sins[i+1]-sins[i])-sins[i]*(coss[i+1]-coss[i]))/ds[i]

radius_s[0]=radius_s[1];radius_s[nx]=radius[nx-1]

#ax.plot(spos,radius,label='theta0='+str(t0)+' degree',linewidth=4)

#for i in np.arange(0,nx):
#    str1=str('{:10.3f}'.format(spos[i]))
#    x_s=str('{:8.4f}'.format(xpos[i]))
#    y_s=str('{:8.4f}'.format(ypos[i]))
#    t_s=str('{:8.3f}'.format(tpos[i]))
#    rs_s=str('{:10.5f}'.format(radius_s[i]))
#    rs=str('{:10.5f}'.format(radius[i]))
#    dx_s=str('{:8.4f}'.format(dx[i]))
#    dy_s=str('{:8.4f}'.format(dy[i]))
#    ds_s=str('{:8.4f}'.format(ds[i]))
#    cos_s=str('{:8.4f}'.format(coss[i]))
#    sin_s=str('{:8.4f}'.format(sins[i]))
#    f.write(str1+dx_s+dy_s+ds_s+t_s+cos_s+sin_s+rs+rs_s+'\n')

#ax.plot(spos,tpos,label='theta',linewidth=4)
#ax.plot(spos,dx,label='dx',linewidth=4)
#ax.plot(spos,dy,label='dy',linewidth=4)
#ax.plot(spos,coss,label='cos',linewidth=4)
#ax.plot(spos,sins,label='sin',linewidth=4)
ax.plot(spos,radius,label='equation theta0='+str(t0)+' deg.',linewidth=4)
ax.plot(spos,radius_s,label='discrete calculation',linewidth=4)

ax.legend(fontsize=20)

plt.show()
fig.savefig("img.png")
