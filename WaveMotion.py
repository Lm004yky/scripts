GlowScript 2.7 VPython

s=sphere (pos=vector(0,0,0), color=vector(1,1,0), make_trail=True)

for i in range (1000):
    rate (160)
    
    x=i/10.0
    y=4*sin(2*pi*i/100.0)
    z=0
    
    s.pos=vector(x,y,z)
    
    
    
    
