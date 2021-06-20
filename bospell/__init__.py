__version__ = "0.0.1"


from . import utils
from .candidates import CandidateModelBase
from .config import Config, DefaultConfig
from .tokenizers import TokenizerBase


class BoSpell:
    """
    The BoSpell class encapsulates the basics needed to accomplish a
    spell checking algorithm.

    Args:
        config (bospell.Config): Configuration class for bospell
    """

    def __init__(self, config: Config = DefaultConfig()):
        self.config = config
        self.tokenizer: TokenizerBase = utils.load_class(config.tokenizer_class)(config)
        self.candidates_model: CandidateModelBase = utils.load_class(
            config.candidates_model_class
        )(config=config)

    def candidates(self, word):
        return self.candidates_model.get_candidates(word)
