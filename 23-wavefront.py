GlowScript 2.7 VPython

# Written by Bruce Sherwood, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

h = 10 # distance from source to surface
depth = h # depth of medium
thick = 0.05 # thickness of curves used to show crests
wavecolor = color.black
raycolor = color.red
scene.userspin = False
scene.userzoom = False
scene.height = 650
scene.width = 650
scene.fov = 0.001
scene.range = 1.9*h
scene.center = vector(-h,0,0)
scene.lights = []
distant_light(direction=vector(0,0,1), color=color.white)

n = 2 # index of refraction
if n >= 1:
    scene.background = color.white
    mediumcolor = color.gray(.1)
else:
    scene.background = color.gray(.8)
    mediumcolor = color.white
source = sphere(pos=vector(-h,0,0), radius=0.3, color=raycolor)
# Note that with pos.z = -0.1 and size.z = 0.2, the rays and wavefronts were visible
# on Windows, but on a Mac they were invisible. The fix was to move the center of
# the box, pos.z, back to -0.2, so that the front of the box is definitely behind z = 0.
medium = box(pos=vector(depth/2,0,-0.2), size=vector(depth,4*h,0.2), color=mediumcolor)

Nchords = 50
Ntimes = 50  # how many moves between crests
Ncrests = 10 # how many crests visible at one time

wavelength = (3*h+n*h)/Ncrests

def makewave(pos, R, angle):
    posdata1 = []
    posdata2 = []
    for i in range(Nchords+1):
        posdata1.append(vector(0,0,0))
        posdata2.append(vector(0,0,0))
    chords = Nchords
    if angle != 0:
        chords = int(Nchords*(pi-angle)/pi+0.5)
    dangle = 2*(pi-angle)/chords
    theta = angle
    for i in range(chords+1):
        posdata1[i] = vector(pos.x+R*cos(theta),pos.y+R*sin(theta),0)
        theta += dangle
    if chords == Nchords:
        return posdata1, posdata2[:1]
    else:
        posdata2[0] = posdata1[chords]
        nchords = Nchords-chords
        dangle = 2*angle/nchords
        theta = -angle
        lastd = h/cos(theta) # distance from source
        lasty = h*tan(theta)
        lastdm = 0 # distance in medium from surface to crest
        for i in range(nchords):
            theta += dangle
            d = h/cos(theta) # distance from source of next ray
            y = h*tan(theta)
            dm = lastdm+(lastd-d)/n # distance in medium from surface to crest
            refract = asin(sin(theta)/n)
            '''
            try:
                refract = asin(sin(theta)/n)
            except:
                if y < 0:
                    y = -h*tan(asin(n))
                else:
                    y = h*tan(asin(n))
                refract = theta
            '''
            posdata2[i+1] = vector(dm*cos(refract),y+dm*sin(refract),0)
            lastd = d
            lastdm = dm
            lasty = y
        return posdata1[:chords+1], posdata2[:nchords+1]

# Create curves at each of their starting positions (Ncrests is the number of them)
waves = []
for i in range(Ncrests):
    R = i*wavelength
    if R <= h:
        angle = 0
    else:
        angle = acos(h/R)
    wave = makewave(source.pos, R, angle)
    waves.append( [R, curve(pos=wave[0], color=wavecolor, radius=thick, visible=False),
                      curve(pos=wave[1], color=wavecolor, radius=thick, visible=False)] )

# Show rays
maxangle = 0.9*atan(medium.height/2/h)
Nrays = 16
dangle = 2*pi/Nrays
for a in range(Nrays):
    angle = (a+.5)*dangle
    if angle <= maxangle or angle >= 2*pi-maxangle:
        incoming = curve(pos=[source.pos, vector(0,h*tan(angle),0)], radius=thick, color=raycolor)
        refract = asin(sin(angle)/n)
        outgoing = curve(pos=[incoming.point(1).pos,
                              vector(medium.length,h*tan(angle)+medium.length*tan(refract),0)], radius=thick, color=raycolor)
        '''
        try:
            refract = asin(sin(angle)/n)
            outgoing = curve(pos=[incoming.pos[1],
                                  vector(medium.length,h*tan(angle)+medium.length*tan(refract),0)], radius=thick, color=raycolor)
        except: # total internal reflection
            outgoing = curve(pos=[incoming.pos[1],
                                  vector(incoming.pos[1])+vector(-3*h,3*h*tan(angle),0)], radius=thick, color=raycolor)
        '''
    else:
        curve(pos=[source.pos, source.pos+vector(3*h*cos(angle),3*h*sin(angle),0)], radius=thick, color=raycolor)


# Animate; Each of the Ncrests curves moves out until it reaches where the next one
# out had begun. At that time the curve reverts back to where it was first created.
advances = 0
t = 0
dt = 1
while True: 
    rate(20)
    if advances >= Ntimes:
        advances = 0
        for i in range(Ncrests-1):
            waves[Ncrests-1-i][0] = waves[Ncrests-2-i][0]
        waves[0][0] = 0
    nwave = 0
    for wave in waves:
        R = wave[0]
        R += wavelength/Ntimes
        if R <= h:
            angle = 0
        else:
            angle = acos(h/R)
        wave[0] = R
        pos1, pos2 = makewave(source.pos, R, angle)
        wave[1].clear()
        wave[1].append(pos1)
        wave[1].visible = (t >= nwave*Ntimes)
        wave[2].clear()
        wave[2].append(pos2)
        wave[2].visible = (t >= nwave*Ntimes)
        nwave += 1
    advances += 1
    t += dt
    
    
    
