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
v0=4

def lighttime(gpoint):
  #this function takes a point on the surface
  #and then calculates the time it takes light to get there
  light=sphere(pos=p1.pos, radius=0.02, color=color.yellow,make_trail=True)
  
  aim=gpoint-p1.pos
  
  light.v=v0*norm(aim)
  thetai=acos(-light.v.y/v0)
  t=0
  dt=0.005
  while light.pos.y>=0:
    rate(200)
    light.pos=light.pos+light.v*dt
    t=t+dt
  aim=p2.pos-gpoint

  light.v=v0*norm(aim)

  #calculate angle of reflection
  thetar=acos(light.v.y/v0)

  #do this until the light gets back up to point 2
  while light.pos.y<=p2.pos.y:
    rate(200)
    #update the position of the light
    light.pos=light.pos+light.v*dt
    t=t+dt
  return(t,thetai,thetar)


#tgraph=graph(xtitle="Incident Angle [Deg]", ytitle="Light Time [s]", fast=False)
#f1=gcurve(color=color.blue)
x=0
dx=0.1

while (p1.pos.x+x)<=p2.pos.x:
  #calc time and angles
  temp=lighttime(vector(p1.pos.x+x,0,0))
  print("Incident = ", temp[1]*180/pi," Reflected =",temp[2]*180/pi," Time = ",temp[0]," s")
  #f1.plot(temp[1]*180/pi,temp[0])
  x=x+dx
