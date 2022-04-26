from pathlib import Path

from symspellpy.symspellpy import Verbosity

from bospell.utils import mkdir
import json


class Config:
    pass


class DefaultConfig(Config):
    base_path = mkdir(Path.home() / ".bospell")
    tokenizer_class = "bospell.tokenizers.BotokWordTokenizer"

    # BoSpell components
    # ------------------

    # Candidates Model
    candidates_model_class = "bospell.candidates.symspell.SymSpellModel"
    DICTIONARY_PATH = (
        Path(__file__).parent / "resources" / "dictionaries" / "general.txt"
    )
    verbosity: Verbosity = Verbosity.CLOSEST
    max_edit_distance: int = 2

    # Error Model
    error_model_class = "bospell.error.NonWordErrorModel"
    
    
class ParticlesConfig(Config):
    base_path = mkdir(Path.home() / ".bospell")
    
    
    # particle
    particle_path = (
        Path(__file__).parent / "resources" / "particles.json"
    )
    particle_json = json.loads((particle_path).read_text(encoding='utf-8'))
    
    particle_types = particle_json['particle_types']
    jes_jug_particles = particle_json['jes_jug_particles']
    yang_jug_particles = particle_json['yang_jug_particles']
    tha_may_particles = particle_json['tha_may_particles']