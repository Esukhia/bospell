from abc import ABC, abstractmethod

from botok import WordTokenizer


class TokenizerBase(ABC):
    """All tokenizer should be subclass of TokenizerBase."""

    @abstractmethod
    def tokenize(self, text):
        pass


class BotokWordTokenizer(TokenizerBase):
    def __init__(self, config):
        self.config = config
        self.tokenizer = WordTokenizer()

    def tokenize(self, text):
        return self.tokenizer.tokenize(text)
