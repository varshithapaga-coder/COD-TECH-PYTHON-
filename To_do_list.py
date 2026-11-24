# TO-DO LIST - CODTECH TASK 2
# Intern ID: CT04DH2349

tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, 1):
                status = "Done ✅" if t["done"] else "Pending ⏳"
                print(f"{i}. {t['task']} - {status}")

    elif choice == "3":
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked as Done!")
        else:
            print("Invalid number!")

    elif choice == "4":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted!")
        else:
            print("Invalid number!")

    elif choice == "5":
        print("Goodbye! 👋")
        break

    else:
        print("Please choose 1 to 5 only!")
