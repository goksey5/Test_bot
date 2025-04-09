import sqlite3
import pytest
from task_manager_bot.database import TaskDatabase  # Veritabanı sınıfınızı içe aktarın

@pytest.fixture
def setup_db():
    """Her testten önce veritabanı bağlantısını kurar ve temizler"""
    test_db_path = 'test_tasks.db'  # Dosya yolu kullanılıyor
    task_db = TaskDatabase(db_path=test_db_path)  # Veritabanı sınıfını bu şekilde başlatıyoruz
    task_db.delete_all_tasks()  # Veritabanını temizler
    yield task_db  # Test için db nesnesini sağlar
    task_db.delete_all_tasks()  # Testten sonra veritabanını temizler
    task_db.close()  # Veritabanı bağlantısını kapat

def test_get_completed_tasks(setup_db):
    """Tamamlanmış görevlerin doğru şekilde alındığını test edelim"""
    
    task_db = setup_db  # Test setup'ı kullanıyoruz

    # Başlangıçta tamamlanmış görev olmamalı
    completed_tasks = task_db.get_completed_tasks()
    assert len(completed_tasks) == 0, "Başlangıçta tamamlanmış görev bulunmamalı."

    # Test: İki görev ekleyelim
    task_db.add_task("Test task 1")
    task_db.add_task("Test task 2")
    
    # Birini tamamla
    task_db.complete_task(1)

    # Tamamlanmış görevleri alalım
    completed_tasks = task_db.get_completed_tasks()

    # Test Sonucu: Tamamlanmış görevlerin sayısı doğru olmalı
    assert len(completed_tasks) == 1, "Tamamlanmış görev sayısı yanlış."

    # Test Sonucu: Görev açıklamaları doğru olmalı
    expected_description = "Test task 1"
    assert completed_tasks[0][1] == expected_description, f"Beklenen açıklama: {expected_description}, Bulunan: {completed_tasks[0][1]}"
