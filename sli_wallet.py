import sys
from typing import List

from my_wallet import Wallet, Income


class WalletCLI:
    def __init__(self):
        self.system_args: List = sys.argv

    def run(self):
        if len(self.system_args) < 2:
            print("Используйте: wallet <command>")
            sys.exit(1)

        command = self.system_args[1]

        if command == "balance":
            print(Wallet().get_balance())
        elif command == "income":
            print(Income())
        else:
            print("Недопустимая команда. Доступные команды: 'start', ")


if __name__ == '__main__':
    wallet_cli = WalletCLI()
    wallet_cli.run()
