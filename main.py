from todolist import TodoList

def display_menu():
    print("\nMenu:")
    print("1. Display all tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Toggle task completion")
    print("5. Update a task")
    print("6. Exit")

def main():
    todo_list = TodoList()
    while True:
        display_menu()
        choice = input("Enter a options: ")
        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            title = input("Enter title name: ")
            description = input("Enter description: ")
            todo_list.add_task(title, description)
        elif choice == '3':
             task_id = input("Enter task id to delete: ")
             todo_list.delete_task(task_id)
        elif choice == '4':
            task_id = input("Enter task id to toggle completion: ")
            todo_list.toggle_task(task_id)
        elif choice == '5':
            task_id = input("Enter id of which task to update: ")
            task_title = input("Enter task title or leave blank to not change title: ")
            task_description = input("Enter task description or leave blank to not change description: ")
            todo_list.update_task(task_id, task_title or None, task_description or None)
        elif choice == '6':
            print("Exiting the application")
            break
        else:
            print("Invalid choice please try again")
     
if __name__ == "__main__":
    main()