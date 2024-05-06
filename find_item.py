from typing import Dict, List


class FindItem:
    """
        Поиск записей по описанию, дате или сумме
    """

    def __init__(self, db, category):
        self.category = category
        self.data = db.data
        self.item = None
        self.item_id = None

    def find_sum(self) -> List[Dict]:
        """
            Поиск записи по сумме
        """
        self.item = int(self.item)
        return [income for income in self.data[self.category] if self.item == income["sum"]]

    def find_date(self) -> List[Dict]:
        """
            Поиск записи по дате
        """
        return [income for income in self.data[self.category] if self.item == income["date"]]

    def find_description(self):
        """
            Поиск записи по описанию
        """
        return [income for income in self.data[self.category] if self.item in income["description"]]

    def get_by_id(self) -> Dict | None:
        if self.item_id and self.item_id < len(self.data[self.category]):
            return self.data[self.category][self.item_id]
        return None

