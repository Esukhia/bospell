from bospell.particle import get_particles_for_string, get_particle_type
from bospell.config import ParticlesConfig




def test_particle():
    pt = ParticlesConfig()
    
    string1 = "འདུག"
    particle_dic1 = get_particles_for_string(string1)
    
    string2 = "བསྟནད་"
    particle_dic2 = get_particles_for_string(string2)
    
    string3 = "དུ་"
    particle_dic3 = get_particles_for_string(string3)
    
    # assert particle_dic1 == pt.jes_jug_particles["ག"]
    assert particle_dic2 == pt.yang_jug_particles
    assert particle_dic3 == pt.tha_may_particles
    
    
if __name__ == "__main__":
    test_particle()