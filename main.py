import json
import uuid

class TodoList:
    def __init__(self, tasks_file='tasks.json'):
        self.tasks_file = tasks_file
        self.tasks = self._read_tasks()

    def _read_tasks(self):
        """Read tasks from the JSON file."""
        try:
            with open(self.tasks_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("File not found. Creating file...")
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON. Returning an empty list.")
            return []

    def _save_tasks(self):
        """Save tasks to the JSON file."""
        try:
            with open(self.tasks_file, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError:
            print(f"Error saving tasks to {self.tasks_file}")

    def add_task(self, title, description):
        """Add a new task to the list."""
        if not title or not description:
            print("Title or description cannot be empty.")
            return
        
        if any(task['title'] == title for task in self.tasks):
            print(f"A task with the title '{title}' already exists. Please use a unique title.")
            return
        
        new_task = {
            'id': str(uuid.uuid4()),
            'title': title,
            'description': description,
            'complete': False
        }

        self.tasks.append(new_task)
        self._save_tasks()
        print(f"Task '{title}' added successfully.")  

    def delete_task(self, id):
        """Delete a task from the list by id."""
        if any(task['id'] == id for task in self.tasks):
            self.tasks = [task for task in self.tasks if task['id'] != id]
            self._save_tasks()
            print(f"Tasks with id '{id}' deleted successfully.")
        else:
            print(f"Task '{id}' not found.")

    def toggle_task(self, id):
        """Toggle completed by id."""
        for task in self.tasks:
            if(task['id'] == id):
                task['complete'] = not task['complete']
                self._save_tasks()
                print(f"Task {id} completion toggled to {task['complete']}.")
                return
        print(f"Task '{id}' not found.")
    
    def update_task(self, task_id, title=None, description=None):
        """Edit a task's title and/or description by id."""
        if title is not None and any(task['title'] == title and task['id'] != task_id for task in self.tasks):
            print(f"A task with the title '{title}' already exists. Please use a unique title.")
            return

        for task in self.tasks:
            if task['id'] == task_id:
                if title is not None:
                    task['title'] = title
                if description is not None:
                    task['description'] = description

                self._save_tasks()
                print(f"Task with ID '{task_id}' has been updated.")
                return
        print(f"Task with ID '{task_id}' not found.")

    def display_tasks(self):
        """ Display  all tasks """
        if not self.tasks:
            print("No tasks found!")
        for task in self.tasks:
            status = "Completed" if task['complete'] else "Not completed"
            print(f"ID: {task['id']}\nTitle: {task['title']}\nDescription: {task['description']}\nStatus: {status}\n")
            

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