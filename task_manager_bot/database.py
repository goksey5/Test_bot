import sqlite3
import os

class TaskDatabase:
    def __init__(self, db_path=None):
        """Veritabanı bağlantısını kurar."""
        if db_path is None:
            # Bu dosyanın bulunduğu klasörde 'tasks.db' adlı veritabanını kullan
            db_path = os.path.join(os.path.dirname(__file__), 'tasks.db')
        self.db_path = db_path

        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            raise Exception("Veritabanı bağlantısı hatalı") from e

        # Tabloyu oluştur (yoksa)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                                id INTEGER PRIMARY KEY,
                                description TEXT,
                                completed BOOLEAN)''')
        self.connection.commit()


    def add_task(self, description):
        """Yeni görev ekler."""
        if not description.strip():
             raise ValueError("Görev açıklaması boş olamaz.")
        
        self.cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (description, False))
        self.connection.commit()
        return self.cursor.lastrowid 
    
    def delete_task(self, task_id):
        """Görevi ID'sine göre siler."""
        self.cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        self.connection.commit()

    def complete_task(self, task_id):
        """Görevi tamamlanmış olarak işaretler."""
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id=?", (task_id,))
        self.connection.commit()
         # Görev sayısını terminale yaz
        self.cursor.execute("SELECT COUNT(*) FROM tasks")
        total = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT COUNT(*) FROM tasks WHERE completed = 1")
        completed = self.cursor.fetchone()[0]

        print(f"✅ Şu anda {completed} görev tamamlandı. Toplam görev sayısı: {total}")

    def get_all_tasks(self):
        """Tüm görevleri getirir."""
        self.cursor.execute("SELECT id, description, completed FROM tasks")
        return self.cursor.fetchall()

    def get_completed_tasks(self):
        """Tamamlanmış görevleri getirir."""
        self.cursor.execute("SELECT id, description FROM tasks WHERE completed = 1")
        return self.cursor.fetchall()

    def delete_all_tasks(self):
        """Tüm görevleri siler."""
        self.cursor.execute("DELETE FROM tasks")
        self.connection.commit()

    def close(self):
        """Veritabanı bağlantısını kapatır."""
        self.connection.close()
