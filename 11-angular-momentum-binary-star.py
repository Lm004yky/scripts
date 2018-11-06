GlowScript 2.7 VPython

# Written by Bruce Sherwood, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Angular momentum of a binary star
scene.background = color.white
scene.y = 0
scene.width = 600
scene.height = 600
G = 6.7e-11
d = 1.5e11
star1 = sphere(pos=vector(d,0,0), radius=5e9, color=color.magenta, make_trail=True, retain=200, interval=10)
star1.mass = 1e30
star2 = sphere(pos=vector(0,0,0), radius=1e10, color=color.blue, make_trail=True, retain=200, interval=10)
star2.mass = 2*star1.mass

# make elliptical orbit in xz plane
ev = (2*pi*d/(365*24*60*60)) 
star1.p = vector(0, star1.mass*ev, 0)
star2.p = -star1.p
dt = 12*60*60

scene.center = vector(-0.2*d,0.3*d,0)
scene.range = 1.8*d # set size of window in meters
scene.forward = vector(0,1,-1) # tip camera angle
scene.lights = []
distant_light(direction=vector(0,-1,0.2))

# A in the xz plane
locationA = vector(-0.4*d, 0, 0) 

Lscale = 3.7e-35
pscale = 4e-24
offset = 2*star1.radius
h = star1.radius
Larr1 = arrow(pos=locationA-vector(offset,0,0), shaftwidth=star1.radius, axis=vector(0,0,0), color=star1.color)
rarr1 = arrow(pos=locationA, shaftwidth=star1.radius, axis=vector(0,0,0), color=color.cyan)
parr1 = arrow(pos=star1.pos, shaftwidth=star1.radius, axis=vector(0,0,0), color=color.red)
Larr2 = arrow(pos=locationA+vector(offset,0,0), shaftwidth=star1.radius, axis=vector(0,0,0), color=star2.color)
rarr2 = arrow(pos=locationA, shaftwidth=star1.radius, axis=vector(0,0,0), color=color.cyan)
parr2 = arrow(pos=star2.pos, shaftwidth=star1.radius, axis=vector(0,0,0), color=color.red)
Larr = arrow(pos=locationA, shaftwidth=star1.radius, axis=vector(0,0,0), color=vector(.7,.5,0))
Llabel1 = label(pos=locationA, text='L1', box=0, opacity=0, color=color.black)
Llabel2 = label(pos=locationA, text='L2', box=0, opacity=0, color=color.black)
Llabel = label(pos=locationA, text='L1+L2', box=0, opacity=0, color=color.black)

while True:
    rate(200)
    r = star2.pos-star1.pos
    F = -(G*star2.mass*star1.mass/mag(r)**2)*norm(r)
    star2.p = star2.p + F*dt
    star2.pos = star2.pos + (star2.p/star2.mass)*dt
    star1.p = star1.p - F*dt
    star1.pos = star1.pos + (star1.p/star1.mass)*dt
    parr2.pos = star2.pos
    parr2.axis = star2.p*pscale
    parr1.pos = star1.pos
    parr1.axis = star1.p*pscale
    rA1 = star1.pos-locationA
    rarr1.axis = rA1
    L1 = cross(rA1,star1.p)
    Larr1.axis = L1*Lscale
    rA2 = star2.pos-locationA
    rarr2.axis = rA2
    L2 = cross(rA2,star2.p)
    Larr2.axis = L2*Lscale
    Larr.axis = (L1+L2)*Lscale
    Llabel1.pos = Larr1.pos+Larr1.axis+vector(0,h,0)
    Llabel2.pos = Larr2.pos+Larr2.axis+vector(0,h,0)
    Llabel.pos = Larr.pos+Larr.axis+vector(0,h,0)
    
    
    
    
