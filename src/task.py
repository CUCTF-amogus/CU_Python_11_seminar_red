from config import messages


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

    def run(self):
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
