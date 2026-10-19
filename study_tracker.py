tasks = []

while True:
    print("\n===== STUDY TRACKER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        subject = input("Subject: ")
        task = input("Task: ")

        tasks.append(subject + " - " + task)

        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\n===== YOUR TASKS =====")

            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_number = int(input("Enter task number to complete: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1] += " [COMPLETED]"
                print("Task completed!")
            else:
                print("Invalid task number")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option")