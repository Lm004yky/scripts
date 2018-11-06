GlowScript 2.7 VPython

# Written by Bruce Sherwood, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Fall 2000
# Major rewrite March 2015 to work either in classic or GlowScript environment

s = """SPEED OF SOUND IN A SOLID
Propagation of a disturbance along a line of atoms connected by spring-like forces.
The interatomic spring stiffness is set to 16 N/m for aluminum or 5 N/m for lead.
COMPUTATIONAL MODEL
The spring-like forces between neighboring atoms are calculated based on their positions.
Next, these forces are used to update the momenta of all the atoms in a time dt.
The final velocities are used to update the positions of all the atoms in the time dt.
Then we repeat the process with the new positions and momenta.
The first and last atoms are fixed and cannot move."""

if version[1] == 'glowscript':
    scene.caption = s
    rangefactor = 0.45
else:
    print(s)
    rangefactor = 0.6

sw = scene.width = 800
sh = scene.height = 600
scene.userspin = scene.userzoom = False
scene.background = color.white
gray = color.gray(0.5)

def Eformat(x, f=2): # f = digits after decimal point
    f = abs(f)
    s = ''
    if x < 0:
        s = '-'
        x = -x
    L = log(x)/log(10) # currently GlowScript does not have the log10 function
    expon = int(L)
    mantissa = L - expon
    num = 10**mantissa
    if s == '-' or expon < 0:
        expon -= 1
        num *= 10
    if f == 0:
        num = int(num)
    else:
        factor = 10**f
        num = round(factor*num)/factor
    snum = str(num)
    while len(snum) < f+2:
        snum += '0'
    return s+snum+'E'+str(expon)

def makeinvisible(axis, disp, atoms, ticks, labels):
    axis.visible = False
    disp.visible = False
    for atom in atoms:
        atom.visible = False
    for tick in ticks:
        tick.visible = False
    for lab in labels:
        lab.visible = False
        
props = {'Al': {'m': 27e-3/6e23,  'ks': 16, 'd': (1/2.7e-3)**(1/3)*0.01},
         'Pb': {'m': 207e-3/6e23, 'ks':  5, 'd': (1/11.6e-3)**(1/3)*0.01} }
for metal in props:
    props[metal]['d'] = props[metal]['d']*props[metal]['m']**(1/3)
dt = 2*pi*sqrt(props['Al']['m']/props['Al']['ks'])/30
dAl = props['Al']['d']
maxstate = 3
state = 3
ret = 'Next'

def setstate(s):
    if ret == 'Next': s += 1
    elif ret == 'Back': s -= 1
    else: s -= 1
    if s < 0: s = maxstate
    if s > maxstate: s = 0
    return s

clickpos = None
def getclick():
    global clickpos
    clickpos = scene.mouse.pos

scene.bind("click", getclick)
bound = True
instruct = label(box=0, color=color.black)

