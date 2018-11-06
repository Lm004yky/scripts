GlowScript 2.7 VPython

s1=sphere (pos=vector(0,6,0), color=vector(1,0,0), make_trail=True)

s2=sphere (pos=vector(0,2,0), color=vector(0,1,0), make_trail=True)

s3=sphere (pos=vector(0,-6,0), color=vector(1,1,0), make_trail=True)

for i in range (1000):
    rate (160)
    
    x=i/100.0
    y1=2*sin(2*pi*i/200)
    y2=2*sin(2*pi*i/200+pi)
    
    y3=y1+y2
    
    z=0
    
    s1.pos=vector(x,6+y1,z)
    s2.pos=vector(x,2+y2,z)   
    s3.pos=vector(x,-6+y3,z)
    
    
    
