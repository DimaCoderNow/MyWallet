import sys
from typing import List


class Commands:
    """
        Обработка команд
    """

    def __init__(self):
        ...


class Wallet:
    """
        Кошелек пользователя
    """
    def __init__(self):
        ...


class DataBase:
    """
        Хранение данных
    """

    def __init__(self):
        ...


class Income:
    """
        Учет расходов
    """

    def __init__(self):
        ...


class User:
    """
        Пользователь кошелька
    """

    def __init__(self):
        ...


class Expenses:
    """
        Учет доходов
    """
    def __init__(self):
        ...


class FindItem:
    """
        Поиск записей по категории, дате или сумме
    """
    def __init__(self):
        ...


class WalletCLI:
    def __init__(self):
        self.system_args: List = sys.argv


    def run(self):
        if len(self.system_args) < 2:
            print("Используйте: wallet <command>")
            sys.exit(1)

        command = self.system_args[1]

        if command == "start":
            print("Использование: wallet <start>")
        else:
            print("Недопустимая команда. Доступные команды: 'start', ")


if __name__ == '__main__':
    wallet = WalletCLI()
    wallet.run()
