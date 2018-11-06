GlowScript 2.7 VPython
#https://www.wired.com/story/model-how-light-reflects-off-a-mirror-with-python/
#Rhett Allain dot-physics 03.28.18 10:00 am
scene.userzoom=False
#starting point
#change this position for fun (but keep it above y = 0)
p1=sphere(pos=vector(-1.5,2,0), radius=0.07, color=color.red)

#ending point
#chnage this position - but keep above y=0
p2=sphere(pos=vector(1.5,1,0), radius=0.07, color=color.red)

#this is just the ground - don't worry about it
ground=box(pos=vector(0,-0.05,0), size=vector(3,0.1,.5))

#this creates the light ray
light=sphere(pos=p1.pos, radius=0.02, color=color.yellow, make_trail=True)

#this is the fake speed of light
v0=2

#this is the location on the surface that the light aims towards
groundpoint=vector(p1.pos.x+.6,0,0)
#this is a vector to figure out the direction of the velocity vector
aim=groundpoint-p1.pos

#set the velocity vector for the light
light.v=v0*norm(aim)

#calculate the angle of incidence
thetai=acos(-light.v.y/v0)

#time and time step
t=0
#you can make the time step smaller if it makes you happy
dt=0.01

#do this first part while the light is "above" the surface
while light.pos.y>=0:
    rate(100)
    #update the position of the light
    light.pos=light.pos+light.v*dt
    #update the time
    t=t+dt

#re-aim towards the second point
aim=p2.pos-groundpoint
#calculate the new velocity vector
light.v=v0*norm(aim)

#calculate angle of reflection
thetar=acos(light.v.y/v0)

#do this until the light gets back up to point 2
while light.pos.y<=p2.pos.y:
    rate(100)
    #update the position of the light
    light.pos=light.pos+light.v*dt
    t=t+dt

#print some stuff
print("Total time = ", t," s")
print("Angle of Incidence = ",thetai*180/pi," deg")
print("Angle of Relfection = ", thetar*180/pi," deg")
