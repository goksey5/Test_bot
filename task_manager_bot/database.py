import sqlite3

class TaskDatabase:
    def __init__(self, db_path='task_manager_bot/tests/test_tasks.db'):
        """Veritabanı bağlantısını kurar."""
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

        # Tabloyu oluşturuyoruz, eğer yoksa
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                                id INTEGER PRIMARY KEY,
                                description TEXT,
                                completed BOOLEAN)''')
        self.connection.commit()

    def add_task(self, description):
        """Yeni bir görev ekler."""
        self.cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (description, False))
        self.connection.commit()

    def complete_task(self, task_id):
        """Bir görevi tamamlanmış olarak işaretler."""
        self.cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (True, task_id))
        self.connection.commit()

    def get_completed_tasks(self):
        """Tamamlanmış görevleri alır."""
        self.cursor.execute("SELECT * FROM tasks WHERE completed = ?", (True,))
        return self.cursor.fetchall()

    def delete_all_tasks(self):
        """Tüm görevleri siler."""
        self.cursor.execute("DELETE FROM tasks")
        self.connection.commit()

    def close(self):
        """Veritabanı bağlantısını kapatır."""
        self.connection.close()
