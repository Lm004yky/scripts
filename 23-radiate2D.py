GlowScript 2.7 VPython

# Written by Joe Heafner, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Joe Heafner, April 2003

# Set up the scene
scene.background = color.white
scene.width = 1000
scene.height = 650
scene.range = 0.7e-11
scene.caption = "Accelerated charge; click to run or pause."

rmin = 0.3e-11 # Minimum radius
dr = 0.5e-11 # Increment in radius
dtheta = pi/6 # Increment in theta
dphi = pi/6 # Increment in phi

obsloc = [] # Empty array
phi = 0
# Start theta at something other than zero in order to avoid a singularity on the y-axis.
for theta in arange(dtheta, 2*pi+dtheta, dtheta):
    r = vector(rmin*sin(theta)*cos(phi), rmin*cos(theta), rmin*sin(theta)*sin(phi))
    vis = abs(r.x) > 1e-13
    rhat = norm(r)
    obsloc.append([r,
                   arrow(pos=vector(0,0,0), axis=r, shaftwidth=0.1e-12, color=color.green),  # radius vectors
                   arrow(pos=r, axis=rhat*1e-12, color=color.magenta, visible=vis)]) # propagation velocity
# Speed of light
c = 3e8
c2 = c**2
# Define a charged particle:
particle = sphere(pos=vector(0,0,0), radius=3e-13, color=color.red)
# Make the charge negative if you want an electron (also make it blue!)
particle.charge = 1.6e-19
if particle.charge < 0:
    particle.color=color.blue
    
#####################################
if particle.charge > 0:
## unsaturate particle to indicate old position
    particle.color = vector(1,.7,.7)  
else:
    particle.color = vector(.7,.7,1)
####################################
    
acc = vector(0,-2e17,0) # Define particle's acceleration

ascale = 0.04*2e-11/1e17 # Scale factor for pretty acc arrow

accarr = arrow(pos=particle.pos, axis=ascale*acc, shaftwidth=0.2e-12, color=color.yellow)
label(pos=accarr.pos + accarr.axis, xoffset=5, text="a",
               color=color.black, box=0, line=0, opacity=0)

oofpez = 9e9 # Coulomb constant, one-over-four-pi-epsilon-zero

escale = 0.1*2e-11/500 # Scale factor for pretty E arrows

bscale = 0.3*2e-11/1e-5 # Scale factor for pretty B arrows

# Create an array of E and B and a_perp arrows
Earr = [] # Empty array
Barr = [] # Empty array

for o in obsloc:
    # Position of field point relative to particle
    pt = o[0]
    vis = abs(pt.x) > 1e-13
    Earr.append(arrow(pos=pt, shaftwidth=0.2e-12, color=color.orange, visible=vis))
    Barr.append(arrow(pos=pt, shaftwidth=0.2e-12, color=color.cyan, visible=vis))

def reset():
    for i,o in enumerate(obsloc):
        # Position of field point relative to particle
        o[0] = rmin*norm(o[0])
        r = o[0] - particle.pos
        rhat = norm(r)
        o[1].pos = vector(0,0,0)
        o[1].axis = r
        o[2].pos = r
        o[2].axis = rhat*1e-12

        # The component of acceleration perpendicular to r is just vector r
        # minus the parallel component of acceleration. The parallel component
        # of acceleration has a magnitude equal to the dot product of acceleration
        # and rhat, and is directed parallel to rhat.
        aperp = acc - dot(acc,rhat)* rhat

        # Calculate radiative E field
        Erad = -oofpez * particle.charge * aperp / (c**2 * mag(r))
        Earr[i].axis = escale*Erad

        # Calculate radiative B field
        # The B field has magnitude E/c and is in the direction of rhat cross Erad.
        rhatcrossE = cross(rhat,Erad)
        Brad = (mag(Erad)/c) * norm(rhatcrossE)
        Barr[i].axis = bscale*Brad

reset()

def getclick(evt):
    global run, first
    run = not run
    if first:
        reset()
        first = False

scene.bind('click', getclick)

# Propagate the pulse
dt = 0.5e-22
t = 0
run = False
first = False
while True:
    rate(60)
    if not run: continue
    for i,o in enumerate(obsloc):
        # Get a new field point by increasing the magnitude of the current
        # vector from the field point to the origin. The components will
        # automatically be updated.
        pt = o[0]
        pt = (mag(pt) + c * dt)*norm(pt)
        o[0] = pt
        r = pt - particle.pos
        rhat = norm(r)
        o[1].axis = r
        o[2].pos = pt
        
        # Update perpendicular component of acceleration
        aperp = acc - dot(acc,rhat) * rhat

        # Update the E field and B field
        Erad = -oofpez * particle.charge * aperp / (c**2 * mag(r))
        rhatcrossE = cross(rhat,Erad)
        Brad = (mag(Erad)/c) * norm(rhatcrossE)
        Earr[i].pos = pt
        Earr[i].axis = escale*Erad
        Barr[i].pos = pt
        Barr[i].axis = bscale*Brad
    t = t + dt
    if t > 250*dt:
        t = 0
        first = True
        run = False

# This program visualizes the radiative E and B fields of a charged particle
# receiving a brief acceleration. Before the acceleration, the particle was
# stationary. After the acceleration, the particle moves with constant
# momentum although this motion is not shown. For obvious reasons, the
# outgoing pulse will have already propagated a finite distance from the
# particle when the simulation starts.
#
# Joe Heafner, April 2003
#
# Future modifications:
#  1) show Poynting vector
#  2) show the radial field inside and/or outside the spherical wavefront
#  3) allow the particle to oscillate

# slowed down; added mouse clicks Ruth Chabay 11/2004
# modified to show planar slice, include r vectors

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
# of taste though. Most advanced textbooks use the convention that z points up.
