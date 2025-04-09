
import sys
import os
import pytest
from task_manager_bot.database import TaskDatabase
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

TEST_DB = "test_tasks.db"

@pytest.fixture
def db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    db = TaskDatabase(db_path=TEST_DB)
    yield db
    db.close()
    os.remove(TEST_DB)

def test_show_tasks(db):
    print("Testing get_all_tasks() function.")
    
    # Test başlangıcında veritabanı boş olmalı
    tasks = db.get_all_tasks()
    assert isinstance(tasks, list), "get_all_tasks() bir liste döndürmeli."
    assert len(tasks) == 0, "Veritabanı başlangıçta boş olmalı."

    print("Test setup passed: No tasks found in the database before the test started.")

    # Görev ekle
    db.add_task("Görev A")
    db.add_task("Görev B")

    # Görevleri kontrol et
    tasks = db.get_all_tasks()
    assert len(tasks) == 2, "Eklenen iki görevden sonra toplam görev sayısı 2 olmalı."

    descriptions = [task[1] for task in tasks]
    assert "Görev A" in descriptions and "Görev B" in descriptions, "Görev açıklamaları doğru saklanmalı."

    print("✅ Test passed: Expected 2 tasks and correct number of tasks retrieved.")
    print("✅ Test passed: Task")
