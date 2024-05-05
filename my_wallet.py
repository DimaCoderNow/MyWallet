import sys
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


class Income:
    """
        Учет расходов
    """

    def __init__(self):
        ...


class Expenses:
    """
        Учет доходов
    """
    def __init__(self):
        ...


