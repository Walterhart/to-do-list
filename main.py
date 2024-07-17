import json
import uuid
tasks_file = 'tasks.json'

def read_tasks():
    """Read tasks from the JSON file."""
    try:
        with open(tasks_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found. Creating file...")
        return []
    

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with open(tasks_file, 'w') as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print(f"Error saving tasks to {tasks_file}")



def add_task(title, description):
    """Add a new task to the list."""
    if not title or not description:
        print("Title or description cannot be empty.")
        return
    
    tasks = read_tasks()

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
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")

def delete_task(id):
    """Delete a task from the list by id."""
    tasks = read_tasks()

    if any(task['id'] == id for task in tasks):
        filtered_tasks = [task for task in tasks if task['id'] != id]
        save_tasks(filtered_tasks)
        print(f"Tasks with id '{id}' deleted successfully.")
    else:
        print(f"Task '{id}' not found.")

def complete_task(id):
    """Mark a task as completed by id."""
    tasks = read_tasks()

    for task in tasks:
        if(task['id'] == id):
            task['complete'] = True
            save_tasks(tasks)
            print(f"Task has been mark completed")
            return
    print(f"Task '{id}' not found.")

def update_task(task_id, title=None, description=None):
    """Edit a task's title and/or description by id."""
    tasks = read_tasks()

    if title is not None and any(task['title'] == title and task['id'] != task_id for task in tasks):
        print(f"A task with the title '{title}' already exists. Please use a unique title.")
        return

    for task in tasks:
        if task['id'] == task_id:
            if title is not None:
                task['title'] = title
            if description is not None:
                task['description'] = description

            save_tasks(tasks)
            print(f"Task with ID '{task_id}' has been updated.")
            return
    print(f"Task with ID '{task_id}' not found.")


#add_task("buy food2","I am hungry broooo")
#delete_task("2db007c3-2621-4d4e-a4c0-bf8af0abf411") 
#complete_task("2db007c3-2621-4d4e-a4c0-bf8af0abf411")
update_task("2db007c3-2621-4d4e-a4c0-bf8af0abf411", "FOoood","Gj u updatedz??")


