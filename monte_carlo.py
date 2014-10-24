
#Alternative energy functions can be imported here
import energy_function
from random import randint, random
from math import exp

def run_monte_carlo(density, T, iterations):
    #Check density is > 0
    if sum(density) <= 0:
        raise Exception("Must have positive density!")

    #Check no bins with negative particles
    neg_parts = False
    for item in density:
        if item <0:
            neg_parts = True
    if neg_parts == True:
        raise Exception("Can't have negative particle number")

    for x in range(iterations):
        #Move a particle left or right
        new_density = move_random_particle(density)
        #Compute old and new energys
        energy = energy_function.energy(density)
        energy_new = energy_function.energy(new_density)
        #If second is lower accept move. If higher, accept with a given probability
        if energy_new < energy:
            density=new_density[:]
        else:
            p0 = compute_boltzman(energy,energy_new,T)
            p1 = random()
            if p0 > p1:
                density=new_density[:]

        return density



def move_random_particle(density):
    #find number of particles
    number_particles = sum(density)
    
    bin_filled = False
    while bin_filled != True:
        #pick a random particle
        random_particle = randint(1,number_particles)

        #find container that holds this particle
        random_particles_bin = find_particles_bin(density,random_particle)

        #Check there are particles in that container
        if density[random_particles_bin] > 0:
            bin_filled = True
    
    #move this particle left or right with equal probability
    new_density = density[:]
    new_density[random_particles_bin] -= 1
    
    if random() > 0.5:
        new_index = (random_particles_bin+1) % len(density)
        new_density[new_index] +=1
    else:
        new_index = (random_particles_bin-1) % len(density)
        new_density[new_index] +=1
        
    return new_density
    
def find_particles_bin(density, particle_number):
    particle_counter = 0
    for index, index_density in enumerate(density):
        particle_counter += index_density
        if particle_counter >= particle_number:
            return index

def compute_boltzman(energy,energy_new,T):
    p0 = exp(-(energy_new-energy)/T)
    return p0
          




