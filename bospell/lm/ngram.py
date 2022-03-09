from pathlib import Path

from nltk.lm import MLE

from .dataset import NGramDataset


class NGramLM:
    def __init__(self, n: int = 3, trained_model: MLE = None):
        if trained_model:
            self.model = trained_model
        else:
            self.model = MLE(n)

    def train(self, dataset: NGramDataset):
        self.model.fit(dataset.train, dataset.vocab)

    def evaluate_sentence(self, sent: str):
        pass

    def predict_next(self):
        pass


def train_ngram(train_path, n) -> NGramLM:
    dataset = NGramDataset(n)
    dataset.load_train(train_path)
    ngram_lm = NGramLM(n=n)
    ngram_lm.train(dataset)
    return ngram_lm
