from pathlib import Path

from bospell.lm.ngram import train_ngram

DATA_PATH = Path(__file__).parent / "data"


def test_train_ngram():
    train_file = DATA_PATH / "train.txt"
    n = 3

    ngram_lm = train_ngram(train_file, n)

    assert ngram_lm.model.vocab
