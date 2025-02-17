def todo_list_app():
    tasks = []
    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the new task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully.")
        
        elif choice == '2':
            if not tasks:
                print("No tasks in the list.")
            else:
                print("\nCurrent Tasks:")
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")
        
        elif choice == '3':
            if not tasks:
                print("No tasks to delete.")
            else:
                try:
                    task_number = int(input("Enter the task number to delete: "))
                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' deleted.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        
        elif choice == '4':
            print("Exiting To-Do List Application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

todo_list_app()
