from classes.shop import Shop
from classes.store import Store
from config import SHOP_INIT_CONTENT, STORE_INIT_CONTENT


# Инициализация объектов
try:
    shop = Shop(SHOP_INIT_CONTENT)
    store = Store(STORE_INIT_CONTENT)
except Exception as e:
    print(f"Ошибка инициализации - {e}")
    exit()

storages = {"магазин": shop,
            "склад": store
            }