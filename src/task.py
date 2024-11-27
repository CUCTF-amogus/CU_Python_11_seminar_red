from config import messages

import json
from datetime import datetime


class Task:
    def __init__(self):
        self.func_choice = {
            1: self.create_task,
            2: self.list_tasks,
            3: self.mark_done,
            4: self.redact_task,
            5: self.delete_task,
            6: self.export_csv,
            7: self.import_csv,
        }

        self.datafile_path = "data/tasks_data.json"
        self.tasks = {}
        # self.tasks[123] = {
        #     "id": 123,
        #     "title": "amogus",
        #     "description": "sus",
        #     "done": False,
        #     "priority": "high",
        #     "due_date": datetime.strptime("12-12-2024", '%d-%m-%Y').date(),
        # }

    def run(self):
        choice = 0
        while True:
            print(messages.task_start_message)
            choice = int(input(messages.choose_message))
            if choice == 8:
                return
            func = self.func_choice[choice]
            func()

    def create_task(self):
        id = int(input("Введите id нового таска: "))
        if id in self.get_tasks().keys():
            print(f"Таск с id - {id} уже существует")
            return

        self.update_task(id)

    def get_tasks(self):
        return self.tasks

    def update_task(self, id: int):
        title = input(f"Введите title таска: ")
        content = input(f"Введите content таска: ")
        priority = input(f"Введите priority таска: ")
        due_date = input(f"Введите due_date таска в формате ДД-ММ-ГГГГ: ")
        due_date = datetime.strptime(due_date, "%d-%m-%Y").date()

        self.tasks[id] = {
            "id": id,
            "title": title,
            "description": content,
            "done": False,
            "priority": priority,
            "due_date": due_date,
        }

    def list_tasks(self):
        for index, task in self.get_tasks().items():
            print(f"id: {index} - title: {task["title"]}")

    def list_task_details(self, task: dict):
        print(
            f"""id: {task["id"]}
title: {task["title"]}
description: {task["description"]}
done: {task["done"]}
priority: {task["priority"]}
due_date: {task["due_date"]}"""
        )

    def list_tasks_details(self):
        for index, task in self.get_tasks().items():
            self.list_task_details(task)

    def mark_done(self):
        id = int(input("Введите id таска для изменения: "))
        if id not in self.get_tasks().keys():
            print(f"Таск с id - {id} не существует")
            return

        self.tasks[id]["done"] = True
        print(f"Таск с id - {id} помечен как сделанный")

    def redact_task(self):
        id = int(input("Введите id таска для редактирования: "))
        if id not in self.get_tasks().keys():
            print(f"Таск с id - {id} не найден")
            return

        self.update_note(id)
        print(f"Таск с id - {id} успешно изменен")

    def delete_task(self):
        id = int(input("Введите id таска для редактирования: "))
        if id not in self.get_tasks().keys():
            print(f"Таск с id - {id} не найден")
            return

        self.tasks.pop(id)
        print(f"Таск с id - {id} успешно удален")

    def import_csv(self):
        # get data from the file
        with open(self.datafile_path, "r") as file:
            json_object = json.load(file)

            for index, value in json_object.items():
                json_object[index]["due_date"] = datetime.strptime(value["due_date"], "%Y-%m-%d").date()
            self.tasks = json_object

        print(f"Данные успешно выгружены из файла {self.datafile_path}")

    def export_csv(self):
        # load data to the file
        with open(self.datafile_path, "w") as file:
            json.dump(self.get_tasks(), file, indent=4, default=str)

        print(f"Данные успешно загружены в файл {self.datafile_path}")


def test():
    task = Task()

    print("==============")
    task.list_tasks()
    print("==============")

    task.import_csv()

    print("==============")
    task.list_tasks()
    print("==============")

    task.create_task()

    print("==============")
    task.list_tasks()
    print("==============")

    task.export_csv()
