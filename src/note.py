from config import messages

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

        self.notes = {}

    def run(self):
        choice = 0
        while choice != 8:
            print(messages.task_start_message)
            choice = input(messages.choose_message)
            func = self.func_choice[choice]

    def create_note(self):
        id = int(input("Введите id новой заметки: "))
        title = input(f"Введите title новой заметки: ")
        content = input(f"Введите content новой заметки: ")
        timestamp = datetime.now()

        self.notes[id] = {
            "id": id,
            "title": title,
            "content": content,
            "timestamp": timestamp,
        }

    def get_notes(self):
        return self.notes

    def list_notes(self):
        pprint(self.get_notes())

    def list_note_details(self):
        pass

    def redact_note(self):
        pass

    def delete_note(self):
        pass

    def import_csv(self):
        # get from the file
        pass

    def export_csv(self):
        # load to the file
        pass


def test():
    note = Note()

    note.create_note()
    # 123
    # amogus
    # sussus
    print(note.get_notes())
    print("==============")
    note.list_notes()
