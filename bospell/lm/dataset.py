from pathlib import Path
from typing import List

from botok import WordTokenizer, sentence_tokenizer
from nltk.lm.preprocessing import pad_both_ends, padded_everygram_pipeline


def sent_tokenize(text):
    wt = WordTokenizer()
    tokens = wt.tokenize(text)
    sentences = sentence_tokenizer(tokens)
    return [[token.text for token in sentence[1]] for sentence in sentences]


def tokenize(text):
    wt = WordTokenizer()
    return [token.text for token in wt.tokenize(text)]


class NGramDataset:
    """Dataset for N-Gram Language model"""

    def __init__(self, n: int = 3):
        self.n = n
        self.train: List[List] = None
        self.vocab = None
        self.test: List[List] = None

    def load_train(self, file_path: Path):
        tokenized_sentences = sent_tokenize(file_path.read_text())
        self.train, self.vocab = padded_everygram_pipeline(self.n, tokenized_sentences)

    @staticmethod
    def preprocess_sentence(sentence: str, n: int):
        tokens = tokenize(sentence)
        return pad_both_ends(tokens, n)
