import numpy as np
#from matplotlib import rc
import matplotlib.pyplot as plt
import pandas as pd

def XYZ2lbr(X,Y,Z):
    r = sqrt(X**2+Y**2+Z**2)
    l = arctan2(Y,X)
    b = pi/2 - arccos(Z/r)
    return l,b,r

def lbr2XYZ(l,b,r):
    X = r*cos(b)*sin(l)
    Y = r*cos(b)*cos(l)
    Z = r*sin(b)
    return X,Y,Z

def xyz2XYZ(x,y,z):
    R0 = -8.0
    return x,-y-R0,z

def XYZ2xyz(X,Y,Z):
    R0 = +8.0
    return X,Y-R0,Z

def xyz2lbr(x,y,z):
    X,Y,Z = xyz2XYZ(x,y,z)
    l,b,r = XYZ2lbr(X,Y,Z)
    return l,b,r

def lbr2xyz(l,b,r):
    X,Y,Z = lbr2XYZ(l,b,r)
    x,y,z = XYZ2xyz(X,Y,Z)
    return x,y,z


data = pd.read_csv('gaia_fundamental_matched2mass.csv')




width = 3.25
golden_ratio = (1.+np.sqrt(5))/2.
height = width/golden_ratio
fig = plt.figure(figsize=(2*width, 2*height), num=1)
cm = plt.cm.get_cmap('RdYlBu_r')

sct=plt.scatter(data['x'],-data['y'], s=35, c=np.log(data['pf']), alpha=.5,cmap=cm)
plt.colorbar(sct,label='Log P ~ Age')
plt.quiver(data['x'],-data['y'],data['pmra'],data['pmdec'], np.log(data['pf']), alpha=.5)
plt.quiver(data['x'],-data['y'],data['pmra'],data['pmdec'], edgecolor='k', facecolor='None', linewidth=.3)

ax = fig.add_subplot(111)
plt.xlim(-40,40)
plt.ylim(-40,40)
plt.plot([-40,40], [0,0],  '-', color='k')
plt.plot([-40,40], [-8,-8],  ':', color='k')
plt.plot([0,0], [-40,40],  '-', color='k')
ax.set_xlabel('x [kpc]')
ax.set_ylabel('y [kpc]')
# savefig('../figures/scatter_ex.png',dpi=48)
#from gammapy.astro.population import ValleeSpiral
#radius=np.arange(0,60,1)
#angles=np.arange(0,60,1)
#vs=ValleeSpiral()
#x,y=vs.xy_position(angles*360/60,radius+3,0)
#plt.plot(x,y-8,  '-', color='r')
#x,y=vs.xy_position(angles*360/60,radius+3,3)
#plt.plot(x,y-8,  '-', color='y')
angle=np.arange(0,3*360,1)


pitch=12.8#; Norma
r0=2.58
x_spi=np.exp(np.tan(pitch*2.*np.pi/360)*(angle*2.*np.pi/360))*r0*np.cos(angle*2.*np.pi/360.)
y_spi=np.exp(np.tan(pitch*2.*np.pi/360)*(angle*2.*np.pi/360))*r0*np.sin(angle*2.*np.pi/360.)-8.0
r2=2.58#; Scutum
x_spi2=np.exp(np.tan(pitch*2.*np.pi/360)*((angle-90)*2.*np.pi/360))*r2*np.cos(angle*2.*np.pi/360.)
y_spi2=np.exp(np.tan(pitch*2.*np.pi/360)*((angle-90)*2.*np.pi/360))*r2*np.sin(angle*2.*np.pi/360.)-8.0
r3=2.58#; sagitt
x_spi3=np.exp(np.tan(pitch*2.*np.pi/360)*((angle-180)*2.*np.pi/360))*r3*np.cos(angle*2.*np.pi/360.)
y_spi3=np.exp(np.tan(pitch*2.*np.pi/360)*((angle-180)*2.*np.pi/360))*r3*np.sin(angle*2.*np.pi/360.)-8.0
r4=2.58#; pers
x_spi4=np.exp(np.tan(pitch*2.*np.pi/360)*((angle-270)*2.*np.pi/360))*r4*np.cos(angle*2.*np.pi/360.)
y_spi4=np.exp(np.tan(pitch*2.*np.pi/360)*((angle-270)*2.*np.pi/360))*r4*np.cos(angle*2.*np.pi/360.)-8.0
plt.plot(x_spi,y_spi,  '--', color='m')
plt.plot(x_spi2,y_spi2,  '--', color='c')
plt.plot(x_spi3,y_spi3,  '--', color='b')
#plt.plot(x_spi4,y_spi4,  '-', color='m')

plt.show()