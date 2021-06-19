from bospell.candidates.symspell import SymSpellModel


def test_get_candidates():
    symspell_model = SymSpellModel()
    candidates = symspell_model.get_candidates("ཤི")
    assert candidates
