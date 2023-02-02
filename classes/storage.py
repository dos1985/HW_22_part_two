from abc import ABC


class Storage(ABC):
    def __init__(self, items: dict, capacity: int):
        self.items = items
        self.capacity = capacity

    def add(self, title: str, amount: int):
        """Увеличивает запас items"""
        self.items[title] = self.items.get(title, 0) + amount

    def remove(self, title: str, amount: int):
        """Уменьшает запас items"""
        self.items[title] -= amount

    def get_free_space(self) -> int:
        """Вернуть количество свободных мест"""
        return self.capacity - sum(self.items.values())

    def get_items(self) -> dict:
        """Возвращает содержание склада в словаре {товар: количество}"""
        return self.items

    def get_unique_items_count(self) -> int:
        """Возвращает количество уникальных товаров."""
        return len(self.items)
