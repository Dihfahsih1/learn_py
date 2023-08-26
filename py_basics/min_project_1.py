# To-Do List Mini-Project

# Initialize an empty list to store tasks
todo_list = []

def add_task(task):
    todo_list.append({'task': task, 'completed': False})
    print(f"Task '{task}' added to the to-do list.")

def view_tasks():
    print("To-Do List:")
    for index, task_info in enumerate(todo_list, start=1):
        status = "Completed" if task_info['completed'] else "Not Completed"
        print(f"{index}. {task_info['task']} - {status}")

def mark_completed(task_index):
    if 1 <= task_index <= len(todo_list):
        todo_list[task_index - 1]['completed'] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def remove_completed():
    global todo_list
    todo_list = [task for task in todo_list if not task['completed']]
    print("Completed tasks removed.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Completed Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            mark_completed(task_index)
        elif choice == '4':
            remove_completed()
        elif choice == '5':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
