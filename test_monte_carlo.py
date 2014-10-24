import monte_carlo

def test_move_particle_simple():
	density = [1];
	moved_density = monte_carlo.move_random_particle(density)
	assert moved_density == density

def test_move_particle_does_something():
	density = [1,2,5,5]
	moved_density = monte_carlo.move_random_particle(density)
	assert moved_density != density

def test_moved_particle_conserves_particles():
	density = [0,2,4,5]
	moved_density = monte_carlo.move_random_particle(density)
	assert sum(moved_density) == sum(density)

def test_find_particles_bin():
	density = [1]
	assert monte_carlo.find_particles_bin(density,1) == 0

def test_find_particles_bin_end():
	density = [1,7,8,9]
	assert monte_carlo.find_particles_bin(density,25) == 3

def test_boltzman():
	assert monte_carlo.compute_boltzman(3,3,100)==1

def test_positive_density():
	from nose.tools import assert_raises
	density = [0]
	with assert_raises(Exception) as exception:
		monte_carlo.run_monte_carlo(density,10,1)