from config import messages

import csv
from datetime import datetime
from pprint import pprint


class Note:
    def __init__(self):
        self.func_choice = {
            1: self.create_note,
            2: self.list_notes,
            3: self.list_note_details,
            4: self.redact_note,
            5: self.delete_note,
            6: self.import_csv,
            7: self.export_csv,
        }

        self.datafile_path = "data/note_data.csv"
        self.notes = {}

    def run(self):
        choice = 0
        while choice != 8:
            print(messages.task_start_message)
            choice = input(messages.choose_message)
            func = self.func_choice[choice]
            func()

    def create_note(self):
        id = int(input("Введите id новой заметки: "))
        if id in self.get_notes().keys():
            print(f"Запись с id - {id} уже существует")
            return

        self.update_note(id)

    def get_notes(self):
        return self.notes

    def update_note(self, id):
        title = input(f"Введите title новой заметки: ")
        content = input(f"Введите content новой заметки: ")
        timestamp = datetime.now()

        self.notes[id] = {
            "id": id,
            "title": title,
            "content": content,
            "timestamp": timestamp,
        }

    def list_notes(self):
        for index, note in self.get_notes().items():
            print(f"id: {index} - title: {note["title"]}")

    def list_note_details(self, note: dict):
        print(
            f"""id: {note["id"]}
title: {note["title"]}
content: {note["content"]}
timestamp: {note["timestamp"]}"""
        )

    def list_notes_details(self):
        for index, note in self.get_notes().items():
            self.list_note_details(note)

    def redact_note(self):
        id = int(input("Введите id для редактирования заметки: "))
        if id not in self.get_notes().keys():
            print(f"Запись с id - {id} не найдена")
            return

        self.update_note(id)
        print(f"Запись с id - {id} изменена")

    def delete_note(self):
        id = int(input("Введите id для удаления заметки: "))
        if id not in self.get_notes().keys():
            print(f"Запись с id - {id} не найдена")
            return

        self.notes.pop(id)
        print(f"Запись с id - {id} удалена")

    def import_csv(self):
        # get data from the file

        with open(self.datafile_path, mode ='r') as file:
            csv_file = csv.reader(file)
            next(csv_file)

            for line in csv_file:
                id, title, content, timestamp = line
                timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                self.notes[id] = {
                    "id": id,
                    "title": title,
                    "content": content,
                    "timestamp": timestamp,
                }

        print(f"Данные успешно выгружены из файла {self.datafile_path}")

    def export_csv(self):
        # load data to the file
        fields = ["id", "title", "content", "timestamp"]

        notes_list = []
        for note in self.get_notes().values():
            note_list = list(note.values())
            note_list[-1] = str(note_list[-1])[:19]
            notes_list.append(note_list)
        print(notes_list)
        
        with open(self.datafile_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(notes_list)
        
        print(f"Данные успешно загружены в файл {self.datafile_path}")


def test():
    note = Note()
    print("==============")
    note.list_notes()
    print("==============")

    note.import_csv()

    print("==============")
    note.list_notes()
    print("==============")

    note.create_note()
    print("==============")
    note.list_notes()
    print("==============")

    note.export_csv()

    print("==============")
    note.list_notes_details()
    print("==============")
