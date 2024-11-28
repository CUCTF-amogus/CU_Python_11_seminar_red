from config import messages

from datetime import datetime
import json


class FinanceRecord:
    def __init__(self):
        self.func_choice = {
            1: self.create_record,
            2: self.list_records,
            3: self.list_specific_records,
            4: self.import_json,
            5: self.export_json,
        }

        self.datafile_path = "data/records_data.json"
        self.records = {}

    def run(self):
        choice = 0
        while True:
            print(messages.task_start_message)
            choice = input(messages.choose_message)
            if choice == 6:
                return
            func = self.func_choice[choice]
            func()

    def create_record(self):
        id = int(input("Введите id новой записи: "))
        if id in self.get_records().keys():
            print(f"Запись с id - {id} уже существует")
            return

        self.update_record(id)

    def get_records(self):
        return self.records

    def update_record(self, id: int):
        amount = int(input(f"Введите amount записи: "))
        description = input(f"Введите description записи: ")
        category = input(f"Введите category записи: ")
        date = input(f"Введите date записи в формате ДД-ММ-ГГГГ: ")
        date = datetime.strptime(date, "%d-%m-%Y").date()

        self.records[id] = {
            "id": id,
            "amount": amount,
            "description": description,
            "category": category,
            "date": date,
        }

    def list_records(self):
        sort_type = input(
            "Введите тип сортировки time, category и любой другой для ее отсутствия: "
        ).lower()
        data = self.get_records()

        if sort_type == "time":
            data = sorted(data, key=lambda x: x["date"])
        elif sort_type == "category":
            data = sorted(data, key=lambda x: x["category"])

        for index, task in data.items():
            print(f"id: {index} - date: {task["date"]}")

    def list_specific_records(self):
        from_date = input(
            f"Введите date с которого будут все записи в формате ДД-ММ-ГГГГ: "
        )
        from_date = datetime.strptime(from_date, "%d-%m-%Y").date()

        data = self.get_records()
        data = list(filter(data, lambda x: x["data"] >= from_date))

    def import_json(self):
        # get data from the file
        with open(self.datafile_path, "r") as file:
            json_object = json.load(file)

            for index, value in json_object.items():
                json_object[index]["date"] = datetime.strptime(
                    value["date"], "%Y-%m-%d"
                ).date()

            self.records = json_object

        print(f"Данные успешно выгружены из файла {self.datafile_path}")

    def export_json(self):
        # load data to the file
        with open(self.datafile_path, "w") as file:
            json.dump(self.get_records(), file, indent=4, default=str)

        print(f"Данные успешно загружены в файл {self.datafile_path}")


def test():
    finance_record = FinanceRecord()

    # finance_record.create_record()

    print("==============")
    finance_record.list_records()
    print("==============")

    finance_record.import_json()

    print("==============")
    finance_record.list_records()
    print("==============")

    finance_record.export_json()

    print("==============")
    finance_record.list_records()
    print("==============")
