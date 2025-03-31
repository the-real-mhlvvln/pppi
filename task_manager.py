class TaskManager:
    def __init__(self, storage):
        """
        Инициализация TaskManager с использованием DataStorage.
        :param storage: Экземпляр класса DataStorage для хранения задач.
        """
        self.storage = storage

    def add_task(self, title):
        """Добавление новой задачи."""
        tasks = self.storage.load_tasks()
        task_id = len(tasks) + 1
        new_task = {"id": task_id, "title": title, "completed": False}
        self.storage.add_task(new_task)
        return f"Задача '{title}' добавлена."

    def list_tasks(self):
        """Просмотр всех задач."""
        tasks = self.storage.load_tasks()
        if not tasks:
            return "Список задач пуст."
        result = "Список задач:\n"
        for task in tasks:
            status = "✓" if task["completed"] else "✗"
            result += f"{task['id']}. [{status}] {task['title']}\n"
        return result.strip()

    def complete_task(self, task_id):
        """Отметка задачи как выполненной."""
        tasks = self.storage.load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.storage.save_tasks(tasks)
                return f"Задача с ID {task_id} отмечена как выполненная."
        return f"Задача с ID {task_id} не найдена."

    def delete_task(self, task_id):
        """Удаление задачи."""
        tasks = self.storage.load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                self.storage.save_tasks(tasks)
                return f"Задача с ID {task_id} удалена."
        return f"Задача с ID {task_id} не найдена."

    def update_task(self, task_id, new_title):
        """Обновление названия задачи."""
        tasks = self.storage.load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["title"] = new_title
                self.storage.save_tasks(tasks)
                return f"Задача с ID {task_id} обновлена. Новое название: '{new_title}'."
        return f"Задача с ID {task_id} не найдена."