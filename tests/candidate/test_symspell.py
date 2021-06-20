from bospell.candidates.symspell import SymSpellModel
from bospell.config import DefaultConfig


def test_get_candidates():
    symspell_model = SymSpellModel(config=DefaultConfig())
    candidates = symspell_model.get_candidates("ཤི")
    assert candidates
