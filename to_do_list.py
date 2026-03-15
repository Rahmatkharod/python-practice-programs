# Command Line To-Do List Application
# Features:
# 1. Add Task
# 2. View Tasks
# 3. Remove Task
# 4. Mark Task as Completed


# List to store tasks as dictionaries
# Example: {"Task": "study python", "status": "pending"}
to_do_list=[] 

def add_task():
    # Take task input from the user
    task = input("Enter the task to be added: ").lower()
    # Check if task already exists
    if any(task == d["Task"] for d in to_do_list):
        print("task already exists")
    else:
        # Add task with default status 'pending'
        to_do_list.append({"Task":task,"status":"pending"})
        print("Task added successfully")
       
def remove_task():
    # Check if the list contains any tasks
    if to_do_list:
        try:
            # Ask user for the task number to remove
            task = int(input("Enter the task number you want to delete "))
            # Convert task number to list index
            task-=1
            # Validate the index entered by the user
            if task < 0 or task >= len(to_do_list):
                print("oops! index out of range")
            else:
                # Remove task from list
                to_do_list.pop(task)
                print("task removed successfully")
        
        except ValueError:
            # Handle invalid input (non-integer values)
            print("Please enter a valid number") 
    else:
        # Message when list is empty
        print("To-Do-List is empty")
    

def view_task():
    # Check if tasks exist
    if to_do_list:
        # enumerate() is used to display task numbers starting from 1
        for index,task in enumerate(to_do_list,1):
            print(f"{index}. {task['Task']} -> {task['status']}")
    else:
        print("no task exists")

def task_completed():
    # Check if the list contains tasks
    if to_do_list:
        try:
            # Ask user for the task number to mark as completed
            task = int(input("Enter the task number you want to mark as completed "))
            # Convert task number to list index
            task -= 1
            # Validate index
            if task < 0 or task >= len(to_do_list):
                print("oops! index out of range")
                return
            else:
                # Update task status
                to_do_list[task]["status"] = "completed"
                print("task updated successfully")
        
        except ValueError:
            # Handle invalid input
            print("Please enter a valid number") 
    else:
        print("To-Do-List is empty")

def menu():
    # Main menu loop
    while(True):
        print()
        print("\n----MENU----")
        print("1. Add a task")
        print("2. View tasks")
        print("3. remove task")
        print("4. mark task as completed")
        print("5. exit")

        # User selects operation
        choice = input("Enter your choice: ")

        # Call corresponding function based on user choice
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            task_completed()
        elif choice == "5":
            print("Exiting...")
            exit()
        else:
            # Handle invalid menu choices
            print("Invalid choice. try again....")

# Entry point of the program
# Ensures menu() runs only when this script is executed directly
if __name__ == "__main__":
    menu()
