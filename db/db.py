import json
from typing import List, Dict


class DataBase:
    """
        Хранение данных
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
        data = self._get_data()
        return data

    @data.setter
    def data(self, new_data: Dict):
        self._data = new_data
        self._save_data()

    def _get_data(self) -> Dict:
        try:
            with open('db/data.json', 'r', encoding='utf-8') as file_data:
                return json.load(file_data)
        except FileNotFoundError:
            with open('db/data.json', 'w', encoding='utf-8') as file_data:
                json.dump(self.empty_data, file_data, indent=4)
                return self.empty_data

    def _save_data(self):
        with open('db/data.json', 'w', encoding='utf-8') as file_data:
            json.dump(self._data, file_data, indent=4)
