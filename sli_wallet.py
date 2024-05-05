import sys
from typing import List

from my_wallet import Wallet, Income


class WalletCLI:
    """
        Получение команд от пользователя для взаимодействия с кошельком
    """
    my_wallet = Wallet()
    my_income = Income()
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
                print(self.prefix_out, Wallet().get_balance())
            elif self.__command == "sum_income":
                ...
            elif self.__command == "sum_expenses":
                ...
            elif self.__command == "get_income":
                self._print_category(self.my_income.income)
                self._success()
            elif self.__command == "get_expenses":
                ...
            elif self.__command == "add_income":
                print(self.prefix_out, "Введите данные расхода:")
                self.my_income.income = (
                    input(f"{self.prefix_in}Описание: "), int(input(f"{self.prefix_in}Сумма: "))
                )
                self._success()
            elif self.__command == "add_expenses":
                ...
            elif self.__command == "find_income":
                ...
            elif self.__command == "find_expenses":
                ...
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

    def _print_category(self, categories: List[dict]) -> None:
        print(self.prefix_out, "ID  Дата        Сумма Описание  ")
        [print(
            self.prefix_out, i, cat["date"], "|", cat["sum"], "|", cat["description"]
        ) for i, cat in enumerate(categories)]


if __name__ == '__main__':
    wallet_cli = WalletCLI()
    wallet_cli.run()
