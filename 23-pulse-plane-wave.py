GlowScript 2.7 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

scene.width = 1000
scene.height = 400
scene.background = color.white
scene.forward = vector(-0.1,-0.2,-1)
scene.fov = 0.01

#Parameters
wavelength = 600
scene.range = 0.5*wavelength
E0 = 200

wave = []
w = wavelength/40
for x in arange(0,wavelength,0.07*wavelength):
    wave.append(box(pos=vector(x,.4*E0,0), size=vector(0.8*E0,w,w), axis=vector(0,.8E0,0), color=color.orange))
    wave.append(pyramid(pos=vector(x,.8*E0,0), size=vector(.2*E0,2*w,2*w), axis=vector(0,.3*E0,0), color=color.orange))
    wave.append(box(pos=vector(x,0,.3*E0), size=vector(0.6*E0,w,w), axis=vector(0,0,.6*E0), color=color.cyan))
    wave.append(pyramid(pos=vector(x,0,.6*E0), size=vector(.15*E0,2*w,2*w), axis=vector(0,0,.15*E0), color=color.cyan))
    #Earrow = arrow(pos=vector(x,0,0), axis=vector(0,E0,0), color=color.orange, shaftwidth=wavelength/40)
    #Barrow = arrow(pos=vector(x,0,0), axis=vector(0,0,0.7*E0), color=color.cyan, shaftwidth=wavelength/40)
wave = compound(wave)

run = True
x = x0 = -2.5*wavelength
dx = 0.002*wavelength

def B_Runbutton(b):
    global run
    run = not run
    if run:
        b.text = "Pause"
    else:
        b.text = "Run"

Runbutton = button(text="Pause", bind=B_Runbutton)

scene.append_to_caption("      A plane wave in the form of a pulse, shown along just one line.")

#Dynamics of wave motion
while True:
    rate(200)
    if not run: continue
    wave.pos.x = x
    x = x + dx
    if x > 1.5*wavelength: x = x0
    
    
    
