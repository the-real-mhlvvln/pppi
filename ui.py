from task_manager import TaskManager
from data_storage import DataStorage

def main():
    # Инициализация хранилища и менеджера задач
    storage = DataStorage("tasks.json")
    manager = TaskManager(storage)

    while True:
        print("\n=== Планировщик задач ===")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Обновить задачу")
        print("6. Выход")

        choice = input("Выберите действие: ").strip()

        try:
            if choice == "1":
                title = input("Введите название задачи: ").strip()
                if not title:
                    print("Ошибка: Название задачи не может быть пустым.")
                    continue
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
                task_id = int(input("Введите ID задачи для обновления: "))
                new_title = input("Введите новое название задачи: ").strip()
                if not new_title:
                    print("Ошибка: Новое название задачи не может быть пустым.")
                    continue
                print(manager.update_task(task_id, new_title))

            elif choice == "6":
                print("До свидания!")
                break

            else:
                print("Неверный выбор. Попробуйте снова.")

        except ValueError:
            print("Ошибка: Введено некорректное значение. Пожалуйста, введите число.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()