# Let's make a to do list app with Python

# Adding the tasks 
# view the all tasks
# Delete the task
# Exit the app

# First we work on adding the tasks

# To keep app running until User quits

tasks = []
file_path = "Todo_data.txt"
with open(file_path, "r") as file:
    data = file.readlines()
task_list = [line.strip() for line in data if line.strip()]
while True:
    print("\n")
    print("---------------TO DO list app------------------")
    print(" 1. Task Entry\n 2. View all tasks \n 3. Delete the Task \n 4. Exit the app")
    ops = input("Enter the operation number:(1,2,3,4) - ")

    if ops == "1":
        while True:
            task = input("Enter the Task (Q to quit)- ").strip()
            if task.upper() == "Q":
                break
            elif task == "":
                print("Task cannot be Empty")
            else:
                tasks.append(task)
                print("Task has been added")
        
        task_list.extend(tasks) 


    elif ops == "2":
        if not task_list: # Empty List returns False
            print("The Task List is empty")
        else:
            serial = 1
            print("\n")
            print("You task list -- ")
            for x in task_list:
                print(f"{serial}. {x}")
                serial += 1

    
    elif ops == "3":
        if not task_list: # Empty List returns False
            print("The Task List is empty")
        else:
            serial = 1
            print("\n")
            print("You task list -- ")
            for x in task_list:
                print(f"{serial}. {x}")
                serial += 1
            
            try:
                delete = (int(input("Enter task serial number to delete: ")) - 1)
                if delete >= len(task_list) or delete < 0:
                    print(f"{delete} - is beyond the scope of the Task list")
                else:
                    print(f"{task_list[delete]} - Task has been deleted")
                    task_list.pop(delete)
            except ValueError:
                print("Please Enter the valid task number")
    
    
    elif ops == "4":
        with open(file_path, "w") as file:
            for line in task_list:
                file.write(line + "\n")
        break


    else:
        print(f"{ops} is invalid Operation.")

print("You have exited the app")


# Deep seek R1 - code
'''
# Simple To-Do List App with File Persistence

def save_tasks(file_path, task_list):
    """Save tasks to a file."""
    with open(file_path, "w") as file:
        for task in task_list:
            file.write(task + "\n")

def load_tasks(file_path):
    """Load tasks from a file, handle missing files."""
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        return []

# Configuration
FILE_PATH = "todo_data.txt"
task_list = load_tasks(FILE_PATH)

# Main app loop
while True:
    print("\n" + "-" * 40)
    print("TO-DO LIST MANAGER")
    print("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    # Add Task
    if choice == "1":
        while True:
            task = input("Enter task (Q to return to menu): ").strip()
            if task.upper() == "Q":
                break
            if not task:
                print("Error: Task cannot be empty!")
                continue
            task_list.append(task)
            save_tasks(FILE_PATH, task_list)  # Save immediately
            print(f"'{task}' added successfully!")
    
    # View Tasks
    elif choice == "2":
        if not task_list:
            print("Your to-do list is empty!")
        else:
            print("\nYOUR TASKS:")
            for i, task in enumerate(task_list, 1):
                print(f"{i}. {task}")
    
    # Delete Task
    elif choice == "3":
        if not task_list:
            print("Your to-do list is empty!")
            continue
            
        print("\nYOUR TASKS:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")
            
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(task_list):
                deleted_task = task_list.pop(task_num - 1)
                save_tasks(FILE_PATH, task_list)  # Save immediately
                print(f"'{deleted_task}' deleted successfully!")
            else:
                print(f"Invalid number: {task_num}. Choose 1-{len(task_list)}")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # Exit
    elif choice == "4":
        print("Saving tasks... Goodbye!")
        break
    
    # Invalid Choice
    else:
        print(f"Invalid choice: '{choice}'. Please choose 1-4")

# Final save before exit (redundant but safe)
save_tasks(FILE_PATH, task_list)
'''