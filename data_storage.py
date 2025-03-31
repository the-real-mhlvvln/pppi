import json
import os

class DataStorage:
    def __init__(self, file_path="tasks.json"):
        """
        :param file_path:
        """
        self.file_path = file_path

    def load_tasks(self):
        """
        Загружаем таски
        :return:
        """
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Ошибка: Файл поврежден или содержит некорректные данные.")
            return []

    def save_tasks(self, tasks):
        """
        Сохраняем таски
        :param tasks:
        :return:
        """
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(tasks, file, ensure_ascii=False, indent=4)
        except IOError:
            print("Ошибка: Не удалось сохранить задачи в файл.")

    def add_task(self, task):
        """Добавление новой задачи."""
        tasks = self.load_tasks()
        tasks.append(task)
        self.save_tasks(tasks)

    def remove_task(self, task_id):
        """Удаление задачи по ID."""
        tasks = self.load_tasks()
        tasks = [task for task in tasks if task.get("id") != task_id]
        self.save_tasks(tasks)

    def update_task(self, task_id, updated_data):
        """Обновление задачи по ID."""
        tasks = self.load_tasks()
        for task in tasks:
            if task.get("id") == task_id:
                task.update(updated_data)
                break
        self.save_tasks(tasks)

    def get_task_by_id(self, task_id):
        """
        Получить таски по id
        :param task_id:
        :return:
        """
        tasks = self.load_tasks()
        for task in tasks:
            if task.get("id") == task_id:
                return task
        return None