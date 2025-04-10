import os
import sqlite3
import pytest
from task_manager_bot.database import TaskDatabase  # Veritabanı sınıfını içe aktar

# Test veritabanı dosyasının tam yolu
@pytest.fixture
def setup_db():
    """Her testten önce veritabanı bağlantısını kurar ve temizler."""
    test_db_path = os.path.join(os.path.dirname(__file__), 'test_tasks.db')  # Test veritabanı dosyasının yolu
    
    if os.path.exists(test_db_path):  # Test başlamadan önce mevcut test veritabanı dosyasını sil
        os.remove(test_db_path)

    task_db = TaskDatabase(db_path=test_db_path)  # Veritabanı sınıfını başlatıyoruz
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
    print("Test başladı: Başlangıçta tamamlanmış görev bulunmuyor.")

    # Test: İki görev ekleyelim
    task_db.add_task("Test task 1")
    task_db.add_task("Test task 2")
    
    # Birini tamamla
    task_db.complete_task(1)

    # Tamamlanmış görevleri alalım
    completed_tasks = task_db.get_completed_tasks()

    # Test Sonucu: Tamamlanmış görevlerin sayısı doğru olmalı
    assert len(completed_tasks) == 1, "Tamamlanmış görev sayısı yanlış."

    # Test Sonucu: Görev açıklamaları doğru şekilde eşleşiyor
    expected_description = "Test task 1"
    assert completed_tasks[0][1] == expected_description, f"Beklenen açıklama: {expected_description}, Bulunan: {completed_tasks[0][1]}"
    
    print("Test tamamlandı: Tamamlanmış görevler doğru şekilde alındı.")


def test_complete_task(setup_db):
    """Bir görev tamamlandığında veritabanının doğru şekilde güncellenip güncellenmediğini test edelim"""

    task_db = setup_db  # Test setup'ı kullanıyoruz

    # Başlangıçta tamamlanmış görev olmamalı
    completed_tasks = task_db.get_completed_tasks()
    assert len(completed_tasks) == 0, "Başlangıçta tamamlanmış görev bulunmamalı."
    print("Test başladı: Başlangıçta tamamlanmış görev bulunmuyor.")

    # Test: Bir görev ekleyelim
    task_db.add_task("Test task to complete")
    task_db.complete_task(1)

    # Test: Tamamlanmış görevleri kontrol edelim
    completed_tasks = task_db.get_completed_tasks()

    # Test Sonucu: Tamamlanmış görevlerin sayısı doğru olmalı
    assert len(completed_tasks) == 1, "Tamamlanmış görev sayısı yanlış."

    # Test Sonucu: Görev açıklamaları doğru şekilde eşleşmeli
    expected_description = "Test task to complete"
    assert completed_tasks[0][1] == expected_description, f"Beklenen açıklama: {expected_description}, Bulunan: {completed_tasks[0][1]}"
    
    print("Test tamamlandı: Görev tamamlandı olarak işaretlendi ve veritabanı güncellendi.")


def test_get_all_tasks(setup_db):
    """Tüm görevleri doğru şekilde alıp almadığını test edelim"""
    
    task_db = setup_db  # Test setup'ı kullanıyoruz

    # Başlangıçta tüm görevler boş olmalı
    all_tasks = task_db.get_all_tasks()
    assert len(all_tasks) == 0, "Başlangıçta görev bulunmamalı."
    print("Test başladı: Başlangıçta görev bulunmuyor.")

    # Test: Bir görev ekleyelim
    task_db.add_task("Test task 1")
    task_db.add_task("Test task 2")

    # Tüm görevleri alalım
    all_tasks = task_db.get_all_tasks()

    # Test Sonucu: Toplam görev sayısı doğru olmalı
    assert len(all_tasks) == 2, "Görev sayısı yanlış."

    # Test Sonucu: Görev açıklamaları doğru şekilde eşleşmeli
    expected_descriptions = ["Test task 1", "Test task 2"]
    actual_descriptions = [task[1] for task in all_tasks]
    assert actual_descriptions == expected_descriptions, f"Beklenen açıklamalar: {expected_descriptions}, Bulunan: {actual_descriptions}"

    print("Test tamamlandı: Görevler doğru şekilde alındı ve açıklamaları eşleşti.")
