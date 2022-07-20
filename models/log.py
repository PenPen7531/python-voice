import json

from models.tasks import Task

class Logs: 
    def __init__(self, name):
        if type(name) != str:
            raise TypeError
        self.name = name
        self.tasks=[]
        try: 
            with open(f"data/{name}_tasks.json") as file:
                self.tasks = [
                    Task(
                        task["task"],
                        task["date"],
                    ) for task in json.load(file)
                ]   
        except:
            self.logs=[]
            print("Created new file")

    def add_task(self, task):
        if type(task) is not Task:
            raise TypeError
        self.tasks.append(task)

    def save_tasks(self):
        with open(f"data/{self.name}_tasks.json", "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file)