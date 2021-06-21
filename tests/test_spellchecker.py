from bospell import BoSpell


def test_candidates():
    spell = BoSpell()
    candidates = spell.candidates("བཀྲ་ཤིད་")
    assert candidates
