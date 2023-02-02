from app.storage_init import storages
from classes.request import Request


request = Request(storages)

print("Логистическая программа приветствует Вас.\n")
print(request.help())

while True:
    user_request = input("\nВведите запрос: ")
    print()

    if user_request.lower() == "exit":
        exit()

    if user_request.lower() == "help":
        print(request.help())
        continue

    try:
        task = request.parse(user_request)

        if task.get("показать"):
            storage = storages.get(task.get("показать"))
            print(storage.get_items())
        else:
            storage_from = storages.get(task.get("from"))
            storage_to = storages.get(task.get("to"))
            product = task.get("product")
            amount = task.get("amount")

            storage_from.remove(product, amount)
            print(f'Курьер забрал {amount} {product} из {task.get("from")}')
            print(f'На {task.get("from")} осталось:\n {storage_from.get_items()}')

            storage_to.add(product, amount)
            print(f'Курьер доставил {amount} {product} в {task.get("to")}')
            print(f'В {task.get("to")} стало:\n {storage_to.get_items()}')

    except Exception as e:
        print(e)