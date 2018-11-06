GlowScript 2.7 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Ruth Chabay Spring 2001
# A plane sinusoidal wave; show there are E and B fields throughout space.

scene.width = 600
scene.height = 600
scene.background = color.white

c = 3e8
lamb = 1e-10
scene.range = 2*lamb

h = 1e-10
omega = 2*pi*c/lamb
scene.center = vector(-lamb,0,0)
scene.forward = vector(-1,-0.2,-1)

xx = arange(-2*lamb,0.001*lamb, lamb/20)
box(pos=vector(-2*lamb,0,0), size=vector(0.01*lamb, 2.5*h, 2.5*h), color=color.gray(0.7), opacity=0.1)
box(pos=vector(-lamb,0,0), size=vector(0.01*lamb, 2.5*h, 2.5*h), color=color.gray(0.7), opacity=0.1)

xhat = vector(1,0,0)

Evec = []
for z in [-h,0,h]:
    for y in [-h,0,h]:
        for x in xx:
            ea = arrow(pos=vector(x,y,z), axis=vector(0,lamb/10,0), color=vector(1,0.6,0), shaftwidth=lamb/40)
            ba = arrow(pos=vector(x,y,z), axis=vector(0,0,0), color=vector(0,1,1), shaftwidth=lamb/40)
            if abs(x+1*lamb) < 0.03*lamb:
                ea.color = color.red
                ba.color = color.black
            ea.B = ba
            Evec.append(ea)

t = 0
dt = lamb/c/100
E0 = lamb/3
run = True

def B_Runbutton(b):
    global run
    run = not run
    if run:
        b.text = "Pause"
    else:
        b.text = "Run"

button(text="Pause", bind=B_Runbutton)

scene.append_to_caption("      In a plane wave, there is E and B throughout the space.")

while True:
    rate(50)
    if not run: continue
    t = t+dt
    for ea in Evec:
       ea.axis = vector(0,E0*cos(omega*t - 2*pi*ea.pos.x/lamb),0)
       ea.B.axis = cross(xhat,ea.axis)*0.7
       
       
       
       
       
