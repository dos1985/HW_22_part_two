from classes.storage import Storage
from classes.storagecheck import StorageCheck


class Store(Storage):
    def __init__(self, items, capacity=100):
        StorageCheck.items_type(items)
        StorageCheck.capacity_type(capacity)
        StorageCheck.items_fit_capacity(items, capacity)

        super().__init__(items, capacity)

    def check_before_add(self, title: str, amount: int):
        StorageCheck.amount_type(amount)
        StorageCheck.amount_value(amount)
        StorageCheck.free_space_available(self.get_free_space(), amount)

    def check_before_remove(self, title: str, amount: int):
        StorageCheck.amount_type(amount)
        StorageCheck.amount_value(amount)
        StorageCheck.title_in_items(self.items, title)
        StorageCheck.available_amount(self.items.get(title, 0), amount)

    def remove(self, title: str, amount: int):
        super().remove(title, amount)

        # Удалить товар из списка, если его не осталось
        if self.items[title] == 0:
            del self.items[title]