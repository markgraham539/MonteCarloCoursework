
# coding: utf-8

# In[121]:

#Alternative energy functions can be imported here
import energy_function
from random import randint, random
from math import exp


density=[0,9,2,1,6]
T=200
iter = 5
for x in range(iter):
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

    #Plot density at this iteration
    
    print density



def move_random_particle(density):
    #find number of particles
    number_particles = sum(density)
    
    #pick a random particle
    random_particle = randint(1,number_particles)
    
    #find container that holds this particle
    random_particles_bin = find_particles_bin(density,random_particle)
    
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
    p0 = exp(-(energy-energy_old)/T)
    return p0
          
#def determine_acceptance():
#def plot_density():


# In[113]:




# In[42]:




# In[12]:




# In[34]:




# In[34]:




# In[34]:




# In[34]:




# In[34]:




# In[34]:




# In[ ]:



