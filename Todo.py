# Let's make a to do list app with Python

# Adding the tasks 
# view the all tasks
# Delete the task
# Exit the app

# First we work on adding the tasks

# To keep app running until User quits
task_list = []
while True:
    print("\n")
    print("---------------TO DO list app------------------")
    print(" 1. Task Entry\n 2. View all taks \n 3. Delete the Task \n 4. Exit the app")
    ops = input("Enter the operation number:(1,2,3,4) - ")

    if ops == "1":
        while True:
            task = input("Enter the Task (Q to quit)- ")
            if task.upper() == "Q":
                break
            else:
                task_list.append(task)

    elif ops == "2":
        serial = 1
        print("\n")
        print("You task list -- ")
        for x in task_list:
            print(f"{serial}. {x}")
            serial += 1

    
    elif ops == "3":
        serial = 1
        print("\n")
        print("You task list -- ")
        for x in task_list:
            print(f"{serial}. {x}")
            serial += 1
        
        delete = int(input("Enter task serial number to delete: "))
        task_list.pop(delete + 1)
    
    
    elif ops == "4":
        break

    else:
        print("Namaste anna")
        break

print("You have exited the app")