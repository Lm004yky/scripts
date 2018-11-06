GlowScript 2.7 VPython

sun=sphere(pos=vector(0,0,0), color=color.yellow, radius=0.8)

mercury=sphere(pos=vector(3,0,0), color=color.white, radius=0.15, make_trail=True)

venus=sphere(pos=vector(5,0,0), color=color.green, radius=0.25, make_trail=True)

earth=sphere(pos=vector(7,0,0), color=color.blue, radius=0.3, make_trail=True)

mars=sphere(pos=vector(10,0,0), color=color.red, radius=0.2, make_trail=True)

for i in range(1000):
    rate (60)
    
    mercury.rotate (angle=0.04, axis=vector(0,0.2,1), origin=vector(0,0,0))
    
    venus.rotate (angle=0.03, axis=vector(0,0,1), origin=vector(0,0,0))
    
    earth.rotate (angle=0.02, axis=vector(0,0,1), origin=vector(0,0,0))
    
    mars.rotate (angle=0.01, axis=vector(0,0,1), origin=vector(0,0,0))
    
    
    
