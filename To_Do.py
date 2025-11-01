def task():
    tasks = []
    print("--------Welcome to thr To-Do List App!-------")
    
    total_tasks = int (input("Enter the number of tasks you want to add: "))
    for i in range(1, total_tasks+1):
        task_name = input(f"Enter the task {i} : ")
        tasks.append(task_name)
        
    print(f"Today's Tasks are\n {tasks}") 
    
    while True:
        operations = int(input(
        "\nChoose an operation:\n"
        "1. Add Task\n"
        "2. Update Task\n"
        "3. Delete Task\n"
        "4. View Tasks\n"
        "5. Exit/Stop\n "
    ))
        
        if operations == 1:
            add = input("Enter the task to add : ")
            tasks.append(add)
            print(f"Task '{add}'  has been added successfully.")
            
        elif operations == 2:
            updated_value = input("Enter the task number to update : ")
            if updated_value in tasks:
                up = input("Enter the new task : ")
                ind = tasks.index(updated_value)
                tasks[ind] = up
                print(f"updated task {up}")  
        
        elif operations == 3:
            del_value = input("Enter the task number to delete : ")
            if del_value in tasks:
                ind = tasks.index(del_value)
                del tasks[ind]
                print(f"Deleted task {del_value}")
            
        elif operations == 4:
            print(f"Today's Tasks are\n {tasks}")
        
        elif operations == 5:
            print("Closing the To-Do List App. Goodbye!")
            break
            
        else:
            print("Invalid operation. Please choose a valid option.")
            break 
        
if __name__ == "__main__":
    task()