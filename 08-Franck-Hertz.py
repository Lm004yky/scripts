GlowScript 2.7 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

## Simplified Franck-Hertz experiment visualization
## 2003-03-16

scene.width=800
scene.height=300
scene.title="Franck-Hertz experiment"
scene.background=color.white
scene.foreground=color.black

# parameters
E0 = 4.9*1.6e-19 # energy of first excited state of mercury atom
L=0.5 # distance between the plates
dVacc = 1 # potential difference between the plates
dVacc_max = 10
E = None # electric field
Run = False
done = False # True if reached the plate on the right

def set_dV(vs):
    global dVacc, E, L
    dVacc = vs
    E = vector(-dVacc/L,0,0)

def reset():
    global Ke, Run, done
    clr = color.rgb_to_hsv(Ke.color)
    hue = clr.x
    electron.pos = vector(-L/2,0,0)
    electron.p = vector(0,0,0)
    Far.pos = electron.pos
    Far.axis=vector(0,0,0)
    par.pos = electron.pos
    par.axis = vector(0,0,0)
    Hg.color=vector(.6,.6,.6)
    t=0
    hue = hue+0.15
    if hue > 1:
        hue = hue-1
    Ke = gcurve(color=color.hsv_to_rgb(vector(hue,1,0.8)))
    done = False
    Run = False
    Runbutton.text = "Run"
    

set_dV(1) # initialize potential difference to 1 volt

# electron and Hg atom
electron=sphere(pos=vector(-L/2,0,0), radius=0.005, color=color.cyan)
electron.q = -1.6e-19
electron.m = 9e-31
electron.p = electron.m*vector(0,0,0)
Far = arrow(pos=electron.pos, shaftwidth=electron.radius, color=color.orange, axis=vector(0,0,0))
Fscale = (L/40)/abs(electron.q*mag(E))
offset = vector(0,electron.radius,0)
par = arrow(pos=electron.pos+offset, color=color.green, shaftwidth=electron.radius, axis=vector(0,0,0))
pscale = (2*L/10)/(1e-24)

Hg = sphere(pos=vector(L/4,0,0), radius=2*electron.radius, color=color.white)
Hg.v = vector(0,0,0)
Hg.m = 201*1.7e-27
d = 0.14
# emitter and collector
emitter=box(pos=vector(-1.1*L/2,0,0), size=vector(0.001,d,d), color=color.blue)
collector = box(pos=vector(1.1*L/2,0,0), size=vector(0.001,d,d), color=color.red)
dt = 1e-10

explain = label(pos=vector(0,0.8*d,0), text='Orange arrow represents force on electron; green arrow represents its momentum.',
    color=color.black, box=0, opacity=0, visible=False)

Vleft = label(pos=emitter.pos-vector(0,0.6*d,0), text='0 V', color=color.black, opacity=0, box=0)
Vright = label(pos=collector.pos-vector(0,0.6*d,0), text='1.0 V', color=color.black, opacity=0, box=0)

def Runb(r):
    global Run, done
    if done: 
        reset()
        Run = True
        r.text = "Pause"
    else:
        Run = not Run
        if Run:
            r.text = "Pause"
        else:
            r.text = "Run"

Runbutton = button(text='Run', bind=Runb)

scene.append_to_caption('   ')

button(text='Reset', bind=reset)

def sliderchange(s):
    set_dV( s.value )
    V = str(round(10*dVacc))
    if len(V) == 1: V = '0'+V
    V = V[0]+'.'+V[1]
    Vright.text = V+' V'

scene.append_to_caption('   Use the slider to set the voltage difference between the plates.\n\n')

slider(value=dVacc, max=dVacc_max, length=800, bind=sliderchange)

scene.fov = 0.5
scene.range = 0.3*L
scene.append_to_caption('\n ')
grafs = graph(ytitle="Electron kinetic energy (eV)", xtitle="position", width=scene.width, height=300,
                    xmax=1.1*L, ymax=dVacc_max, 
                    background=color.white, foreground=color.black)
               
Ke = gcurve(color=color.red)
Ke.plot(pos=(0,0))

while True:
    rate(50)
    if not Run: continue
    explain.visible = True
    done = False
    collide=False
    t=0
    while electron.pos.x < collector.pos.x:
        rate(1000)
        if not Run: continue
        F = electron.q * E
        electron.p = electron.p + F*dt
        electron.pos = electron.pos + (electron.p/electron.m)*dt
        Hg.pos = Hg.pos + Hg.v*dt
        Far.pos = electron.pos
        Far.axis = F*Fscale
        par.pos = electron.pos+offset
        par.axis = pscale*electron.p
        K=mag(electron.p)**2/(2*electron.m)
        K2 = K/1.6e-19
        Ke.plot(pos=(electron.pos.x+L/2.,K2))
        if (mag(Hg.pos - electron.pos) < electron.radius) and not collide:
            if K >= E0:
                collide = True
                K = K-E0
                p0 = electron.p
                pmag = sqrt(2*electron.m*K)
                electron.p = vector(pmag,0,0)
                pHg = p0 - electron.p
                Hg.v = pHg/Hg.m
                #print Hg.v
                Hg.color=vector(1,.4,1)
        t=t+dt
    Run=False
    Runbutton.text = 'Run'
    done = True
    
    
    
    
    

