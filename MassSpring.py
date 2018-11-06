GlowScript 2.7 VPython

spring = helix(pos=vector(0,8,0), axis=vector(0,-8,0), radius=1,color=vector(1,0,0), thickness=0.3)

mass = box(size=vector(3,3,3), color=vector(0,1,0), pos=vector(0,-1.5,0))

ceiling = box(size=vector(10,0.1,10), color=vector(1,1,1), pos=vector(0,8.1,0))

for i in range(100000):
    rate(300)
    
    spring.axis=vector(0,-8+6*sin(2*pi*i/1000.0),0)
    
    mass.pos=vector(0,-1.5+6*sin(2*pi*i/1000.0),0)    
    
    
