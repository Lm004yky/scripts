GlowScript 2.7 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Ruth Chabay Spring 2001

scene.width = 1000
scene.height = 650
scene.background = color.white
scene.forward = vector(0,-.2,-1)
scene.range = 8

lamb = 2     
c = 3e8
omega = 2*pi*c/lamb
d=2*lamb
L=2*lamb
antenna = cylinder(pos=vector(0,-L/2,0), axis=vector(0,L,0), color=color.gray(.7), radius=0.5)

Evec = []

dist_to_screen = 4.0*lamb    
dts = dist_to_screen
ds = lamb/20
dt = lamb/c/100
E0 = lamb*5

slit1 = vector(0,0,0)
rvectors=[]
dtheta = pi/3
for theta in arange(0,2*pi,dtheta):
    r1 = vector(dts*cos(theta),0,dts*sin(theta))
    rvectors.append(r1)
    
## create waves
for r1 in rvectors:
    dr1 = ds*norm(r1)
    rr1 = slit1 + 10*dr1
    for i in range(120):
        ea = arrow(pos=rr1, axis=vector(0,(E0*cos(2*pi*mag(rr1-slit1))/lamb),0), color=color.orange, shaftwidth=lamb/40, r=norm(r1), visible=False)
        ba = arrow(pos=rr1, axis=vector(0,0,0), color=color.cyan, shaftwidth=lamb/40, visible=False)
        ea.B = ba
        Evec.append(ea)
        rr1 = rr1 + dr1

run = False
first = True
showB = False # don't show B vectors

def B_Runbutton(b):
    global run
    run = not run
    if run:
        b.text = "Pause"
    else:
        b.text = "Run"

def B_ShowBbutton(b):
    global showB
    showB = not showB
    for a in Evec:
        a.B.visible = showB
    if showB:
        b.text = "Hide B"
    else:
        b.text = "Show B"
        
button(text="Run", bind=B_Runbutton)

scene.append_to_caption("      ")
        
button(text="Show B", bind=B_ShowBbutton)

t = 0
while True:
    rate(50)
    if not run: continue
    for ea in Evec:
        decrease = 1/(mag(ea.pos)+lamb/20)
        ea.axis = vector(0,decrease*E0*cos(omega*t - 2*pi*mag(ea.pos-slit1)/lamb),0)
        ea.B.axis = cross(ea.r,ea.axis)*.7
        if first: ea.visible = True
    first = False
    t = t+dt
    
    
    
    
