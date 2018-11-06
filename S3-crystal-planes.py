GlowScript 2.7 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Ruth Chabay Spring 2001

scene.width = scene.height = 650
scene.background = color.white
scene.forward = vector(1,-0.8,-2)
scene.range = 4.5
scene.caption = "Click to see planes containing many atoms."

def wirebox (s, boxcolor):
    pts = [vector(-s, -s, -s), vector(-s, -s, s), vector(-s, s, s), \
           vector(-s, s, -s), vector(-s, -s, -s), vector(s, -s, -s), \
           vector(s, s, -s), vector(-s, s, -s), vector(s, s, -s), \
           vector(s, s, s), vector(-s, s, s), vector(s, s, s), \
           vector(s, -s, s), vector(-s, -s, s), vector(s, -s, s), vector(s, -s, -s)]
    for i,pt in enumerate(pts):
        pts[i] = pt - vector(1,1,1)
    return curve(color=boxcolor, radius=0.05, pos=pts)

for x in arange(-2, 3, 2):
    for z in arange (-2, 3, 2):
        for y in arange (-2, 3, 2):
            a=sphere(pos=vector(x,y,z), radius = 0.3, color=vector(1,0,1))

for x in arange (-1, 3, 2):
    for z in arange (-1, 3, 2):
        for y in arange (-1, 3, 2):
            a=sphere(pos=vector(x,y,z), radius = 0.3, color=vector(0,1,1))

unit = wirebox(1, color.gray(.8))

op = 0.7
plane1=box (pos=vector(0,0,0), size=vector(6,0.01,6), color=color.gray(.8),
            visible=False, opacity=op)

plane2 = box(pos=vector(0, 0, 0), size=vector(6,0.01,6), color=color.gray(.8),
             visible=False, opacity=op)
plane2.rotate(axis = vector(0,0,1), angle=pi/4)

scene.waitfor('click')
unit.visible = False
plane1.visible = True

while True:
    scene.waitfor('click')
    plane1.visible = False
    plane2.visible = True
    scene.waitfor('click')
    plane1.visible = True
    plane2.visible = False
    
    
    
