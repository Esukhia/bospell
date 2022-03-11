from pathlib import Path

from bospell.lm.ngram import NGramLM, train_ngram

DATA_PATH = Path(__file__).parent / "data"


def test_train_ngram():
    train_file = DATA_PATH / "train.txt"
    n = 3

    ngram_lm = train_ngram(train_file, n, save=False)

    assert ngram_lm.model.vocab


def test_save_model():
    train_file = DATA_PATH / "train.txt"
    n = 3

    ngram_lm = train_ngram(train_file, n)

    assert ngram_lm.model_path.is_file()


def test_load_model():
    train_file = DATA_PATH / "train.txt"
    n = 3
    train_ngram(train_file, n)

    ngram_lm = NGramLM()
    assert not ngram_lm.model.vocab

    ngram_lm.load_model()

    assert ngram_lm.model.vocab


def test_evaluate_sentence():
    ngram_lm = NGramLM()
    ngram_lm.load_model()

    prob = ngram_lm.evaluate_sentence("བྱང་ཆུབ་འདི་བརྙེས་དེ་ལ་ཕྱག་འཚལ་ལོ། །")

    assert prob
