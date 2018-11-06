GlowScript 2.7 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

R = 4e11
scene.background = color.white
scene.width = scene.height = 700
scene.range = 2.5*R

scene.caption = """Right button drag or Ctrl-drag to rotate "camera" to view scene.
Middle button or Alt-drag to drag up or down or scroll wheel to zoom in or out.
  On a two-button mouse, middle is left + right.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

s1 = sphere(pos=vector(0,R,0), radius=1e10, color=color.magenta, make_trail=True)
s2 = sphere(pos=vector(0,-R,0), radius=1e10, color=color.blue, make_trail=True)
s3 = sphere(pos=vector(2*R,0,0), radius=1e10, color=color.green, make_trail=True)
s1.m = 5e30
s2.m = 5e30
s3.m = 5e30*1e-1
G = 6.7e-11
v = sqrt(G*s1.m/(4*R))
s1.p = s1.m*vector(0,0,-v)
s2.p = s2.m*vector(0,0,v)
s3.p = vector(0,0,0)
dt = 60*1000
t = 0
while True:
    rate(200)
    r21 = s2.pos - s1.pos
    F21 = -norm(r21)*G*s1.m*s2.m/mag(r21)**2
    r32 = s3.pos - s2.pos
    F32 = -norm(r32)*G*s3.m*s2.m/mag(r32)**2
    r31= s3.pos - s1.pos
    F31 = -norm(r31)*G*s3.m*s1.m/mag(r31)**2
    s3.p = s3.p + (F32+F31)*dt
    s2.p = s2.p + (F21-F32)*dt
    s1.p = s1.p + (-F21-F31)*dt
    s1.pos = s1.pos + (s1.p/s1.m)*dt
    s2.pos = s2.pos + (s2.p/s2.m)*dt
    s3.pos = s3.pos + (s3.p/s3.m)*dt
    t = t+dt
    
    
    
    


