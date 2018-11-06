GlowScript 2.7 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

scene.width = 1000
scene.height = 600
scene.background = color.white

#Parameters
wavelength = 600
scene.range = 1*wavelength
E0 = 1e4
c = 3e8

frequency = c/wavelength
period = 1/frequency
dt = 3e-4*period
t = 0

#Make a list of observation locations along a line
pointlist=arange(-3*wavelength/2, 3*wavelength/2, wavelength/16)
arrowlist=[]

#Loop over observation locations and create electric and magnetic field arrows there
#Add the arrows to a list
for x in pointlist:
    Earrow=arrow(pos=vector(x,0,0), color=color.orange, shaftwidth=wavelength/40)
    Earrow.B=arrow(pos=vector(x,0,0), color=color.cyan, shaftwidth=wavelength/40)
    arrowlist.append(Earrow)
    if abs(x) < 0.03*wavelength:
        Earrow.color = color.red
        Earrow.B.color = color.black

yy = -wavelength*.65
xx = -0.5*wavelength
dyy = wavelength/5
pts = [vector(xx,yy+dyy,0),vector(xx,yy-dyy,0),vector(xx,yy,0),vector(xx+wavelength,yy,0),
       vector(xx+wavelength,yy+dyy,0),vector(xx+wavelength,yy-dyy,0)]
ruler = curve(color=color.green, pos=pts,radius=wavelength/60)
run = True

def B_Runbutton(b):
    global run
    run = not run
    if run:
        b.text = "Pause"
    else:
        b.text = "Run"

button(text="Pause", bind=B_Runbutton)

scene.append_to_caption("      The green marker indicates the length of one wavelength.")

#Dynamics of wave motion
while True:
    rate(1000)
    if not run: continue
    #Loop over arrows and update their axes according to planewave equation
    for Earrow in arrowlist:
        E = vector(0,E0*cos(2*pi*(frequency*t-Earrow.pos.x/wavelength)),0)
        B = vector(0,0,E.y/c)
        Earrow.axis = E/40
        Earrow.B.axis = B*(c/50)
    t = t+dt
    
    
    
    
