
import os
import pytest
from task_manager_bot.database import TaskDatabase



TEST_DB = "test_tasks.db"

@pytest.fixture
def db():
    # Test veritabanı var mı kontrol et, varsa sil
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    
    # Yeni bir veritabanı oluştur
    db = TaskDatabase(db_path=TEST_DB)
    yield db
    # Test sonrası veritabanı dosyasını kapat ve sil
    db.close()
    os.remove(TEST_DB)

def test_delete_task(db):
    print("Testing delete_task() function.")
    
    # 1. Görev ekleyelim
    task1_id = db.add_task("Silinecek görev 1")
    task2_id = db.add_task("Kalacak görev 2")
    
    # 2. Eklenen görevlerin ID'lerini kontrol edelim
    assert isinstance(task1_id, int), "task1_id int olmalı"
    assert isinstance(task2_id, int), "task2_id int olmalı"
    
    # 3. Başlangıçta iki görev olduğundan emin olalım
    tasks_before = db.get_all_tasks()
    assert len(tasks_before) == 2, "Başlangıçta iki görev olmalı."
    
    # 4. Birini silelim
    db.delete_task(task1_id)
    
    # 5. Görev silindikten sonra veritabanındaki görevlerin durumunu kontrol edelim
    tasks_after = db.get_all_tasks()
    assert len(tasks_after) == 1, "Bir görev silindikten sonra yalnızca bir görev olmalı."
    assert tasks_after[0][1] == "Kalacak görev 2", "Doğru görev kalmalı."
    
    # 6. Silinen görevin ID'sinin hala var olup olmadığını kontrol edelim
    assert task1_id not in [task[0] for task in tasks_after], "Silinen görev veritabanında olmamalı."

    # Test sonucu mesajı (isteğe bağlı)
    print("✅ Test passed: delete_task().")
