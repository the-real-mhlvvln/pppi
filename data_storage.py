import json
import os

class DataStorage:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path

    def load_tasks(self):
        """Загрузка задач из файла."""
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_tasks(self, tasks):
        """Сохранение задач в файл."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)