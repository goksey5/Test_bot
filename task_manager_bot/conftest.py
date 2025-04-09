import os
import pytest
from database import TaskDatabase

# Her testten önce veritabanı dosyasını sil
@pytest.fixture(autouse=True)
def clean_test_db():
    db_path = "test_tasks.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    yield  # test çalıştıktan sonra devam eder
    if os.path.exists(db_path):
        os.remove(db_path)

# Her test için db nesnesi oluşturur ve test sonunda kapatır
@pytest.fixture
def db():
    db = TaskDatabase("test_tasks.db")
    yield db
    db.conn.close()
