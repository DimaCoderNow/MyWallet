from datetime import datetime
from typing import List, Dict

from db.db import DataBase


class Wallet:
    """
        Кошелек пользователя
    """
    database: DataBase = DataBase()

    def __init__(self):
        self.data: Dict = self.database.data

    def get_balance(self) -> int:
        balance = self.data["balance"]
        return balance


class Income(Wallet):
    """
        Учет расходов
    """
    def __init__(self):
        super().__init__()

    @property
    def income(self) -> List:
        return self.data["income"]

    @income.setter
    def income(self, new_value: (str, int)) -> None:
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")
        new_income = {
            "date": formatted_date,
            "description": new_value[0],
            "sum": new_value[1]
        }
        self.data["income"].append(new_income)
        self.database.data = self.data


class Expenses:
    """
        Учет доходов
    """
    def __init__(self):
        ...


