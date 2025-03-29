from abc import ABC, abstractmethod
import json
import csv

class AbstractFile(ABC):
    @abstractmethod
    def read(self) -> list | dict | str:
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

    def read(self) -> list | dict | None:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return None  # Возвращаем None вместо пустого списка
        
    def write(self, data: list | dict) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def append(self, data: list | dict) -> None:
        existing_data = self.read()
        if existing_data is None:
            existing_data = [] if isinstance(data, list) else {}
        
        if isinstance(existing_data, list):
            existing_data.extend(data)
        elif isinstance(existing_data, dict):
            existing_data.update(data)
        self.write(existing_data)


# txt
class TxtFile(AbstractFile):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> str:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return ''
        
    def write (self, data: str) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(data)

    def append(self, data: str) -> None:
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(data + '\n')

# Csv
class CsvFile(AbstractFile):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> list[list[str]]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return list(csv.reader(f))
        except FileNotFoundError:
            return []
        
    def write(self, data: list[list[str]]) -> None:
        with open(self.file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    def append(self, data: list[list[str]]) -> None:
        with open(self.file_path, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)