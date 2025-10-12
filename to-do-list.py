tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def view_task():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    view_task()
    if tasks:
        try:
            index = int(input("Enter the task number to remove: "))
            removed = tasks.pop(index - 1)
            print(f"Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a valid task number.")
    else:
        print("No tasks to remove.")

def save_to_pdf(filename="todo_list.pdf"):
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas

    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica", 16)
    c.drawString(100, 750, "My To-Do List")
    c.setFont("Helvetica", 12)

    y = 720
    for i, task in enumerate(tasks, 1):
        c.drawString(100, y, f"{i}. {task}")
        y -= 20

    c.save()
    print(f"To-Do List saved to {filename}")

def Exit():
    save_to_pdf()
while True:
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Save To PDF")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        save_to_pdf()
    elif choice == "5":
        Exit()
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")
