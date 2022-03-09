import logging
import pickle
from pathlib import Path

from botok import WordTokenizer
from nltk.lm import MLE

from bospell.config import DefaultConfig
from bospell.utils import mkdir

from .dataset import NGramDataset

LM_PATH = mkdir(DefaultConfig.base_path / "lm")


def tokenize(text):
    wt = WordTokenizer()
    return [token.text for token in wt.tokenize(text)]


class NGramLM:
    def __init__(self, n: int = 3):
        self.n = n
        self.model = MLE(n)
        self.model_path = LM_PATH / f"{n}_gram.model"

    def train(self, dataset: NGramDataset, save=True):
        self.model.fit(dataset.train, dataset.vocab)
        if save:
            pickle.dump(self.model, self.model_path.open("wb"))
            logging.info(f"ngram model saved at: {self.model_path}")

    def load_model(self, path: Path = None):
        if path:
            if path.is_file():
                self.model_path = path
            else:
                logging.exception(f"ngram model doesn't exits at: {path}")
        self.model = pickle.load(self.model_path.open("rb"))

    def evaluate_sentence(self, sentence: str):
        tokens = tokenize(sentence)

    def predict_next(self):
        pass


def train_ngram(train_path, n, **kwargs) -> NGramLM:
    dataset = NGramDataset(n)
    dataset.load_train(train_path)
    ngram_lm = NGramLM(n=n)
    ngram_lm.train(dataset, **kwargs)
    return ngram_lm
