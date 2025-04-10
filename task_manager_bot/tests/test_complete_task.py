
import os
import pytest
from task_manager_bot.database import TaskDatabase



TEST_DB = "test_tasks.db"

@pytest.fixture
def db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    db = TaskDatabase(db_path=TEST_DB)
    yield db
    db.close()
    os.remove(TEST_DB)

def test_complete_task(db):
    print("Testing complete_task() function.")

    task1_id = db.add_task("Test görev 1")
    task2_id = db.add_task("Test görev 2")

    db.complete_task(task1_id)

    tasks_after = db.get_all_tasks()
    assert tasks_after[0][0] == task1_id
    assert tasks_after[0][2] == 1, "Görev 1 tamamlanmış olmalı."
    assert tasks_after[1][2] == 0, "Görev 2 tamamlanmamış olmalı."

    print("✅ Test passed: complete_task().")
