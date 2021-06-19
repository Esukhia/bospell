from typing import List

from symspellpy import SymSpell, Verbosity

from ..config import Config
from . import CandidateModelBase


class SymSpellModel(CandidateModelBase):
    """
    Candidate model based on symspell algorithm.
    https://github.com/wolfgarbe/SymSpell
    """

    def __init__(
        self,
        verbosity: Verbosity = Verbosity.CLOSEST,
        max_edit_distance: int = 2,
        config: Config = Config(),
    ):
        self.sym_spell = SymSpell()
        self.verbosity = verbosity
        self.max_edit_distance = max_edit_distance
        self.config = config
        self.load_dictionary()

    def load_dictionary(self):
        if not self.config.DICTIONARY_PATH.is_file():
            raise FileNotFoundError("Dictionary doesn't exists")
        self.sym_spell.load_dictionary(
            self.config.DICTIONARY_PATH, term_index=0, count_index=1
        )

    def get_candidates(self, word: str) -> List[str]:
        suggestions = self.sym_spell.lookup(
            word, self.verbosity, max_edit_distance=self.max_edit_distance
        )
        suggested_words = []
        for i, suggestion in enumerate(suggestions):
            if i > 5:
                break
            suggested_words.append(suggestion.term)
        return suggested_words
