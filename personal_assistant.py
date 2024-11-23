import csv
import pandas as pd


class Note:
    def __init__(self):
        pass


class Task:
    def __init__(self):
        pass


class Contact:
    def __init__(self):
        pass


class FinanceRecord:
    def __init__(self):
        pass


class Calculator:
    def __init__(self):
        pass



def main():
    print("""Добро пожаловать в Персональный помощник!
Выберите действие:
1. Управление заметками
2. Управление задачами
3. Управление контактами
4. Управление финансовыми записями
5. Калькулятор
6. Выход""")
    choice = int(input("Выберите действие:"))



if __name__ == "__main__":
    main()
