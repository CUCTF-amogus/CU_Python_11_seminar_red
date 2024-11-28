from config import messages

import json


class Contact:
    def __init__(self):
        self.func_choice = {
            1: self.create_contact,
            2: self.find_contact,
            3: self.redact_contact,
            4: self.delete_contact,
            5: self.import_json,
            6: self.export_json,
        }

        self.datafile_path = "data/contacts_data.json"
        self.contacts = {}

    def run(self):
        choice = 0
        while True:
            print(messages.task_start_message)
            choice = input(messages.choose_message)
            if choice == 7:
                return
            func = self.func_choice[choice]
            func()

    def create_contact(self):
        id = int(input("Введите id нового контакта: "))
        if id in self.get_contacts().keys():
            return

        self.update_contact(id)

    def get_contacts(self):
        return self.contacts

    def update_contact(self, id: int):
        name = input(f"Введите name контакта: ")
        phone = input(f"Введите phone контакта: ")
        email = input(f"Введите email контакта: ")

        self.contacts[id] = {
            "id": id,
            "name": name,
            "phone": phone,
            "email": email,
        }

    def list_contacts(self):
        print(self.get_contacts())
        for index, contact in self.get_contacts().items():
            print(f"id: {index} - name: {contact["name"]}")

    def list_contact_details(self, contact: dict):
        print(
            f"""id: {contact["id"]}
name: {contact["name"]}
phone: {contact["phone"]}
email: {contact["email"]}"""
        )

    def find_contact(self):
        name = input("Ввведите имя для поиска контакта")
        for index, contact in self.get_contacts():
            if contact["name"] == name:
                self.list_contact_details(contact)
                return

    def redact_contact(self):
        id = int(input("Введите id контакта для редактирования: "))
        if id not in self.get_contacts().keys():
            print(f"Контакт с id - {id} не найден")
            return

        self.update_contact(id)
        print(f"Контакт с id - {id} успешно изменен")

    def delete_contact(self):
        id = int(input("Введите id контакта для редактирования: "))
        if id not in self.get_contacts().keys():
            print(f"Контакт с id - {id} не найден")
            return

        self.contacts.pop(id)
        print(f"Контакт с id - {id} успешно удален")

    def import_json(self):
        # get data from the file
        with open(self.datafile_path, "r") as file:
            self.contacts = dict(json.load(file))

        print(f"Данные успешно выгружены из файла {self.datafile_path}")

    def export_json(self):
        # load data to the file
        with open(self.datafile_path, "w") as file:
            json.dump(self.get_contacts(), file, indent=4, default=str)

        print(f"Данные успешно загружены в файл {self.datafile_path}")


def test():
    contact = Contact()

    print("==============")
    contact.list_contacts()
    print("==============")

    contact.import_json()

    print("==============")
    contact.list_contacts()
    print("==============")

    contact.create_contact()

    print("==============")
    contact.list_contacts()
    print("==============")

    contact.export_json()
