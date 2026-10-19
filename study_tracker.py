tasks = []

while True:
    print("\n===== STUDY TRACKER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

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
        print("Goodbye!")
        break

    else:
        print("Invalid option")