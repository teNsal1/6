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

# JSON
class JsonFile(AbstractFile):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> list | dict:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        
    def write(self,data: list | dict) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def append(self, data: list | dict) -> None:
        existing_data = self.read()
        if isinstance(existing_data, list):
            existing_data.extend(data)
        elif isinstance(existing_data, dict):
            existing_data.update(data)
        self.write(existing_data)