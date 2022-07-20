from models.log import Logs
from models.tasks import Task
import pytest
import json
import os

def test_init():
    log1=Logs("Jeff")
    assert log1.name=="Jeff"
    assert log1.tasks==[]


def test_add_task():
    task1=Task("Made Room", "Jan 31")
    log1=Logs("Jeff")
    log1.add_task(task1)
    assert task1 in log1.tasks

def test_invalid_task():
    log1=Logs("Jeff")
    with pytest.raises(TypeError):
        log1.add_task("Test")

def test_save_tasks():
    task1=Task("Made Room", "Jan 31")
    log1=Logs("test_file")
    log1.add_task(task1)
    log1.save_tasks()
    with open(f"data/{log1.name}_tasks.json") as file:
                tasks = [
                    Task(
                        task["task"],
                        task["date"],
                    ) for task in json.load(file)
                ]   

    assert tasks[0].task=="Made Room"
    assert tasks[0].date=="Jan 31"

    reopen_file=Logs("test_file")

    os.remove("./data/test_file_tasks.json")

def test_invalid_init():
    with pytest.raises(TypeError):
        Logs(123)