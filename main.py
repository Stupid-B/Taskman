from datetime import datetime

class Task:
    def __init__(self, name: str, description: str, status: str = "to-do"):
        self.name = name
        self.description = description
        self.status = status
        self.createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updatedAt = self.createdAt

    def update_status(self, new_status: str):
        self.status = new_status
        self.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Task: {self.name}\nDescription: {self.description}\nStatus: {self.status}\nCreated: {self.createdAt}\nLast Updated: {self.updatedAt}\n"

class TaskManager:
    def __init__(self):
        self.active_tasks = {}  # Tasks that are to-do or on-going
        self.completed_tasks = {}  # Tasks that are done

    def add_task(self, name: str, description: str, status: str = "to-do") -> Task:
        if name in self.active_tasks or name in self.completed_tasks:
            return None  # Task name must be unique
        task = Task(name, description, status)
        if status == "done":
            self.completed_tasks[name] = task
        else:
            self.active_tasks[name] = task
        return task

    def get_task(self, name: str) -> Task:
        return self.active_tasks.get(name) or self.completed_tasks.get(name)

    def list_active_tasks(self):
        if not self.active_tasks:
            print("No active tasks found!")
            return
        print("\n=== Active Tasks ===")
        for task in self.active_tasks.values():
            print(task)
            print("-" * 50)

    def list_completed_tasks(self):
        if not self.completed_tasks:
            print("No completed tasks found!")
            return
        print("\n=== Completed Tasks ===")
        for task in self.completed_tasks.values():
            print(task)
            print("-" * 50)

    def update_task_status(self, name: str, new_status: str):
        task = self.active_tasks.get(name) or self.completed_tasks.get(name)
        if not task:
            return False

        task.update_status(new_status)
        
        # Move task between lists if needed
        if new_status == "done":
            if name in self.active_tasks:
                self.completed_tasks[name] = self.active_tasks.pop(name)
        else:
            if name in self.completed_tasks:
                self.active_tasks[name] = self.completed_tasks.pop(name)
        
        return True

def main():
    manager = TaskManager()
    
    while True:
        print("\n=== Task Manager Menu ===")
        print("1. Add New Task")
        print("2. List Active Tasks")
        print("3. List Completed Tasks")
        print("4. Update Task Status")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            print("\nAvailable status options: to-do, on-going, done")
            status = input("Enter task status (default: to-do): ").lower() or "to-do"
            
            task = manager.add_task(name, description, status)
            if task:
                print("\nTask added successfully!")
                print(task)
            else:
                print("\nError: Task name already exists!")
            
        elif choice == "2":
            manager.list_active_tasks()
            
        elif choice == "3":
            manager.list_completed_tasks()
            
        elif choice == "4":
            if not (manager.active_tasks or manager.completed_tasks):
                print("\nNo tasks available to update!")
                continue
                
            print("\n=== Active Tasks ===")
            manager.list_active_tasks()
            print("\n=== Completed Tasks ===")
            manager.list_completed_tasks()
            
            name = input("\nEnter task name to update: ")
            print("\nAvailable status options: to-do, on-going, done")
            new_status = input("Enter new status: ").lower()
            
            if manager.update_task_status(name, new_status):
                print("\nTask status updated successfully!")
            else:
                print("\nTask not found!")
                
        elif choice == "5":
            print("\nThank you for using Task Manager!")
            break
            
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()

