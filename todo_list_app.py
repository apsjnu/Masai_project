# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:57:29 2025

@author: hp
"""

import os

# Define the file to store tasks
tasks_file = "tasks.txt"

def load_tasks():
    """
    Load tasks from the file.
    
    Returns:
        list: A list of tasks, where each task is a dictionary.
    """
    tasks = []
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) == 4:
                    tasks.append({
                        "id": parts[0],
                        "description": parts[1],
                        "deadline": parts[2],
                        "status": parts[3]
                    })
    return tasks

def save_tasks(tasks):
    """
    Save tasks to the file.
    
    Args:
        tasks (list): A list of tasks, where each task is a dictionary.
    """
    with open(tasks_file, "w") as file:
        for task in tasks:
            file.write(f"{task['id']}, {task['description']}, {task['deadline']}, {task['status']}\n")

def add_task(tasks):
    """
    Add a new task.
    
    Args:
        tasks (list): A list of tasks, where each task is a dictionary.
    """
    task_id = str(len(tasks) + 1)
    description = input("Enter task description: ")
    deadline = input("Enter task deadline (YYYY-MM-DD): ")
    tasks.append({"id": task_id, "description": description, "deadline": deadline, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully.")

def edit_task(tasks):
    """
    Edit an existing task.
    
    Args:
        tasks (list): A list of tasks, where each task is a dictionary.
    """
    task_id = input("Enter the Task ID to edit: ")
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = input(f"Enter new description (current: {task['description']}): ") or task["description"]
            task["deadline"] = input(f"Enter new deadline (current: {task['deadline']}): ") or task["deadline"]
            save_tasks(tasks)
            print("Task updated successfully.")
            return
    print("Task not found.")

def delete_task(tasks):
    """
    Delete a task.
    
    Args:
        tasks (list): A list of tasks, where each task is a dictionary.
    """
    task_id = input("Enter the Task ID to delete: ")
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully.")
            return
    print("Task not found.")

def mark_completed(tasks):
    """
    Mark a task as completed.
    
    Args:
        tasks (list): A list of tasks, where each task is a dictionary.
    """
    task_id = input("Enter the Task ID to mark as completed: ")
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed.")
            return
    print("Task not found.")

def display_tasks(tasks):
    """
    Display all tasks.
    
    Args:
        tasks (list): A list of tasks, where each task is a dictionary.
    """
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Deadline: {task['deadline']}, Status: {task['status']}")

def main():
    """
    Main function to run the To-Do List application.
    """
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. View All Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            edit_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            display_tasks(tasks)
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
