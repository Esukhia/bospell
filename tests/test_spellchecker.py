from bospell import BoSpell


def test_candidates():
    spell = BoSpell()
    candidates = spell.candidates("ཤི")
    assert candidates
