from pathlib import Path

from bospell.lm.dataset import NGramDataset

DATA_PATH = Path(__file__).parent / "data"


def test_ngram_dataset():
    dataset = NGramDataset()
    dataset.load_train(DATA_PATH / "train.txt")

    assert dataset.train
    assert dataset.vocab
