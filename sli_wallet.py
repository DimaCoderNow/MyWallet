import sys
import re

from typing import List, Dict

from db.db import DataBase
from find_item import FindItem
from my_wallet import Wallet, Income, Expenses


class WalletCLI:
    """
        Получение команд от пользователя для взаимодействия с кошельком
    """
    db = DataBase()
    my_wallet = Wallet(db)
    my_income = Income(db)
    my_expenses = Expenses(db)
    find_income = FindItem(db, "income")
    find_expenses = FindItem(db, "expenses")
    help_cmd = [
        "balance - посмотреть текущий баланс",
        "sum_income - сумма расходов",
        "sum_expenses - сумма доходов",
        "get_income - посмотреть расходы",
        "get_expenses - посмотреть доходы",
        "add_income - добавить расходы",
        "add_expenses - добавить доходы",
        "find_income - поиск расходов",
        "find_expenses - поиск доходов",
        "exit - выход из программы",
    ]
    prefix_in = "\033[35m" + "sli_wallet: " + "\033[0m"
    prefix_out = "\033[35m" + " " * 10 + ">" + "\033[0m"

    def __init__(self):
        print(f"{self.prefix_in}")
        print(f"{self.prefix_out} Добро пожаловать!")
        self.__command = self._get_command()

    def run(self):
        while True:
            if self.__command == "balance":
                print(self.prefix_out, self.my_wallet.balance)

            elif self.__command == "sum_income":
                print(self.prefix_out, "Сумма расходов")
                print(self.prefix_out, self.my_income.sum_income)

            elif self.__command == "sum_expenses":
                print(self.prefix_out, "Сумма доходов")
                print(self.prefix_out, self.my_expenses.sum_expenses)

            elif self.__command == "get_income":
                self._print_category(self.my_income.income)

            elif self.__command == "get_expenses":
                self._print_category(self.my_expenses.expenses)

            elif self.__command == "add_income":
                self.my_income.income = self._input_category("расхода")
                self._success()

            elif self.__command == "add_expenses":
                self.my_expenses.expenses = self._input_category("дохода")
                self._success()

            elif self.__command == "find_income":
                result = self._item_find(self.find_income)
                self._print_category(result)
            elif self.__command == "find_expenses":
                result = self._item_find(self.find_expenses)
                self._print_category(result)

            elif self.__command == "exit":
                print(self.prefix_out, "Программа завершена")
                sys.exit(0)

            elif self.__command == "help":
                [print(self.prefix_out, cmd) for cmd in self.help_cmd]

            else:
                print(self.prefix_out,
                      "\033[31m" + "Недопустимая команда." + "\033[0m" + " Просмотреть доступные команды: help")
            self.__command = self._get_command()

    def _get_command(self) -> str:
        return input(self.prefix_in)

    def _success(self) -> None:
        print(self.prefix_out, "success!")

    def _print_category(self, categories: List[Dict]) -> None:
        print(self.prefix_out, "ID  Дата        Сумма Описание  ")
        [print(
            self.prefix_out, i, cat["date"], "|", cat["sum"], "|", cat["description"]
        ) for i, cat in enumerate(categories)]

    def _input_category(self, type_cat: str) -> (str, int):
        print(f"{self.prefix_out} Введите данные {type_cat}:")
        return input(f"{self.prefix_in}Описание: "), int(input(f"{self.prefix_in}Сумма: "))

    def _item_find(self, find: FindItem) -> List[Dict]:
        find.item = input(f"{self.prefix_out} Введите данные для поиска")
        if not find.item:
            print(self.prefix_out, "Пустой запрос!")
            return []
        elif find.item.isdigit():
            return find.find_sum()
        elif re.match(r"\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\b", find.item):
            return find.find_date()
        else:
            return find.find_description()


if __name__ == '__main__':
    wallet_cli = WalletCLI()
    wallet_cli.run()
