GlowScript 2.7 VPython

sun=sphere(pos=vector(0,0,0), color=color.yellow, radius=0.8)

mercury=sphere(pos=vector(3,0,0), color=color.white, radius=0.15, make_trail=True)

venus=sphere(pos=vector(5,0,0), color=color.green, radius=0.25, make_trail=True)

earth=sphere(pos=vector(7,0,0), color=color.blue, radius=0.3, make_trail=True)

mars=sphere(pos=vector(10,0,0), color=color.red, radius=0.2, make_trail=True)

for i in range(1000):
    rate (10)
    
    y=sin(2*pi*i/100)
    x=cos(2*pi*i/100)
    
    mercury.pos=vector(3*x,3*y,0)
    
    venus.pos=vector(5*x,5*y,0)
    
    earth.pos=vector(7*x,7*y,0)
    
    mars.pos=vector(10*x,10*y,0)
    
    
    
