class Request:

    def __init__(self, storages: dict):
        self.storages = storages

    @property
    def storage_list(self):
        return list(self.storages.keys())

    def help(self):
        return f"Вы можете ввести команды:\n" \
               f"1. показать содержимое ОбЪЕКТ\n" \
               f"2. доставить из ОБЪЕКТ_1 в ОБЪЕКТ_2 ЧИСЛО НАИМЕНОВАНИЕ_ТОВАРА\n" \
               f"3. help - для вывода этой справки\n" \
               f"4. exit - для выхода из программы\n" \
               f"Примечание: список объектов: {self.storage_list}\n"

    def parse(self, request_str: str) -> dict:

        request_str = request_str.lower()
        words_list = request_str.split(" ")

        if "показать" in words_list:
            for storage in self.storage_list:
                if storage in words_list:
                    return {"показать": storage}

            raise ValueError("не найден объект из списка, чтобы ПОКАЗАТЬ.")

        elif "доставить" in words_list:
            result = {}

            for index, word in enumerate(words_list):
                if ("из" == word) and (index != len(words_list)):
                    from_obj = words_list[index + 1]

                    if from_obj not in self.storage_list:
                        raise "не корректный запрос: объект после ИЗ не из списка доступных объектов."
                    result["from"] = from_obj

                elif ("в" == word) and (index != len(words_list)):
                    to_obj = words_list[index + 1]

                    if to_obj not in self.storage_list:
                        raise "не корректный запрос: объект после В не из списка доступных объектов."
                    result["to"] = to_obj

                elif word.isdigit():
                    result["amount"] = int(word)
                    result["product"] = words_list[index + 1]

            if len(result) != 4:
                raise ValueError("не корректный запрос: не хватает данных для того, чтобы ДОСТАВИТЬ.")

            self.storages[result["from"]].check_before_remove(result["product"], result["amount"])
            print(f'{result["from"]} проверен - нужное количество есть.')

            self.storages[result["to"]].check_before_add(result["product"], result["amount"])
            print(f'{result["to"]} проверен - готов принять товар.')

            return result

        else:
            raise ValueError("не корректный запрос - см. help.")