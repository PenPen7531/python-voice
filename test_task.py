from multiprocessing.sharedctypes import Value
import pytest
from models.tasks import Task

def test_init_succ():
    task1=Task("Make Room", "Jan 31")
    assert task1.date=="Jan 31"
    assert task1.task=="Make Room"

def test_to_dict():
    task1=Task("Clean dishes", "Feb 31")
    assert task1.date=="Feb 31"
    assert task1.task=="Clean dishes"
    assert task1.to_dict()=={
        "task": "Clean dishes",
        "date": "Feb 31"
    }

def test_invalid_init():
    with pytest.raises(TypeError):
        Task(123, "Rando Date")
    with pytest.raises(TypeError):
        Task("Rando Task", 392123)