while True:
    state = setstate(state)
    if state == 0:
        N = 10
        scene.range = rangefactor*(N+2)*dAl
        instruct.pos = vector(0.5*(N+2)*dAl,0.3*(N+2)*dAl,0)
        instruct.text = 'Click an atom to displace it.'
        instruct.visible = True
        metal = 'Al'
        showcurve = False
        atomcolor = color.blue
        cradius = 0
        if bound:
            scene.unbind("click", getclick)
            bound = False
    elif state == 1:
        N = 10
        scene.range = rangefactor*(N+2)*dAl
        instruct.pos = vector(0.5*(N+2)*dAl,0.2*(N+2)*dAl,0)
        instruct.text = 'Click an atom to displace it. Displacements of atoms are plotted vertically.'
        instruct.visible = True
        metal = 'Al'
        showcurve = True
        atomcolor = color.blue
        cradius = 0
        if version[1] == 'glowscript':
            cradius = 0.01*dAl
        if bound:
            scene.unbind("click", getclick)
            bound = False
    elif state == 2:
        N = 100
        scene.range = rangefactor*N*dAl
        instruct.pos = vector(0.5*100*dAl,70*dAl,0)
        instruct.text = 'Click an atom to displace it, then click anywhere when the pulse reaches the right end.'
        instruct.visible = True
        metal = 'Al'
        showcurve = True
        atomcolor = color.blue
        cradius = 0
        if version[1] == 'glowscript':
            cradius = 0.1*dAl
        if not bound:
            scene.bind("click", getclick)
            bound = True
    elif state == 3:
        length = 100*dAl
        scene.range = rangefactor*N*dAl
        N = int(length/props['Pb']['d'])
        instruct.pos = vector(0.5*100*dAl,70*dAl,0)
        instruct.text = 'Click an atom to displace it, then click anywhere when the pulse reaches the right end.'
        instruct.visible = True
        metal = 'Pb'
        showcurve = True
        atomcolor = color.green
        cradius = 0
        if version[1] == 'glowscript':
            cradius = 0.1*dAl
        if not bound:
            scene.bind("click", getclick)
            bound = True

    d = props[metal]['d'] # inter-nuclear distance
    m = props[metal]['m'] # mass of one atom
    ks = props[metal]['ks'] # effective stiffness of interatomic "spring" force
    dxinitial = 0.3*d # initial displacement of touched atom
    sy = ((N+2)*d)*(sh/sw) # height of canvas in world coordinates
    yoffset = d+(sy-d)/2# location of curve centerline
    axis = curve(pos=[vector(0,yoffset,-d/10), vector((N+1)*d,yoffset,-d/10)], radius=cradius, color=gray, visible=showcurve)
    scale = 2*((sy-d)/2)/dxinitial # scale up graph of displacements
    if N <= 10:
        scale = scale/2

    disp = curve(color=color.blue, radius=cradius, visible=showcurve)
    for nn in range(N+2):
        disp.append(pos=vector(nn*d,yoffset,0))
    atoms = []
    ticks = []
    for nn in range(N+2): # movable masses from 1 to N; end atoms fixed
        atoms.append(sphere(pos=vector(nn*d,0.5*d,0), radius=0.5*d, color=atomcolor, id=nn))
        atoms[nn].p = vector(0,0,0)
        if N <= 10:
            if not (nn == 0 or nn == (N+1)):
                ticks.append(curve(pos=[vector(nn*d,1.1*d,0),vector(nn*d,1.5*d,0)], color=gray))
    atoms[0].color = gray
    atoms[N+1].color = gray
    
    labels = [None,None,None,None,instruct]
    labels[0] = label(pos=atoms[0].pos+vector(0,d/2.,0), text='Back', yoffset=10, box=0, line=0, opacity=0, color=color.black, visible=(state>0))
    labels[1] = label(pos=atoms[N+1].pos+vector(0,d/2.,0), text='Next', yoffset=10, box=0, line=0, opacity=0, color=color.black)
    s = str(N)+' '+metal+' atoms, '+Eformat((N+1)*d)+' m'
    labels[2] = label(pos=vector(0.4*(N+1)*d,d/2,0), yoffset=10, height=20, text= s, visible=0, box=0, line=0, opacity=0, color=color.black)
    labels[3] = label(pos=vector(0.8*N*d,d/2,0),text='t = 0', yoffset=10, height=20, visible=0, box=0, line=0, opacity=0, color=color.black)
    
    if N > 10:
        labels[2].visible = True
        labels[3].visible = True
    if showcurve:
        scene.center = vector((N+1)*d/2,sy/2,0)
    else:
        scene.center = vector((N+1)*d/2,0,0)

    ret = None
    while True:
        # watch for clicking an atom to displace it
        scene.waitfor('click')
        picked = scene.mouse.pick
        if picked:
            ith = picked.id
            # clicked an end atom
            if ith == 0 or ith == N+1:
                if ith == 0 and state == 0: continue
                makeinvisible(axis, disp, atoms, ticks, labels)
                if ith == 0:
                    ret = 'Back'
                    break
                else:
                    ret = 'Next'
                    break
            atoms[ith].pos.x = ith*d+dxinitial
            atoms[ith].color = color.red
            if version[1] == 'glowscript':
                disp.modify(ith, y=yoffset+scale*dxinitial) # GlowScript
            else:
                disp.y[ith] = yoffset+scale*dxinitial # classic
            break

    if ret != None: continue
    t = 0
    clickpos = None

    # main loop; for N <= 10 click to advance, else free run
    if N <= 10:
        if state > 0:
            instruct.text = 'Click anywhere to advance, or click the atom below Next or Back.'
        else:
            instruct.text = 'Click anywhere to advance, or click the atom below Next.'
    else:
        instruct.text = 'Click to stop when the pulse reaches the right end.'
    while True: 
        if N <= 10:
            scene.waitfor('click')
            picked = scene.mouse.pick
            if picked:
                ith = picked.id
                if (ith == 0 and state > 0) or ith == N+1:
                    if ith == 0 and state == 0: continue
                    makeinvisible(axis, disp, atoms, ticks, labels)
                    if ith == 0:
                        ret = 'Back'
                        break
                    else:
                        ret = 'Next'
                        break
        else:
            rate(100)
            if clickpos:
                ret = 'Stop'
                clickpos = None
                break

######## THE HEART OF THE COMPUTATION ###########  
        for nn in range(1, N+1):
            Fright = ks*(atoms[nn+1].pos.x-atoms[nn].pos.x-d) # force exerted by atom to right
            Fleft = -ks*(atoms[nn].pos.x-atoms[nn-1].pos.x-d) # force exerted by atom to left
            atoms[nn].p.x = atoms[nn].p.x+(Fright+Fleft)*dt # update momentum

        for nn in range(1, N+1): # after updating all momenta, update positions
            atoms[nn].pos.x = atoms[nn].pos.x+(atoms[nn].p.x/m)*dt
            if version[1] == 'glowscript':
                disp.modify(nn, y=yoffset+scale*(atoms[nn].pos.x-nn*d)) # GlowScript
            else:
                disp.y[nn] = yoffset+scale*(atoms[nn].pos.x-nn*d) # classic

        t = t+dt
        s = 't = '+Eformat(t)+' s'
        labels[3].text = s
##################################################

    if ret != 'Stop': continue
    ret = 'Next'
    if metal == 'Al':
        element = 'aluminum'
        speed = '4800'
    else:
        element = 'lead'
        speed = '1200'
        
    if N > 10:
        dist = (N-ith)*d
# speed of sound
        s = 'dist. = '+Eformat(dist)+' m\nv = '+str(int(dist/t))+' m/s'
        arr = arrow(pos=vector(atoms[ith].pos.x,0.1*N*d,0), axis=vector(atoms[N].pos.x-atoms[ith].pos.x,0,0), shaftwidth=d, color=color.cyan)
        report = label(pos=arr.pos+0.5*arr.axis+vector(0,3*dAl,0), height=20, yoffset=15, text=s, box=0, line=0, opacity=0, color=color.black)
        instruct.text = 'The measured value for the speed of sound in '+element+' is '+speed+' m/s.\nClick anywhere to proceed, or click the atom below Back.'
        scene.waitfor('click')
        arr.visible = 0
        report.visible = 0
        picked = scene.mouse.pick
        if picked:
            ith = picked.id
            if ith == 0 or ith == N+1:
                makeinvisible(axis, disp, atoms, ticks, labels)
                if ith == 0: ret = 'Back'
                else: ret = 'Next'   
    makeinvisible(axis, disp, atoms, ticks, labels)
    
    
    
    
    
    
