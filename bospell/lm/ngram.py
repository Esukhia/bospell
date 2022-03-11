import logging
import math
import pickle
from pathlib import Path

from nltk.lm import KneserNeyInterpolated
from nltk.util import ngrams as get_ngrams

from bospell.config import DefaultConfig
from bospell.utils import mkdir

from .dataset import NGramDataset

LM_PATH = mkdir(DefaultConfig.base_path / "lm")


class NGramLM:
    def __init__(self, n: int = 3):
        self.n = n
        self.model = KneserNeyInterpolated(n)
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
        # TODO: set self.n from self.model
        self.n = self.model.order

    def evaluate_sentence(self, sentence: str):
        """check the prob. of `sentence`"""
        tokens = NGramDataset.preprocess_sentence(sentence, self.n)
        ngrams = list(get_ngrams(tokens, self.n))
        total_logscore = 0
        for ngram in ngrams:
            cur_logscore = self.model.logscore(ngram[-1], ngram[:-1])
            total_logscore += cur_logscore
        return math.exp(total_logscore)

    def predict_next(self):
        pass


def train_ngram(train_path, n, **kwargs) -> NGramLM:
    dataset = NGramDataset(n)
    dataset.load_train(train_path)
    ngram_lm = NGramLM(n=n)
    ngram_lm.train(dataset, **kwargs)
    return ngram_lm
