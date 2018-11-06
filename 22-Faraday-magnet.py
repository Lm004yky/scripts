GlowScript 2.7 VPython

# Written by Ruth Chabay and Bruce Sherwood, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Ruth Chabay 2007-08-07
# Revised Bruce Sherwood 2007-11-10

scene.height = 600
scene.width = 800
scene.background = color.white
scene.range = 0.45
scene.lights = []
distant_light(direction=vector(1,0,.5), color=color.gray(0.7))
distant_light(direction=vector(-1,0.5,0.5), color=color.gray(0.7))
Bcolor = vector(0,.5,.5)
Bcolorother = vector(.8,1,1)
sw = 0.01
swother = 0.005

def Bfield(source,obsloc):
    r = obsloc - source
    return kmag*(3*dot(mu,norm(r))*norm(r) - mu)/mag(r)**3

def showB():
    for arr in Bother:
        arr.axis=Bscale*Bfield(magnet.pos, arr.pos)

xhat = vector(1,0,0)

Rdisk = 0.3
f = cos(pi/4)
rmagnet = 0.03
Lmagnet = 0.12
dpole = 0.03
south = cylinder(pos=vector(-Lmagnet/2,0,0), radius=rmagnet, color = vector(0,0,1), axis=vector(dpole,0,0))
north = cylinder(pos=vector(Lmagnet/2,0,0), radius=rmagnet, color = vector(1,0,0), axis=vector(-dpole,0,0))
bar = cylinder(pos=south.pos+vector(dpole,0,0), radius=south.radius, axis = north.pos-vector(dpole,0,0)-south.pos-vector(dpole,0,0), color=vector(0.7,0.7,0.7))
magnet = compound([south, north, bar])

showallB = False # if True, show B at many places, not just within circle
surface = cylinder(pos=vector(0.4,0,0), radius=Rdisk, axis=vector(0.002,0,0), color=vector(0.9,0.9,0.9), opacity=0.5)

deltax = Lmagnet/5
kmag = 1e-7
mu = vector(1.0,0,0) # magnetic dipole moment of bar magnet

Bscale = 0.13*Rdisk/2e-6
Escale = 0.7*Rdisk/2e-7
xmax = 0.4*Rdisk

Earr=[]#E on perimeter of surface
for theta in arange(0,2*pi,pi/6):
    a=arrow(pos=vector(surface.pos.x, surface.radius*cos(theta),surface.radius*sin(theta)), axis=vector(0,0,0), color=color.orange, shaftwidth=.01)
    a.vv = norm(a.pos - surface.pos)
    Earr.append(a)

Bsurface = [] ## arrows on surface at which to calculate field, flux
dR = 0.2*Rdisk
for y in arange(-0.8*Rdisk,0.9*Rdisk,dR):
    a = arrow(pos=vector(surface.pos.x, y, 0),axis=vector(0,0,0), color=Bcolor, shaftwidth=sw)
    Bsurface.append(a)

Bother = [] ## locations at which to display magnetic field around magnet
dtheta = pi/6
phi = pi/4
for theta in arange(dtheta, pi-dtheta/2, dtheta):
    x = Rdisk*cos(theta)
    y = Rdisk*sin(theta)
    z = 0
    Bother.append( arrow(pos=vector(x,y,z), axis=vector(0,0,0)) )
    Bother.append( arrow(pos=vector(x,-y,z), axis=vector(0,0,0)) )
    Bother.append( arrow(pos=vector(x,z,y), axis=vector(0,0,0)) )
    Bother.append( arrow(pos=vector(x,z-y,0), axis=vector(0,0,0)) )
    Bother.append( arrow(pos=vector(x,y,z), axis=vector(0,0,0)) )
    Bother.append( arrow(pos=vector(x,y,z), axis=vector(0,0,0)) )
    Bother.append( arrow(pos=vector(x,y,z), axis=vector(0,0,0)) )
    Bother.append( arrow(pos=vector(x,y,z), axis=vector(0,0,0)) )
    Bother.append( arrow(pos=vector(x,y,z), axis=vector(0,0,0)) )

    a = vector(x,y,z)
    b = rotate(a,angle=phi, axis=vector(1,0,0))
    Bother.append( arrow(pos=vector(b.x,b.y,b.z), axis=vector(0,0,0)) )
    Bother.append( arrow(pos=vector(b.x,-b.y,b.z), axis=vector(0,0,0)) )
    b = rotate(a, angle=3*phi, axis=vector(1,0,0))
    Bother.append( arrow(pos=vector(b.x,b.y,b.z), axis=vector(0,0,0)) )
    Bother.append( arrow(pos=vector(b.x,-b.y,b.z), axis=vector(0,0,0)) )

for arr in Bother:
    arr.color = Bcolorother
    arr.shaftwidth = swother
    arr.visible = False

scene.center = surface.pos/2
scene.forward = -vector(1,0,2.5)

flux = 0
dt = 0.01
t = 0
vx = v0 = 0.1
dBdtarr = arrow(pos=surface.pos+vector(0,-0.1*Rdisk,0.2*Rdisk), axis=vector(0,0,0), color=color.magenta, shaftwidth=sw)
run = False

def Set_Runbutton(s):
    Runbutton.text = s

def B_Runbutton(b):
    global run, showallB
    run = not run
    if run:
        b.text = "Pause"
        for arr in Bsurface: arr.visible = True
        if showallB:
            for arr in Bother: arr.visible = True
    else:
        b.text = "Run"

def show_everywhere(bb):
    global showallB
    showallB = not showallB
    if showallB:
        bb.text= "Show B only inside loop"
        for b in Bother: b.visible = True
    else:
        bb.text = "Show B everywhere"
        for b in Bother: b.visible = False
        
Runbutton = button(text='Run', bind=B_Runbutton)

scene.append_to_caption("    Show B everywhere: ")
        
checkbox(bind=show_everywhere)

s = """\nFaraday's law: as magnet moves toward or away there is a curly electric field.
Magenta arrow represents -dB/dt."""
scene.append_to_caption(s)

while True:
    rate(0.5/dt)
    if not run: continue
    t = t + dt
    if abs(magnet.pos.x+vx*dt) > 0.7*xmax:
        if magnet.pos.x > 0:
            ax = -0.2
        else:
            ax = 0.2
    else:
        ax = 0
        if vx > 0:
            vx = v0
        else:
            vx = -v0
    vx += ax*dt
    magnet.pos.x += vx*dt
    showB()
    oldflux = flux
    flux = 0
    for arr in Bsurface:
        B = Bfield(magnet.pos, arr.pos)
        arr.axis = B*Bscale
        flux += dot(B,xhat)*pi*abs(arr.pos.y)*dR 
    dflux = flux - oldflux
    dBdtarr.axis = vector(-0.15*dflux/1e-8,0,0)
    E = (dflux/dt)/(2*pi*surface.radius)
    for a in Earr:
        a.axis = -E*Escale*cross(xhat,a.vv)
        
        
        
        
    

