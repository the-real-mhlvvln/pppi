class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        """Добавление новой задачи."""
        task_id = len(self.tasks) + 1
        self.tasks.append({"id": task_id, "title": title, "completed": False})
        return f"Задача '{title}' добавлена."

    def list_tasks(self):
        """Просмотр всех задач."""
        if not self.tasks:
            return "Список задач пуст."
        result = "Список задач:\n"
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            result += f"{task['id']}. [{status}] {task['title']}\n"
        return result.strip()

    def complete_task(self, task_id):
        """Отметка задачи как выполненной."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return f"Задача с ID {task_id} отмечена как выполненная."
        return f"Задача с ID {task_id} не найдена."

    def delete_task(self, task_id):
        """Удаление задачи."""
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return f"Задача с ID {task_id} удалена."
        return f"Задача с ID {task_id} не найдена."