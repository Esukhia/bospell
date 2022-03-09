import importlib
from pathlib import Path


def load_class(path):
    path_splited = path.split(".")
    module_path = ".".join(path_splited[:-1])
    class_name = path_splited[-1]
    cls = getattr(importlib.import_module(module_path), class_name)
    return cls


def mkdir(path: Path):
    path.mkdir(exist_ok=True, parents=True)
    return path
