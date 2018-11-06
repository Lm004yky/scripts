GlowScript 2.7 VPython

# Written by Joe Heafner, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# This program visualizes the radiative E and B fields of a charged particle
# receiving a brief acceleration. Before the acceleration, the particle was
# stationary. After the acceleration, the particle moves with constant
# momentum although this motion is not shown. For obvious reasons, the
# outgoing pulse will have already propagated a finite distance from the
# particle when the simulation starts.
#
# Written by Joe Heafner, April 2003

# Set up the scene
scene.width = 800
scene.height = 700
scene.forward = vector(-1, -1, -5)
scene.background = color.white
scene.range = 1e-011

# Create an array of field points (observer locations). This is a spherical
# distribution of points, but you could also use a rectangular distribution
# of points.

# Coordinate transformation for the grid of field points.
# Note that this is not the standard textbook transformaton!
# <x, y, z> = <r sin(theta) cos(phi), r cos(theta), r sin(theta) sin(phi)>
# phi wraps around the y-axis
# theta is relative to +y-axis
#
# This mapping of spherical coords to rectangular coords matches VPython's
# coordinate axis orientation, with y pointing "up". This is merely a matter
# of taste though. Most textbooks use the convention that z points up.

c = 3e8 # Speed of light
c2 = c**2

# Define a charged particle
particle = sphere(pos=vector(0,0,0), color=color.red, radius=3e-13)

particle.charge = 1.6e-19
particle.color = color.red

acc = vector(0,-2e17,0) # Define particle's acceleration

ascale = 0.04*2e-11/1e17 # Scale factor for pretty acc arrow

accarr = arrow(pos=particle.pos, axis=ascale*acc, shaftwidth=0.2e-12, color=color.yellow)

kel = 9e9 # Coulomb constant

escale = 0.1*2e-11/500 # Scale factor for pretty E arrows

bscale = 0.3*2e-11/1e-5 # Scale factor for pretty B arrows

rmin = 0.3e-11  # Minimum radius
dr = 0.5e-11    # Increment in radius
dtheta = pi/6  # Increment in theta
dphi = pi/6    # Increment in phi

obsloc = []     # Empty array
for r in arange(rmin, 2*rmin, dr): 
    for phi in arange(0, 2*pi+dphi, dphi):
        for theta in arange(dtheta, pi+dtheta, dtheta):
            obsloc.append(vector(0,0,0))
            
def reset_obsloc():
    # We need the extra dr if we want r to assume the last possible value.
    # This is also apparently necessary for theta and phi.
    i = 0
    for r in arange(rmin, 2*rmin, dr): 
        for phi in arange(0, 2*pi+dphi, dphi):
            # Start theta at something other than zero in order to avoid a
            # singularity on the y-axis.
            for theta in arange(dtheta, pi+dtheta, dtheta):
                obsloc[i] = vector(r*sin(theta)*cos(phi), r*cos(theta), r*sin(theta)*sin(phi))
                i += 1
                # Put a tiny dot at each point if desired
                # sphere(pos=a, radius=1e-13, color=color.green)

# Create an array of E and B and a_perp arrows
Earr = []     # Empty array
Barr = []     # Empty array
for i in range(len(obsloc)):
    Earr.append(arrow(shaftwidth=0.2e-12, color=color.orange))
    Barr.append(arrow(shaftwidth=0.2e-12, color=color.cyan))

def create_arrows(vis):
    for i,pt in enumerate(obsloc):

        # Position of field point relative to particle
        r = pt - particle.pos
        rhat = norm(r)

        # The component of acceleration perpendicular to r is just vector r
        # minus the parallel component of acceleration. The parallel component
        # of acceleration has a magnitude equal to the dot product of acceleration
        # and rhat, and is directed parallel to rhat.
        aperp = acc - acc.dot(rhat)* rhat

        # Visualize a_perp at each point if desired
        # Not recommended if you're visualizing the fields
        # a = arrow(pos=pt, axis=ascale*aperp, shaftwidth=0.2e-12, color=color.green)
        # aarr.append(aa)

        # Calculate radiative E field
        Erad = -kel * particle.charge * aperp / (pow(c,2 )* mag(r))
        
        Earr[i].pos = pt
        Earr[i].axis = escale*Erad
        Earr[i].visible = vis

        # Calculate radiative B field
        # The B field has magnitude E/c and is in the direction of rhat cross Erad.
        rhatcrossE = rhat.cross(Erad)
        Brad =  (mag(Erad)/c) * norm(rhatcrossE)
        
        Barr[i].pos = pt
        Barr[i].axis = bscale*Brad
        Barr[i].visible = vis

def show_arrows():
    for i in range(len(obsloc)):
        Earr[i].visible = True
        Barr[i].visible = True

reset_obsloc()
create_arrows(False)

run = False
first = True # signals need to make arrows visible

def Brun(b):
    global run, first
    run = not run
    if run:
        b.text = "Pause"
        if first:
            first = False
            show_arrows()
    else:
        b.text = "Run"

Runbutton = button(text='Run', bind=Brun)

scene.append_to_caption('  ')

def Resetbutton():
    global run, t, first
    run = False
    Runbutton.text = "Run"
    t = 0
    reset_obsloc()
    create_arrows(False)
    first = True
    
def prereset(b):
    Resetbutton()

button(text='Reset', bind=prereset)

scene.append_to_caption('  ')

def flip_charge(c):
    particle.charge = -particle.charge
    if particle.charge > 0:
        particle.color = color.red
        c.text = "- charge"
    else:
        particle.color = color.blue
        c.text = "+ charge"
    Resetbutton()

button(text='-charge', bind=flip_charge)

scene.append_to_caption("   An accelerated charge radiates electric (orange) and magnetic (cyan) fields.")

# Propagate the pulse
dt = 1e-22
t = 0
while True:
    rate(30)
    if not run: continue
    
    i = 0
    for pt in obsloc:
        
        # Get a new field point by increasing the magnitude of the current
        # vectortor from the field point to the origin. The components will
        # automatically be updated.
        pt = norm(pt)*(mag(pt) + c * t)
        r = pt - particle.pos
        rhat = norm(r)

        # Update perpendicular component of acceleration
        aperp = acc - acc.dot(rhat) * rhat
        
        # aarr[i].pos = pt
        # aarr[i].axis = ascale*aperp

        # Update the E field and B field
        Erad = -kel * particle.charge * aperp / (pow(c,2 )* mag(r))
        Earr[i].pos = pt
        Earr[i].axis = escale*Erad
        rhatcrossE = rhat.cross(Erad)
        Brad = (mag(Erad)/c) * norm(rhatcrossE)
        Barr[i].pos = pt
        Barr[i].axis = bscale*Brad
        i = i + 1
    
    t = t + dt
    
    
    

