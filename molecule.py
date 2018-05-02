import particle as p
import numpy as np
class Molecule:
    '''Stores and calculates information about diatomic molecules'''
    def __init__(self,pos1,pos2,m1,m2,L0,k):
        '''Creates a diatomic molecule with Particle 1 with initial (x,y) position = pos1 and mass = m1, Particle 2 with initial (x,y) position = pos2 and mass = m2, equilibrium length = L0, and spring constant = k.'''
        self.p1=p.Particle(pos1,m1)
        self.p2=p.Particle(pos2,m2)
        self.k=k
        self.L0=L0
    def __repr__(self):
        return "pos1: {self.pos1}, pos2: {self.pos2}, mass1: {self.m1}, mass2: {self.m2}, L0: {self.L0}, k = {self.k}".format(self=self)
    def get_displ(self):
        '''Returns displacement vector from Particle 1 to Particle 2'''
        return self.p2.pos - self.p1.pos
    def get_force(self):
        '''Returns force from spring on Particle 1'''
        displ = self.get_displ()
        return np.multiply(self.k,displ)