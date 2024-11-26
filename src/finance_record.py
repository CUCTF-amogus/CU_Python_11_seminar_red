from config import messages


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

    def run(self):
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
