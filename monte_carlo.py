def energy(density, coeff=1.0):
	energy =0
	for number in density:
		energy = energy + number*(number-1)
	return energy*coeff/2

def move_random_particle(density):
	array_items = arra
