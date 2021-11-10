# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:00:58 2021

@author: rouss
"""

import csv
import math as math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random




n = 80000
nt = 256


x = np.zeros((n,nt))
T = np.zeros((n,nt))
z = np.zeros((n,nt))

xa=0.0
ya=0.0
za=0.0
for i in range (0,40000):
    na = 22.5
    t= np.linspace(0.0,na,nt)
    
    xc=na
    yc=-2.0
 
    t[0]=0.0
    
    xb= random.uniform(-1.0,1.0)
    if (xb - xc) == 0 or (xc-xb) == 0:
        xb=xb-0.05
    
    yb= random.uniform(-3.0,3.0)
    a= ((yc-ya)/((xc-xa)*(xc-xb))) - ((yb-ya)/((xb-xa)*(xc-xb)))
    b = ((yb-ya)/(xb-xa))-a*(xb+xa)
    c= ya-(a*xa**2)-(b*xa)
    
    x[i,:] = (a*t**2 + b*t + c)
    x[i,0]=0.0
    x[i,255]= yc
    T[i,:]= t
    print(T)
    z[i,:]= ((-a*t**2 - b*t - c - t )* -0.55)
   
    z[i,0]=0.0
    z[i,255]=11.275
    #print(z[i,255])
    
    
for i in range (40000,80000):
    na = 32.5
    t= np.linspace(0.0 ,na,nt)
    t[0]=0.0
    xc=na
    yc=2.5
  
    
    xb= random.uniform(-5.0,5.0)
    if (xb - xc) == 0 or (xc-xb) == 0:
        xb=xb-0.05
    yb= random.uniform(-5.0,5.0)
    
    a= ((yc-ya)/((xc-xa)*(xc-xb))) - ((yb-ya)/((xb-xa)*(xc-xb)))
    b = ((yb-ya)/(xb-xa))-a*(xb+xa)
    c= ya-(a*xa**2)-(b*xa)
    
    x[i,:] = (a*t**2 + b*t + c)
    x[i,0]=0.0
    x[i,255]= yc
    T[i,:]= t
    z[i,:]= ((-a*t**2 - b*t - c - t)*0.23)
    z[i,0]=0.0
    z[i,255]=-8.05
    #print(z[i,255])
    
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(T[0,:],x[0,:],z[0,:],'o-')
ax.view_init(elev=20., azim=120)

fig2= plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.plot(T[550,:],x[550,:],z[550,:],'o-')       
ax2.view_init(elev=20., azim=120)

fig2= plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.plot(T[100,:],x[100,:],z[100,:],'o-')    
ax2.view_init(elev=20., azim=120)

fig2= plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.plot(T[50000,:],x[50000,:],z[50000,:],'o-')    
ax2.view_init(elev=20., azim=120)

plt.figure()
plt.plot(T[50000,:],x[50000,:])
plt.legend()
plt.show()

plt.figure()
plt.plot(T[5000,:],x[5000,:])
plt.legend()
plt.show()

data = x
datay= T
dataz= z

file = open('data_traj_cvae_2obj80000_x_3d_finaltest.csv', 'w+', newline ='')
with file: 
    write = csv.writer(file)
    write.writerows(data)

filey = open('data_traj_cvae_2obj80000_t_3d_finaltest.csv', 'w+', newline ='')
with filey: 
    writey = csv.writer(filey)
    writey.writerows(datay)
    
filez = open('data_traj_cvae_2obj80000_z_3d_finaltest.csv', 'w+', newline ='')
with filez: 
    writez = csv.writer(filez)
    writez.writerows(dataz)
print("termine")
