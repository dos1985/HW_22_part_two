from config import SHOP_MAX_UNIQUE_ITEMS


class StorageCheck:
    @staticmethod
    def items_type(items):
        if type(items) != dict:
            raise TypeError("некорректный запрос - items должно быть dict.")

    @staticmethod
    def capacity_type(capacity):
        if type(capacity) != int:
            raise TypeError("некорректный запрос - capacity должно быть int.")

    @staticmethod
    def items_fit_capacity(items, capacity):
        if sum(items.values()) > capacity:
            raise ValueError("некорректный запрос - количество единиц товаров больше, чем вместительность.")

    @staticmethod
    def unique_items_amount_in_shop(items):
        if len(items) > SHOP_MAX_UNIQUE_ITEMS:
            raise ValueError(f"количество уникальных товаров должно быть не больше {SHOP_MAX_UNIQUE_ITEMS} "
                             "- попробуйте уменьшить количество уникальных товаров.")

    @staticmethod
    def amount_type(amount):
        if type(amount) != int:
            raise TypeError("некорректный запрос - amount должно быть целым числом.")

    @staticmethod
    def amount_value(amount):
        if amount <= 0:
            raise ValueError("некорректный запрос - amount должно быть больше 0.")

    @staticmethod
    def unique_items_before_add(items, title):
        if len(items) == SHOP_MAX_UNIQUE_ITEMS and title not in items.keys():
            raise ValueError("количество уникальных товаров достигло максимального значения - попробуйте что-то другое.")

    @staticmethod
    def free_space_available(free_space, amount):
        if free_space < amount:
            raise ValueError("недостаточно места - попробуйте что-то другое.")

    @staticmethod
    def title_in_items(items, title):
        if not items.get(title):
            raise ValueError("нет товара - попробуйте заказать другой товар.")

    @staticmethod
    def available_amount(available_amount, amount):
        if available_amount < amount:
            raise ValueError("не хватает - попробуйте заказать меньше.")