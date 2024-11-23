from abc import ABC, abstractmethod
from loguru import logger

class OutputDriver(ABC):
    name = None

    def __init__(self, *args, **kwargs):
        self.log = logger

    @abstractmethod
    def put(self, output: str):
        pass

    @abstractmethod
    def close(self):
        pass
