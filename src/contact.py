import messages


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

    def run(self):
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
