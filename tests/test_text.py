from bospell import Text


def test_text_correct():
    text = Text("བོད་པའི་བུ་བཀྲ་ཤིད་")
    corrected = text.corrected
    assert corrected == "བོད་པའི་བུ་བཀྲ་ཤིས"
