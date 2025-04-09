import sys
import os
import pytest
from task_manager_bot.database import TaskDatabase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

TEST_DB = "test_tasks.db"

@pytest.fixture
def db():
    # Her testten önce temiz bir veritabanı başlat
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    db = TaskDatabase(db_path=TEST_DB)
    yield db
    db.close()
    os.remove(TEST_DB)

# Test 1: Geçerli görevleri eklemek
def test_add_task(db):
    print("Testing add_task() function.")
    
    tasks_before = db.get_all_tasks()
    assert len(tasks_before) == 0, "Veritabanı başlangıçta boş olmalı."

    db.add_task("Test görev 1")
    db.add_task("Test görev 2")

    tasks_after = db.get_all_tasks()
    assert len(tasks_after) == 2, "İki görev eklendikten sonra görev sayısı 2 olmalı."

    assert tasks_after[0][1] == "Test görev 1", "İlk görev açıklaması doğru olmalı."
    assert tasks_after[1][1] == "Test görev 2", "İkinci görev açıklaması doğru olmalı."

    print("✅ Test passed: add_task().")

# Test 2: Geçersiz verilerle görev eklemek
def test_add_task_invalid_data(db):
    print("Testing add_task() with invalid data.")

    task_id = db.add_task("")
    tasks_after = db.get_all_tasks()
    assert all(task[1] != "" for task in tasks_after), "Boş görev eklenmemeli."

    print("✅ Test passed: add_task_invalid_data().")


# Test 3: Boş veritabanı durumu
def test_empty_database(db):
    print("Testing empty database.")
    
    tasks = db.get_all_tasks()
    assert len(tasks) == 0, "Veritabanı boş olmalı."
    
    print("✅ Test passed: Empty database.")

# Test 4: Büyük veri seti eklemek
def test_large_data_set(db):
    print("Testing large data set.")

    # 1000 görev ekleyelim
    for i in range(1000):
        db.add_task(f"Test görev {i + 1}")

    tasks_after = db.get_all_tasks()
    assert len(tasks_after) == 1000, "Veritabanına 1000 görev eklenmeli."

    print("✅ Test passed: Large data set.")

# Test 5: Veritabanı bağlantı hatası
@pytest.fixture
def invalid_db():
    invalid_db_path = "invalid_folder/invalid_path.db"  # klasör de hatalı olmalı
    db = TaskDatabase(db_path=invalid_db_path)
    yield db
    db.close()


def test_database_connection_error():
    invalid_path = "invalid_folder/invalid_path.db"
    
    # Klasör yoksa hata beklenmeli
    with pytest.raises(Exception) as excinfo:
        TaskDatabase(db_path=invalid_path)
    
    assert "Veritabanı bağlantısı hatalı" in str(excinfo.value)

    print("✅ Test passed: Database connection error.")

# Test 6: Görev tamamla işlevini test etme
def test_complete_task(db):
    print("Testing complete_task() function.")

    task1_id = db.add_task("Test görev 1")
    task2_id = db.add_task("Test görev 2")

    db.complete_task(task1_id)

    tasks_after = db.get_all_tasks()
    assert tasks_after[0][0] == task1_id
    assert tasks_after[0][2] == 1, "Görev 1 tamamlanmış olmalı."  # 1 olarak kontrol et
    assert tasks_after[1][2] == 0, "Görev 2 tamamlanmamış olmalı."

    print("✅ Test passed: complete_task().")
