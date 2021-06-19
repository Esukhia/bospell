from pathlib import Path


class Config:
    DICTIONARY_PATH = (
        Path(__file__).parent / "resources" / "dictionaries" / "general.txt"
    )
