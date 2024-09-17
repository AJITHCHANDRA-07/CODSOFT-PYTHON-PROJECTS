# To-Do List Application

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "pending"})
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['task']} - {task['status']}")

    def update_task(self, task_number, new_task):
        try:
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task {task_number} updated successfully!")
        except IndexError:
            print("Invalid task number.")

    def mark_as_done(self, task_number):
        try:
            self.tasks[task_number - 1]["status"] = "done"
            print(f"Task {task_number} marked as done!")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            print(f"Task {task_number} deleted successfully!")
        except IndexError:
            print("Invalid task number.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            to_do_list.add_task(task)
        elif choice == "2":
            to_do_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            to_do_list.update_task(task_number, new_task)
        elif choice == "4":
            task_number = int(input("Enter the task number to mark as done: "))
            to_do_list.mark_as_done(task_number)
        elif choice == "5":
            task_number = int(input("Enter the task number to delete: "))
            to_do_list.delete_task(task_number)
        elif choice == "6":
            print("Exiting To-Do List Application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()