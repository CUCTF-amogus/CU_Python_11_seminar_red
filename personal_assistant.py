import messages

import csv
import pandas as pd


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
        
        self.run()

    def run(self, ):
        choice = 0
        while choice != 8:
            print(messages.task_start_message)
            choice = input(messages.choose_message)
            func = self.func_choice[choice]

    def create_note():
        pass

    def list_notes():
        pass

    def list_note_details():
        pass

    def redact_note():
        pass

    def delete_note():
        pass

    def import_csv():
        pass
    
    def export_csv():
        pass


class Task:
    def __init__(self):
        self.func_choice = {
            1: self.create_task,
            2: self.list_tasks,
            3: self.mark_done,
            4: self.redact_task,
            5: self.delete_task,
            6: self.import_csv,
            7: self.export_csv,
        }
        
        self.run()

    def run(self, ):
        choice = 0
        while choice != 8:
            print(messages.task_start_message)
            choice = input(messages.choose_message)
            func = self.func_choice[choice]
    
    def create_task():
        pass

    def list_tasks():
        pass

    def mark_done():
        pass

    def redact_task():
        pass

    def delete_task():
        pass

    def import_csv():
        pass
    
    def export_csv():
        pass


class Contact:
    def __init__(self):
        self.func_choice = {
            1: self.create_contact,
            2: self.find_contact,
            3: self.redact_contact,
            4: self.delete_contact,
            5: self.import_csv,
            6: self.export_csv,
        }
        
        self.run()

    def run(self, ):
        choice = 0
        while choice != 7:
            print(messages.task_start_message)
            choice = input(messages.choose_message)
            func = self.func_choice[choice]
    
    def create_contact():
        pass

    def find_contact():
        pass

    def redact_contact():
        pass

    def delete_contact():
        pass

    def import_csv():
        pass
    
    def export_csv():
        pass


class FinanceRecord:
    def __init__(self):
        self.func_choice = {
            1: self.create_record,
            2: self.list_record,
            3: self.list_specific_record,
            4: self.import_csv,
            5: self.export_csv,
        }
        
        self.run()

    def run(self, ):
        choice = 0
        while choice != 6:
            print(messages.task_start_message)
            choice = input(messages.choose_message)
            func = self.func_choice[choice]
    
    def create_record():
        pass

    def list_record():
        pass

    def list_specific_record():
        pass

    def import_csv():
        pass
    
    def export_csv():
        pass


class Calculator:
    def __init__(self):
        pass



def main():
    print(messages.start_message)
    choice = int(input(messages.choose_message))
    if choice == 1:
        note = Note()


if __name__ == "__main__":
    main()
