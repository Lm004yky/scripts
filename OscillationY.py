GlowScript 2.7 VPython

s=sphere(pos=vector(0,0,0), color=vector(0,1,0), radius=4)

for i in range(400):
    rate(30)
    
    position = 5*sin(2*pi*i/100)
    
    s.pos=vector(0, position, 0)
    
    
    
    
