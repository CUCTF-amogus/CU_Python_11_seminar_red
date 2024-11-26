import messages
from src import *


def main():
    note = Note()
    task = Task()
    contact = Contact()
    finance_record = FinanceRecord()
    calculator = Calculator()

    func_choice = {
        1: note.run,
        2: task.run,
        3: contact.run,
        4: finance_record.run,
        5: calculator.run,
    }

    while True:
        print(messages.start_message)
        choice = int(input(messages.choose_message))

        if choice == 6:
            break

        func = func_choice[choice]
        func()

if __name__ == "__main__":
    main()
