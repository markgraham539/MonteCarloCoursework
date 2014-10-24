
# coding: utf-8

# In[26]:

def energy(density, coeff=1.0):
    energy =0
    for number in density:
        energy = energy + number*(number-1)
    return energy*coeff/2


