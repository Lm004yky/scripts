GlowScript 2.7 VPython

spring = helix(pos=vector(-5,1+0.1-3,0), axis=vector(5,0,0), radius=0.7, color=vector(1,1,0), thickness=0.2)

mass = box(size=vector(2,2,2), color=vector(0,1,0), pos=vector(1,1-3,0))

ceiling = box(size=vector(10,0.1,10), color=vector(1,1,1), pos=vector(0,0-3,0))

wall = box(size=vector(0.1,10,10), color=vector(1,1,1), pos=vector(-5,5-3,0))

for i in range(100000):
    rate(300)
    
    spring.axis=vector(5+3*sin(2*pi*i/1000.0),0,0)
    
    mass.pos=vector(1+3*sin(2*pi*i/1000.0),1-3,0)    
    
    
    
