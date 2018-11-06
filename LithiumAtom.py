GlowScript 2.7 VPython
proton1=sphere(pos=vector(0.9,0.4,0), radius=1, color=vector(1,0,0))
proton2=sphere(pos=vector(-0.9,-0.4,0), radius=1, color=vector(1,0,0))
proton3=sphere(pos=vector(0,0.9,0), radius=1, color=vector(1,0,0))
neutron1=sphere(pos=vector(0.9,-0.2,0.9), radius=1, color=vector(0.5,0.5,0.5))
neutron2=sphere(pos=vector(0.9,0.4,-0.9), radius=1, color=vector(0.5,0.5,0.5))
neutron3=sphere(pos=vector(-0.9,0.2,-0.9), radius=1, color=vector(0.5,0.5,0.5))
neutron4=sphere(pos=vector(-0.9,0.8,0.9), radius=1, color=vector(0.5,0.5,0.5))
electron1=sphere(pos=vector(10,0,0), radius=0.2, color=vector(0,1,1), make_trail=1)
electron2=sphere(pos=vector(0,10,0), radius=0.2, color=vector(0,1,1), make_trail=1)
electron3=sphere(pos=vector(-15,0,0), radius=0.2, color=vector(0,1,1), make_trail=1)
for i in range(100000):
    rate(300)
    x1=10*(cos(2*pi*i/1000))
    y1=10*(sin(2*pi*i/1000))
    electron1.pos=vector(x1,y1,0)
    y2=10*(cos(2*pi*i/1000))
    z2=10*(sin(2*pi*i/1000))
    electron2.pos=vector(0,y2,z2)
    x3=-15*(cos(2*pi*i/1000))
    z3=15*(sin(2*pi*i/1000))
    electron3.pos=vector(x3,0,z3)

    
    
