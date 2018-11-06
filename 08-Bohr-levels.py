GlowScript 2.7 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

## energy levels of Bohr atom; graphs of K, U, K+U
## 2003-03-16

scene.title = "Bohr model of the atom"

scene.height = 300
scene.width = 300
scene.range = 2e-9
scene.zoom = scene.spin = False
background = color.white
flash = color.black
scene.background = background

def circle(radius, thickness, tint):
    dtheta = 2*pi/50
    angles=arange(0,2*pi+dtheta, dtheta)
    c = curve(color=tint, radius=thickness)
    for a in angles:
        c.append(radius*vector(cos(a),sin(a),0))
    return c

# atom
nucleus=sphere(radius=1e-11, color=color.red)
hbar = 1.05e-34
oofpez = 9e9
qe = 1.6e-19
m = 9e-31
levels=[]

for N in arange(1,6,1):
    r = (N**2)*(hbar**2)/(oofpez*(qe**2)*m)
    levels.append(circle(r, 1e-11, vector(0,0.5,0)))

rs = 1.2*(5**2)*(hbar**2)/(oofpez*(qe**2)*m)
Stop = box(pos=vector(-1*rs, -rs,0), color=color.cyan, size=vector(10e-10,5e-10,1e-12))
Stoplabel = label(pos=Stop.pos, color=color.black, text='Pause', box=0, opacity=0)
label(pos=vector(0,rs,0), text='Click here to cycle through levels.', color=color.black, box=0, opacity=0)

# energy, well and level graphs
gforeground = color.black
if version[1] == 'glowscript':
    Wg = graph(title="energy (eV) vs. distance (m)", width=400, height=200, ymax=0, ymin=-14.0, xmax=36*0.53e-10)
    Eg = graph(title="energy (eV), K(blue)+U(green)=magenta, vs. time", height=200 )
else:
    Wg = graph(x=300, y=0, title="energy (eV) vs. distance", width=400, height=300, ymax=0, ymin=-14.0, xmax=36*0.53e-10, background=color.white, foreground=color.black)
    Eg = graph(x=0, y=300, title="energy (eV), K(blue)+U(green)=magenta, vs. time", width=700, height=200, background=color.white, foreground=color.black )

U = gcurve(graph=Wg)
Kg = gcurve(graph=Eg, color=vector(0,0,0.8))
Ug = gcurve(graph=Eg, color=vector(0,0.8,0))
KUg = gcurve(graph=Eg, color=vector(0.8,0,0.8))

for r in arange(0.53e-10, 36*0.53e-10, 0.53e-10):
    Uel = -oofpez*qe/r
    U.plot(pos=(r,Uel))
states=[]
for N in arange(1,6,1):
    r = N**2*0.53e-10
    E = -13.6/N**2
    lvl = gcurve(graph=Wg, pos=([(0,E), (2*r,E)]), color=color.black)
    states.append(lvl)

states[0].color=color.magenta

# orbits
N=1
r=(N**2)*0.53e-10
omega = N*hbar/(m*r**2)
electron=sphere(radius=4e-11, color=color.blue, pos=vector(r,0,0))
dt = (2*pi/omega)/100
t = 0.0

stopped = False

clicked = False
def getclick():
    global clicked
    clicked = True
    
scene.bind("click", getclick)

## increase energy
up = True

tflash = -1 # if t > 0, flash is in process

while True:
    rate(400)
    if clicked:
        clicked = False
        ret = scene.mouse.pick
        if scene.mouse.pick == Stop:
            stopped = not stopped
            if stopped: Stoplabel.text = 'Run'
            else: Stoplabel.text = 'Pause'
            continue
        scene.background = flash
        tflash = clock()
        if up:
            states[N-1].color = gforeground
            N = N + 1
            states[N-1].color = color.magenta
            if N is 5:
                up = False
        else:
            states[N-1].color = gforeground
            N = N -1
            states[N-1].color = color.magenta
            if N is 1:
                up = True
        r = (N**2)*0.53e-10
        omega = N*hbar/(m*r**2)
    if stopped:
        continue
    else:
        if tflash > 0 and clock()-tflash >= 0.5:
            scene.background = background
            tflash = -1
        electron.pos = r*vector(cos(omega*t), sin(omega*t), 0)
        t = t+dt
        K = 0.5*oofpez*(qe)/r
        U = -oofpez*(qe)/r
        Kg.plot(pos=(t,K))
        Ug.plot(pos=(t,U))
        KUg.plot(pos=(t,(K+U)))
        
        
        
        
