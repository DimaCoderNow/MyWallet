import json
from typing import List, Dict


class DataBase:
    """
        Хранение данных.
        Позволяет хранить данные в JSON файле, считывать и записывать данные.
    """
    empty_data: Dict = {
        "expenses": [],
        "income": [],
        "balance": 0
    }

    def __init__(self):
        self._data = self._get_data()

    @property
    def data(self) -> Dict:
        """
            Получение обновленных данных
        """
        data = self._get_data()
        return data

    @data.setter
    def data(self, new_data: Dict) -> None:
        """
            Применение новых данных
        """
        self._data = new_data
        self._save_data()

    def _get_data(self) -> Dict:
        """
            Считывает данные из JSON файла, если его нет создается новый с пустыми данными
        """
        try:
            with open('db/data.json', 'r', encoding='utf-8') as file_data:
                return json.load(file_data)
        except FileNotFoundError:
            with open('db/data.json', 'w', encoding='utf-8') as file_data:
                json.dump(self.empty_data, file_data, indent=4)
                return self.empty_data

    def _save_data(self) -> None:
        """
            Записывает данные в JSON файл
        """
        with open('db/data.json', 'w', encoding='utf-8') as file_data:
            json.dump(self._data, file_data, indent=4)
