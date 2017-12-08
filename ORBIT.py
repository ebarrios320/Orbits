#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 01:54:02 2017

@author: estebanbarrios
"""
from pylab import * 
from matplotlib.animation import *

def circle(x0,y0,R,N) :
    ''' create circle, given center x0,y0, input radius R,
        and number of points N, then 
        output arrays of x and y coordinates '''
        
    theta = linspace(0.0,2.0*pi,N)
    x = R * cos(theta) + x0
    y = R * sin(theta) + y0
    return x,y



a= array([.39,.72,1,1.52,5.20,9.54,19.2,30.1]) #astronomical units of the planets in order of the planet 
period = a**(3.0/2.0) 

#distance of the planets 
d= array([390,790,980, 1520,5200,9540,19200,30100])
#attributes of the sun
x0 =0 
y0 = 0
r_s=70*1.2#actual earth radius is 695e6 

#radius of the planets 
r_Ear = 63.781#e in m {for all the planets}
r_Merc= 24
r_Ven = 60 
r_Mars= 33.9
r_Jup = 700
r_Sat = 582 
r_Ura = 253
r_Nep = 246

#Distance of the planets
d_Ear = 1000#152
d_Merc= 390#70
d_Ven = 790#109
d_Mars= 1520#249
d_Jup = 5200#816
d_Sat = 9540#1514
d_Ura = 19200#3003
d_Nep = 30100#4545

fig = plt.figure()
ax = plt.axes(xlim=(-1e4-1000, 1e4+1000), ylim=(-1e4-1000, 1e4+1000), aspect=True)

for i in range(8) :
    x, y = circle(0.0,0.0,d[i],10000) # orbit
    plot(x,y,':k')



Sun = plt.Circle((x0, y0), radius=r_s, ec='yellow', fc='yellow', lw=3)
Mercury = plt.Circle((0, 0), radius=r_Merc, ec='gray', fc='gray', lw=3)
Venus = plt.Circle((0, 0), radius=r_Ven, ec='red', fc='black', lw=3)
Earth = plt.Circle((0, 0), radius=r_Ear, ec='green', fc='green', lw=3)
Mars = plt.Circle((0, 0), radius=r_Mars, ec='red', fc='red', lw=3)
Jupiter = plt.Circle((0, 0), radius=r_Jup, ec='orange', fc='orange', lw=3)
Saturn = plt.Circle((0, 0), radius=r_Sat, ec='gray', fc='yellow', lw=3)
Uranus = plt.Circle((0, 0), radius=r_Ura, ec='green', fc='green', lw=3)
Neptune = plt.Circle((0, 0), radius=r_Nep, ec='green', fc='green', lw=3)

ax.add_patch(Sun)

def init():
    
    ax.add_patch(Earth)
    ax.add_patch(Mercury)
    ax.add_patch(Venus) 
    ax.add_patch(Mars) 
    ax.add_patch(Jupiter)
    ax.add_patch(Saturn)
    ax.add_patch(Uranus)
    ax.add_patch(Neptune)
    
    return Mercury, Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune,
def animate(i):
    

    theta = radians(i)
    mx = d_Merc*np.cos(theta/period[0]) 
    my = d_Merc*np.sin(theta/period[0]) 
    
    vx = d_Ven *np.cos(theta/period[1]) 
    vy = d_Ven *np.sin(theta/period[1]) 
    
    ex = d_Ear*np.cos(theta/period[2]) 
    ey = d_Ear*np.sin(theta/period[2]) 
    
    Mx = d_Mars*np.cos(theta/period[3]) 
    My = d_Mars*np.sin(theta/period[3])
   
    Jx = d_Jup*np.cos(theta/period[4]) 
    Jy = d_Jup*np.sin(theta/period[4]) 
    
    Sx = d_Sat*np.cos(theta/period[5]) 
    Sy = d_Sat*np.sin(theta/period[5]) 
    
    Ux = d_Ura*np.cos(theta/period[6]) 
    Uy = d_Ura*np.sin(theta/period[6]) 
    
    Nx = d_Nep*np.cos(theta/period[7]) 
    Ny = d_Nep*np.sin(theta/period[7]) 
    
    Mercury.center = (mx, my)
    Venus.center = (vx, vy)
    Earth.center = (ex, ey)
    Mars.center  = (Mx, My)
    Jupiter.center = (Jx, Jy)
    Saturn.center = (Sx, Sy)
    Uranus.center = (Ux, Uy)
    Neptune.center = (Nx, Ny)
  
    return  Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune,

anim = FuncAnimation(fig, animate, init_func=init, frames=1080, 
                               interval=25, blit=True)

plt.show()
