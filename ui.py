from task_manager import TaskManager
from data_storage import DataStorage

def main():
    storage = DataStorage()
    manager = TaskManager()
    manager.tasks = storage.load_tasks()  # Загрузка задач при старте

    while True:
        print("\n=== Планировщик задач ===")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название задачи: ")
            print(manager.add_task(title))

        elif choice == "2":
            print(manager.list_tasks())

        elif choice == "3":
            task_id = int(input("Введите ID задачи для отметки: "))
            print(manager.complete_task(task_id))

        elif choice == "4":
            task_id = int(input("Введите ID задачи для удаления: "))
            print(manager.delete_task(task_id))

        elif choice == "5":
            storage.save_tasks(manager.tasks)  # Сохранение задач перед выходом
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()