from config import messages


class Calculator:
    def __init__(self):
        self.func_choice = {
            1: self.calculate,
        }

        self.datafile_path = "data/tasks_data.json"
        self.tasks = {}

    def run(self):
        choice = 0
        while True:
            print(messages.calculator_start_message)
            choice = int(input(messages.choose_message))
            if choice == 2:
                return
            func = self.func_choice[choice]
            func()
    
    def calculate(self):
        expression = input("Введите выражение которое надо посчитать: ")
        print(f"{expression} = {eval(expression)}")

def test():
    calc = Calculator()

    calc.calculate()
    calc.calculate()
