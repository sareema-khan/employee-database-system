print("================================")
print(" TO-DO LIST MANAGEMENT SYSTEM")
print("================================")

# list to store tasks
tasks = []


# FUNCTION TO ADD TASK
def add_task():

    # user enters task title
    title = input("Enter task title: ")

    # creating task dictionary
    task = {
        "title": title,
        "completed": False
    }

    # adding task into task list
    tasks.append(task)

    print("Task added successfully!\n")


# FUNCTION TO VIEW TASKS
def view_tasks():

    # checking if task list is empty
    if len(tasks) == 0:
        print("No tasks available.\n")

    else:

        print("\n===== YOUR TASKS =====")

        # loop through all tasks
        for index, task in enumerate(tasks, start=1):

            # checking task status
            status = "Done" if task["completed"] else "Pending"

            print(f"{index}. {task['title']} - {status}")

        print()



# FUNCTION TO COMPLETE TASK
def complete_task():

    # showing tasks
    view_tasks()

    # if no tasks return
    if len(tasks) == 0:
        return

    # asking user for task number
    task_number = int(input("Enter task number to mark complete: "))

    # validating task number
    if 1 <= task_number <= len(tasks):

        # marking task completed
        tasks[task_number - 1]["completed"] = True

        print("Task marked as completed!\n")

    else:
        print("Invalid task number.\n")


# FUNCTION TO DELETE TASk
def delete_task():

    # showing tasks
    view_tasks()

    # if no tasks return
    if len(tasks) == 0:
        return

    # asking task number
    task_number = int(input("Enter task number to delete: "))

    # checking valid task number
    if 1 <= task_number <= len(tasks):

        # removing task from list
        removed_task = tasks.pop(task_number - 1)

        print(f"Task '{removed_task['title']}' deleted successfully!\n")

    else:
        print("Invalid task number.\n")



# FUNCTION TO UPDATE TASK
def update_task():

    # showing tasks
    view_tasks()

    # if list empty return
    if len(tasks) == 0:
        return

    # asking task number
    task_number = int(input("Enter task number to update: "))

    # validating task number
    if 1 <= task_number <= len(tasks):

        # taking new title
        new_title = input("Enter new task title: ")

        # updating task title
        tasks[task_number - 1]["title"] = new_title

        print("Task updated successfully!\n")

    else:
        print("Invalid task number.\n")


# MAIN PROGRAM LOOP
while True:

    print("===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Update Task")
    print("6. Exit")

    # taking user choice
    choice = input("Enter your choice: ")


    # MENU CONDITIONS

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        update_task()

    elif choice == "6":
        print("Exiting To-Do List System...")
        break

    else:
        print("Invalid choice. Please try again.\n")