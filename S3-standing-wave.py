GlowScript 2.7 VPython

# Written by Bruce Sherwood, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

lamb = 2
scene.width = 1000
scene.height = 600
scene.background = color.white
scene.range = 3*lamb
scene.center = vector(5*lamb,0,0)
scene.fov = 0.01
scene.userspin = False
scene.userzoom = False

omega = pi
k = 2*pi/lamb
v = omega/k
dx = 0.02
r = 0.05
A = 2
curve(pos=[vector(0,0,0), vector(10*lamb,0,0)], color=color.gray(0.9), radius=0.7*r)
left = curve(color=vector(1,0.95,0.95), radius=r)
right = curve(color=vector(0.9,1,1), radius=r)
wave = curve(color=color.blue, radius=r)
N = 0
for x in arange(0,12*lamb+dx/2,dx):
    wave.append(pos=vector(x,0,0))
    left.append(pos=vector(x,A*sin(k*x),r))
    right.append(pos=vector(x,A*sin(k*x),r))
    N += 1

xleft = 0
xright = 0

def reset(r):
    global xleft, xright
    xleft = -12*lamb
    xright = 10*lamb
    for i in range(N):
        wave.modify(i, y=0)

def B_Showbutton(b):
    left.visible = not left.visible
    right.visible = not right.visible
    if left.visible:
        b.text = "Hide traveling waves"
    else:
        b.text = "Show traveling waves"

button(text="Restart", bind=reset)

scene.append_to_caption("      ")

button(text="Hide traveling waves", bind=B_Showbutton)

scene.append_to_caption("      A standing wave can result from the interference of two traveling waves.")

reset(None)

while True:
    left.origin.x = xleft
    right.origin.x = xright
    xleft += dx
    xright -= dx
    if xleft > 0:
        xleft -= lamb
    if xright < -lamb:
        xright += lamb
    i = 0
    for x in arange(0,10*lamb+3*dx/2,dx):
        yleft = yright = 0
        if x < xleft+12*lamb:
            yleft = left.point(int(round((x-xleft)/dx))).pos.y
        if x > xright:
            yright = right.point(int(round((x-xright)/dx))).pos.y
        wave.modify(i, y=yleft+yright)
        i += 1
    rate(100)
    
    
    
