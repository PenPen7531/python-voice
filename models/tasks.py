class Task:
    def __init__(self, task, date):
        if type(task) != str:
            raise TypeError
        self.task=task
        if type(date) != str:
            raise TypeError
        self.date=date

    def to_dict(self):
        return {
            "task": self.task,
            "date": self.date,
        }   