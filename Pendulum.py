GlowScript 2.7 VPython

gravity=vector(0,-9.8,0)

velocity=vector(3,0,0)

length=8

rope = cylinder(pos=vector(0,length,0), axis=vector(0,-length,0), radius=0.05, color=vector(1,0,0), length=8)

mass = sphere(radius=1, color=vector(0,1,0), pos=vector(0,rope.pos.y-length,0))

ceiling = box(size=vector(10,0.1,10), color=vector(1,1,1), pos=vector(0,8.1,0))

dt=0.01

for i in range(100000):
    rate(300)
    
    velocity.x=velocity.x+mass.pos.x/length*gravity.y*dt
    
    mass.pos.x=mass.pos.x+velocity.x*dt
    
    mass.pos.y=length*(1-sqrt(1-(mass.pos.x/length)**2.0))
    
    x=mass.pos.x
    
    y=mass.pos.y
    
    mass.pos=vector(x,y,0)
    
    rope.axis=vector(x,y-length,0)
    
    
    
    
