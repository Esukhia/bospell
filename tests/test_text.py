from bospell.text import Text


def test_text_correct():
    text = Text("བཀྲ་ཤིས་བདེ་ལེག།")
    text.correct()
    assert text.suggestions
