import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                label TEXT,
                task TEXT,
                status TEXT,
                priority TEXT,
                person TEXT,
                start_date TEXT,
                due_date TEXT,
                task_finished INTEGER
            )
        """)

    def insert_task(self, label, task, status, priority, person, start_date, due_date, task_finished):
        self.cursor.execute("""
            INSERT INTO tasks (label, task, status, priority, person, start_date, due_date, task_finished)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            label, task, status, priority, person, start_date, due_date, task_finished
        ))

    def fetch_all_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()

    def update_task(self, task_id, label, task, status, priority, person, start_date, due_date, task_finished):
        self.cursor.execute("""
            UPDATE tasks
            SET label=?, task=?, status=?, priority=?, person=?, start_date=?, due_date=?, task_finished=?
            WHERE id=?
        """, (
            label, task, status, priority, person, start_date, due_date, task_finished, task_id
        ))

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))

if __name__ == "__main__":
    # Exemple d'utilisation
    db_file = "tasks.db"
    with DatabaseManager(db_file) as db:
        db.create_table()
  #      db.insert_task("Travail", "Test", "En cours", "P1", "", "test","2023-10-05", "2023-10-10", 0)
  #      tasks = db.fetch_all_tasks()
  #      print("Tasks:")
  #      for task in tasks:
  #          print(task)
