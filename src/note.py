import messages


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
