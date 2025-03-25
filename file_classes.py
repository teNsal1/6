from abc import ABC, abstractmethod
import json
import csv

class AbstractFile(ABC):
    @abstractmethod
    def read(self) -> list | str:
        pass

    @abstractmethod
    def write(self, data) -> None:
        pass

    @abstractmethod
    def append(self,data) -> None:
        pass