# particle system
import time

class ParticleSystem():
    def __init__(self):
        self.G = 6.67430 * pow(10, -9) # -11
        self.t0 = time.time()
        
    def update_particle_positions(self, particle_list):
        a, b = particle_list[0], particle_list[1]
        rx = abs(a.x - b.x)
        ry = abs(a.y - b.y)
        t = time.time() - self.t0
        
        # implementation of physics equations
    
   