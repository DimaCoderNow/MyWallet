from datetime import datetime
from typing import List, Dict


class Wallet:
    """
        Кошелек пользователя
    """
    def __init__(self, db):
        self.db = db

    @property
    def balance(self) -> int:
        """
            Возвращает текущий баланс из базы данных
        """
        return self.db.data["balance"]

    def _create_data(self, value: (str, int)) -> Dict:
        """
            Формирует данные новой записи в виде словаря с текущей датой
        """
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")
        return {
            "date": formatted_date,
            "description": value[0],
            "sum": value[1]
        }

    def _update_item(self, item_id: int, new_value: (str, int), item_key: str) -> None:
        """
            Обновление записи в базе данных в зависимости от категории
        """
        update_data = self.db.data
        if new_value[0]:
            update_data[item_key][item_id]["description"] = new_value[0]
        if new_value[1]:
            diff_balance = update_data[item_key][item_id]["sum"] - new_value[1]
            update_data[item_key][item_id]["sum"] = new_value[1]
            if item_key == "income":
                update_data["balance"] = self.balance + diff_balance
            else:
                update_data["balance"] = self.balance - diff_balance
        self.db.data = update_data


class Income(Wallet):
    """
        Учет расходов
    """
    def __init__(self, db):
        super().__init__(db)

    @property
    def income(self) -> List[Dict]:
        """
            Возвращает записи с расходами
        """
        return self.db.data["income"]

    @income.setter
    def income(self, new_value: (str, int)) -> None:
        """
            Добавление новой записи расхода
        """
        new_income = self._create_data(new_value)
        new_data = self.db.data
        new_data["income"].append(new_income)
        new_data["balance"] = self.balance - new_value[1]
        self.db.data = new_data

    @property
    def sum_income(self) -> int:
        """
            Вычисляет сумму расходов
        """
        return sum(income["sum"] for income in self.db.data["income"])

    def update(self, income_id: int, new_value: (str, int)) -> None:
        """
            Обновление расходов
        """
        self._update_item(income_id, new_value, "income")


class Expenses(Wallet):
    """
        Учет доходов
    """
    def __init__(self, db):
        super().__init__(db)

    @property
    def expenses(self) -> List[Dict]:
        """
            Возвращает записи с доходами
        """
        return self.db.data["expenses"]

    @expenses.setter
    def expenses(self, new_value: (str, int)) -> None:
        """
            Добавление новой записи дохода
        """
        new_expenses = self._create_data(new_value)
        new_data = self.db.data
        new_data["expenses"].append(new_expenses)
        new_data["balance"] = self.balance + new_value[1]
        self.db.data = new_data

    @property
    def sum_expenses(self) -> int:
        """
            Вычисляет сумму доходов
        """
        return sum(expense["sum"] for expense in self.db.data["expenses"])

    def update(self, expenses_id: int, new_value: (str, int)) -> None:
        """
            Обновление доходов
        """
        self._update_item(expenses_id, new_value, "expenses")
