from bospell.config import ParticlesConfig
from bospell.utils import parse_syl

def get_last_character_type(syl_parts):
    if syl_parts['yang_jug'] != "":
        return "yang_jug"
    elif syl_parts['jes_jug'] != "":
        return "jes_jug"
    else:
        return None

def get_particles_for_string(last_syl):
    pt = ParticlesConfig()
    syl_parts = parse_syl(last_syl)
    if syl_parts:
        last_syl_part = get_last_character_type(syl_parts)
        if last_syl_part:
            character = syl_parts[last_syl_part]
            if last_syl_part == "yang_jug":
                if syl_parts[last_syl_part] == "ད":
                    return pt.yang_jug_particles
            elif last_syl_part == "jes_jug":
                return pt.jes_jug_particles[character]
        else:
            return pt.tha_may_particles
   
def add_tsekdung(particle):
    particle_len = len(particle)
    if particle[particle_len-1] == "་":
        return particle
    else:
        return particle + "་"


def get_particle_type(particle):
    particle = add_tsekdung(particle)
    pt = ParticlesConfig()
    for part_type, particles in pt.particle_types.items():
        if particle in particles:
            return part_type
