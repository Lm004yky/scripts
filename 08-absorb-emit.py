GlowScript 2.7 VPython

# Written by Bruce Sherwood, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Excitation of atoms by electron beam
# March 2003

# number of discrete energy levels
Nlevels = 5 
# electron beam energy (Nlevels-1 corresponds to top level)
Eexcite = 3 
# If Eexcite < Nlevels-1, upper levels are not excited
# energy levels measured up from ground state
Eset = [0,2.8,4,4.7,5] 
# number of atoms
Natoms = 30 

scene.width = 600
scene.height = 600
scene.background = color.white
scene.userzoom = scene.userspin = False
# number of possible photon emission lines
Nlines = Eexcite*(Eexcite+1)/2 
greyintensity = 0.8
grey = vector(greyintensity,greyintensity,greyintensity)
# sets scale of display
Escale = 1 
L = Nlevels*Escale
# radius of horizontal line representing an energy level
Rlevel = Escale/30
# radius of atom
Ratom = Escale/10 
# list of energy level lines
levels = [] 
for N in range(Nlevels):
    levels.append(cylinder(pos=vector(-L/2,Eset[N]*Escale,0), axis=vector(L,0,0), radius=Rlevel, color=grey))
# list of atoms
atoms = [] 
# list of already-emitted photons that have been displayed in spectrum
photons = [] 
# spectrum displayed in rectangle bounded by (sx1,sy1) and (sx2,sy2)
sx1 = -L/2 
sx2 = -sx1
sy1 = levels[0].pos.y-2*Escale
sy2 = sy1+Escale
# display energy emitted as photon
emitarr = arrow(visible=False, shaftwidth=2*Ratom) 
# display energy absorbed from electron beam
absorbarr = arrow(visible=False, shaftwidth=2*Ratom, color=grey)

# Currently the GlowScript version of label ignores new lines.
beamon1 = 'Electron beam is on. Click to excite an atom or emit a photon.'
beamon2 = 'Build up spectrum of emitted photons.'
beam = label(pos=vector(0,levels[0].pos.y-0.4*Escale,0), box=0, text=beamon1, color=color.black, opacity=0)
beam2 = label(pos=vector(0,levels[0].pos.y-0.62*Escale,0), box=0, text=beamon2, color=color.black, opacity=0)
beamoff = 'Electron beam is off. Eventually all atoms will end up back in the ground state.'
beam.on = True

# convert photon energy to color (hue)
def Ecolor(Ephoton): 
    Erange = levels[-1].pos.y-levels[0].pos.y
    hue = (5/6)*Ephoton/Erange
    return color.hsv_to_rgb(vector(hue,1,1))
    
# atom has energy level, can absorb energy from electron beam or emit photon
class atom: 
    def __init__(self,x,energy):
        self.ball = sphere(pos=vector(x,0,0), radius=Ratom, color=color.yellow)
        self.__E = energy
    def getE(self):
        return self.__E
    def setE(self,energy):
        self.__E = energy
        self.ball.pos.y = levels[energy].pos.y
    def emit(self,Efinal):
        Einitial = self.getE()
        Ephoton = levels[Einitial].pos.y-levels[Efinal].pos.y
        emitarr.pos = self.ball.pos
        self.setE(Efinal)
        emitarr.axis = self.ball.pos-emitarr.pos
        emitarr.color = Ecolor(Ephoton)
        emitarr.visible = True
        for photon in photons:
            if Ephoton == photon.E: return
        Erange = levels[-1].pos.y-levels[0].pos.y
        x1 = sx1+(sx2-sx1)*Ephoton/Erange
        photons.append(box(pos=vector(x1,(sy1+sy2)/2,0), size=vector(Ratom,sy2-sy1,0.01), color=Ecolor(Ephoton), E=Ephoton))
    def absorb(self,Efinal):
        absorbarr.pos = self.ball.pos
        self.setE(Efinal)
        absorbarr.axis = self.ball.pos-absorbarr.pos
        absorbarr.visible = True

def randint(start, end):
    R = round(end - start)
    return int(round(start + R*random()))

scene.range = 4*Escale
scene.center = vector(0,(sy1+levels[-1].pos.y)/2,0)
# put all atoms in ground state initially
for N in range(Natoms): 
    atoms.append(atom(-L/2+(N+1)*L/(Natoms+1),0))

scene.waitfor('click')
while True:
    action = False
    # randomly choose one of the atoms
    Na = randint(0,Natoms-1)
    aa = atoms[Na]
    # If in ground state, and not all emission lines have been displayed yet,
    #   absorb energy from electron beam:
    if aa.getE() == 0 and len(photons) < Nlines:
        aa.absorb(randint(1,Eexcite))
        # show arrow indicating absorption of energy
        action = True
        scene.waitfor('click')
        absorbarr.visible = 0
    # randomly choose one of the atoms
    Na = randint(0,Natoms-1) 
    aa = atoms[Na]
    # If in excited state, emit a photon:
    if aa.getE() > 0:
        # randomly choose a lower energy level
        Efinal = randint(0,aa.getE()-1) 
        aa.emit(Efinal)
        # show arrow indicating photon emission
        action = True
        scene.waitfor('click') 
        emitarr.visible = False
    if len(photons) == Nlines and beam.on:
        beam.on = False
        beam2.visible = False
        beam.text = beamoff
        action = True
        scene.waitfor('click')
    if not action: scene.waitfor('click')
    
    
    
