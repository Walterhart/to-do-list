import json
import uuid

class TodoList:
    def __init__(self, tasks_file='tasks.json'):
        self.tasks_file = tasks_file

    
    def read_tasks(self):
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

    def save_tasks(self, tasks):
        """Save tasks to the JSON file."""
        try:
            with open(self.tasks_file, 'w') as file:
                json.dump(tasks, file, indent=4)
        except IOError:
            print(f"Error saving tasks to {self.tasks_file}")

    def add_task(self, title, description):
        """Add a new task to the list."""
        if not title or not description:
            print("Title or description cannot be empty.")
            return
        
        tasks = self.read_tasks()

        if any(task['title'] == title for task in tasks):
            print(f"A task with the title '{title}' already exists. Please use a unique title.")
            return
        
        new_task = {
            'id': str(uuid.uuid4()),
            'title': title,
            'description': description,
            'complete': False
        }

        tasks.append(new_task)
        self.save_tasks(tasks)
        print(f"Task '{title}' added successfully.")  

    def delete_task(self, id):
        """Delete a task from the list by id."""
        tasks = self.read_tasks()

        if any(task['id'] == id for task in tasks):
            filtered_tasks = [task for task in tasks if task['id'] != id]
            self.save_tasks(filtered_tasks)
            print(f"Tasks with id '{id}' deleted successfully.")
        else:
            print(f"Task '{id}' not found.")

    def toggle_task(self, id):
        """Toggle completed by id."""
        tasks = self.read_tasks()

        for task in tasks:
            if(task['id'] == id):
                task['complete'] = not task['complete']
                self.save_tasks(tasks)
                print(f"Task {id} completion toggled to {task['complete']}.")
                return
        print(f"Task '{id}' not found.")
    
    def update_task(self, task_id, title=None, description=None):
        """Edit a task's title and/or description by id."""
        tasks = self.read_tasks()

        if title is not None and any(task['title'] == title and task['id'] != task_id for task in tasks):
            print(f"A task with the title '{title}' already exists. Please use a unique title.")
            return

        for task in tasks:
            if task['id'] == task_id:
                if title is not None:
                    task['title'] = title
                if description is not None:
                    task['description'] = description

                self.save_tasks(tasks)
                print(f"Task with ID '{task_id}' has been updated.")
                return
        print(f"Task with ID '{task_id}' not found.")

    def display_tasks(self):
        """ Display  all tasks """
        tasks = self.read_tasks()
        if not tasks:
            print("No tasks found!")
        for task in tasks:
            status = "Completed" if task['complete'] else "Not completed"
            print(f"ID: {task['id']}\nTitle: {task['title']}\nDescription: {task['description']}\nStatus: {status}\n")
            
todo_list = TodoList()
todo_list.display_tasks()
# todo_list.add_task("buy food", "I am hungry")
# todo_list.delete_task("62fe3ec0-16cd-415c-ad49-b91cd91c4620")
#todo_list.toggle_task("62fe3ec0-16cd-415c-ad49-b91cd91c4620")
# todo_list.update_task("62fe3ec0-16cd-415c-ad49-b91cd91c4620", "Food", "Updated description")