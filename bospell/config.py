from pathlib import Path

from botok import WordTokenizer
from symspellpy.symspellpy import Verbosity


class Config:
    pass


class DefaultConfig(Config):
    DICTIONARY_PATH = (
        Path(__file__).parent / "resources" / "dictionaries" / "general.txt"
    )

    tokenizer_class = "bospell.tokenizers.BotokWordTokenizer"

    candidates_model_class = "bospell.candidates.symspell.SymSpellModel"
    verbosity: Verbosity = Verbosity.CLOSEST
    max_edit_distance: int = 2
