GlowScript 2.7 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Ruth Chabay Spring 2001

scene.width = 650
scene.height = 750
scene.forward = vector(-0.3,-1.5,-2)
scene.background = color.white
scene.range = 0.35

ihat=vector(1,0,0)
lamb = 0.1   
c = 3e8
omega = 2*pi*c/lamb
d = 2*lamb ## slit spacing

Evec1 = []
Evec2 = []
Evec3 = []
Evec4 = []

dist_to_screen = 4*lamb    
scene.center = vector(dist_to_screen*.65,-d/2,0)
ds = lamb/20
dt = lamb/c/100
E0 = lamb/3

screen = curve(pos = [vector(dist_to_screen,0,0),vector(dist_to_screen,0,1.5*d)], color=vector(0.6,0.6,0.6), radius=0.001)
slit1 = vector(0, 0, -d/2) 
slit2 = vector(0, 0, d/2)  

max1 = vector(dist_to_screen,0,0)
max2 = vector(dist_to_screen,0,0.24)
min1 = vector(dist_to_screen,0,0.108) 

#### vectors from slits to max2:
r1mx = max2 - slit1
r2mx = max2 - slit2
## vectors from slits to min1:
r1mn = min1 - slit1
r2mn = min1 - slit2

# vectors from slits to loc. on screen
dr1mx = ds*norm(r1mx)
dr2mx = ds*norm(r2mx)
dr1mn = ds*norm(r1mn)
dr2mn = ds*norm(r2mn)

rr1mx = slit1 + vector(0,0,0) ## current loc along wave 1
rr2mx = slit2 + vector(0,0,0) ## current loc along wave 2
rr1mn = slit1 + vector(0,0,0) ## current loc along wave 3
rr2mn = slit2 + vector(0,0,0) ## current loc along wave 4

i1 = None
i2 = None
i3 = None
i4 = None

## create first wave (max1)
ct = 0
while ct < 120:
    ea = arrow(pos=rr1mx, axis=vector(0,E0*cos(2*pi*mag(rr1mx-slit1)/lamb),0), color=color.red, shaftwidth=lamb/40)
    if abs(ea.pos.x - dist_to_screen) < 0.002 and i1 == None:
        i1 = ea
    else:
        Evec1.append(ea)
    rr1mx = rr1mx + dr1mx
    ct = ct + 1
    
## create second wave (max2)
ct = 0
while ct < 100:
    ea = arrow(pos=rr2mx, axis=vector(0,E0*cos(2*pi*mag(rr2mx-slit2)/lamb),0), color=vector(1.,.6,0), shaftwidth=lamb/40)
    if abs(ea.pos.x - dist_to_screen) < 0.002 and i2 == None:
        i2 = ea
    else:
        Evec2.append(ea)
    rr2mx = rr2mx + dr2mx
    ct = ct + 1

## create third wave (min1)
ct = 0
while ct < 120:
    ea = arrow(pos=rr1mn, axis=vector(0,E0*cos(2*pi*mag(rr1mn-slit1)/lamb),0), color=color.red, shaftwidth=lamb/40)
    if abs(ea.pos.x - dist_to_screen) < 0.002 and i3 == None:
        i3 = ea
    else:
        Evec3.append(ea)
    rr1mn = rr1mn + dr1mn
    ct = ct + 1
    
#### create fourth wave (min2)
ct = 0
while ct < 100:
    ea = arrow(pos=rr2mn, axis=vector(0,E0*cos(2*pi*mag(rr2mn-slit2)/lamb),0), color=vector(1.,.6,0), shaftwidth=lamb/40)
    if abs(ea.pos.x - dist_to_screen) < 0.002 and i4 == None:
        i4 = ea
    else:
        Evec4.append(ea)
    rr2mn = rr2mn + dr2mn
    ct = ct + 1

i1.visible = False
i3.visible = False
i2.axis = vector(0,0,0)
i2.color = color.green
i4.axis = vector(0,0,0)
i4.color = color.green
t=0
while True:
    rate(50)
    t = t+dt
    for ea in Evec1:
       ea.axis = vector(0,E0*cos(omega*t - 2*pi*mag(ea.pos-slit1)/lamb),0)
    for ea in Evec2:
       ea.axis = vector(0,E0*cos(omega*t - 2*pi*mag(ea.pos-slit2)/lamb),0)
    summx = E0*cos(omega*t - 2*pi*mag(i1.pos-slit1)/lamb)+E0*cos(omega*t - 2*pi*mag(i2.pos-slit2)/lamb) # superposition
    i2.axis = vector(0,summx,0)
    
    for ea in Evec3:
       ea.axis = vector(0,E0*cos(omega*t - 2*pi*mag(ea.pos-slit1)/lamb),0)
    for ea in Evec4:
       ea.axis = vector(0,E0*cos(omega*t - 2*pi*mag(ea.pos-slit2)/lamb),0)
    summn = E0*cos(omega*t - 2*pi*mag(i3.pos-slit1)/lamb)+E0*cos(omega*t - 2*pi*mag(i4.pos-slit2)/lamb) # superposition
    i4.axis = vector(0,summn,0)
    
    
    
