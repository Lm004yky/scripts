GlowScript 2.7 VPython

proton1=sphere(pos=vector(0,0,0.9), radius=1, color=vector(1,0,0))
proton2=sphere(pos=vector(0,1.1,0), radius=1, color=vector(1,0,0))
proton3=sphere(pos=vector(0.9,0,0), radius=1, color=vector(1,0,0))
proton4=sphere(pos=vector(-1.1,0,-0.5), radius=1, color=vector(1,0,0))

neutron1=sphere(pos=vector(0,-1.1,0.7), radius=1, color=vector(0.5,0.5,0.5))
neutron2=sphere(pos=vector(0.5,0,-1.1), radius=1, color=vector(0.5,0.5,0.5))
neutron3=sphere(pos=vector(0,0,1.1), radius=1, color=vector(0.5,0.5,0.5))
neutron4=sphere(pos=vector(0,0.9,0), radius=1, color=vector(0.5,0.5,0.5))
neutron5=sphere(pos=vector(1.1,0,-0.7), radius=1, color=vector(0.5,0.5,0.5))

electron1=sphere(pos=vector(10,0,0), radius=0.2, color=vector(0,1,1), make_trail=1)
electron2=sphere(pos=vector(0,10,0), radius=0.2, color=vector(0,1,1), make_trail=1)
electron3=sphere(pos=vector(-10,-10,0), radius=0.2, color=vector(0,1,1), make_trail=1)
electron4=sphere(pos=vector(10,-10,0), radius=0.2, color=vector(0,1,1), make_trail=1)

for i in range(100000):
    rate(300)
    x1=10*(cos(2*pi*i/1000.0))
    y1=10*(sin(2*pi*i/1000.0))
    electron1.pos=vector(x1,y1,0)

    y2=10*(cos(2*pi*i/1000.0))
    z2=10*(sin(2*pi*i/1000.0))
    electron2.pos=vector(0,y2,z2)

    x3=-10*(cos(2*pi*i/1000.0))
    y3=x3
    z3=10*(sin(2*pi*i/1000.0))/sin(pi/4.0)
    electron3.pos=vector(x3,y3,z3)

    x4=10*(cos(2*pi*i/1000.0))
    y4=-x4
    z4=10*(sin(2*pi*i/1000.0))*(-1.0)/sin(pi/4.0)
    electron4.pos=vector(x4,y4,z4)
    
    
    
    
    




    
        
