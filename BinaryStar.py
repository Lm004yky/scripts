GlowScript 2.6 VPython

# http://internal.physics.uwa.edu.au/~andrew/teaching/

win=1000
scene = display(title="Orbit", width=win, height=win, range=4e11, forward=vector(0,-1,0), up=vector(-1,0,0) )

giant = sphere()
giant.pos = vector(-1e11,0,0)
giant.radius = 2e10
giant.color = color.red
giant.mass = 1e30
giant.p = vector(0, 0, -1e2) * giant.mass

dwarf = sphere()
dwarf.pos = vector(1.5e11,0,0)
dwarf.radius = 1e10
dwarf.color = color.yellow
dwarf.mass = 1e28
dwarf.p = -giant.p

for a in [giant, dwarf]:
  a.orbit = curve(color=a.color, radius = 2e9)

dt = 86400

autoscale=0
autocenter=0

startbar=None
endbar=None
starttick=-1

while 1:
  rate(100)

  dist = dwarf.pos - giant.pos
  force = 6.7e-11 * giant.mass * dwarf.mass * dist / mag(dist)**3
  giant.p = giant.p + force*dt
  dwarf.p = dwarf.p - force*dt

  for a in [giant, dwarf]:
    a.pos = a.pos + a.p/a.mass * dt
    a.orbit.append(pos=a.pos)


# http://internal.physics.uwa.edu.au/~andrew/teaching/
# Some VPython software for teaching astronomy
#To use these, you'll need Python and VPython
#Unless otherwise indicated, all code is copyright Andrew Williams, but freely usable for teaching purposes. If anyone uses any of this code, please let me know, especially if you alter it or add features. See my home page for other non-teaching software.
#tempdemo.py: Demonstrates the color and energy vs wavelength curve for a black body at varying temperatures (you also need blackbody.py, which was adapted from the C code at http://www.physics.sfasu.edu/astro/color.html). The color estimation isn't particularly accurate, see here for more accurate colors).
#stars2.py: Demonstrates collapse and 'evaporation' for a small star cluster, a slightly modified version of a demo program that comes with VPython.
#tullys.py and the source data, tully.csv: Interactive 3D view of the 2367 galaxies in the Tully 'Nearby Galaxy Catalog'. Sizes are scaled up by a factor of 10, and spiral orientations are random, not real. Left-click on a galaxy to see its name.
#Norbit.py: Demonstrates Kepler's second law (an orbit sweeps out equal areas per unit time) with a modified version of 'orbit.py' from the VPython distribution. Click to highlight the area swept out over the next 0.5 seconds).
#moon.py: Demonstrates 1:1 tidal locking in the Moon's orbit (not to scale)
#mercury.py: Demonstration of 3:2 tidal locking in Mercury's orbit (not to scale)
#mars.py: Demonstrates oppositions of Mars showing Mars and Earth's orbits (not to scale)
  
