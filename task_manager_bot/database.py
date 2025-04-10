import sqlite3

class TaskDatabase:
    def __init__(self, db_path="tasks.db"):
        self.db_path = db_path
        try:
            self.conn = sqlite3.connect(self.db_path)
            self._create_tasks_table()
        except Exception as e:
            raise Exception("Veritabanı bağlantısı hatalı.")

    def _create_tasks_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    completed BOOLEAN NOT NULL DEFAULT 0
                )
            """)

    def add_task(self, description):
        if not description:
            return None
        with self.conn:
            cursor = self.conn.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
            return cursor.lastrowid

    def delete_task(self, task_id):
        if not isinstance(task_id, int):
            raise ValueError("Görev ID'si geçerli bir tamsayı olmalıdır.")
        with self.conn:
            self.conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    def complete_task(self, task_id):
        with self.conn:
            self.conn.execute(
                "UPDATE tasks SET completed = 1 WHERE id = ?",
                (task_id,)
            )

    def get_all_tasks(self):
        cursor = self.conn.execute("SELECT id, description, completed FROM tasks")
        return cursor.fetchall()

    def get_task_by_id(self, task_id):
        cursor = self.conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        return cursor.fetchone()

    def get_completed_tasks(self):
        cursor = self.conn.execute("SELECT id, description FROM tasks WHERE completed = 1")
        return cursor.fetchall()

    def delete_all_tasks(self):
        with self.conn:
            self.conn.execute("DELETE FROM tasks")

    def close(self):
        self.conn.close()
