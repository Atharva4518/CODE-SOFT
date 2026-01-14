def task():
    tasks = []
    print("-----WELCOME TO THE TO DO LIST MANAGER-----")


    total_task = int(input("ENTER THE NO. OF TASK TO ADD:- "))
    for i in range(1,total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    
    print(f"Today's task are {tasks}")


    while True:
        operation = int(input("Enter 1 to Add\n Enter 2 to update\n Enter 3 to Delete\n Enter 4 to "
        "view\n Enter 5 to Exit.."))
    

        if operation == 1:
            add = input("Enter the task you want to add =")
            tasks.append(add)
            print(f"Task {add} has been successfully aded.")

        elif operation == 2:
            update = input("Enter the task you want to update =")
            if update in tasks:
                new = input("Enter new task ")
                new1 = tasks.index(update)
                tasks[new1] = new
                print(f"Updated task {new}")

        elif operation == 3:
            delete = input("Enter the task you want to delete:- ")
            if delete in tasks:
                new2 = tasks.index(delete)
                del tasks[new2]
                print(f"Task {delete} has been deleted.")
            else:
                print("The task is not in list..")
        
        
        elif operation ==4:
            print(f"Total task = {tasks}")

        elif operation == 5 or "exit" or "Exit":
            print("BEST OF LUCK")
            print("YOU CAN COMPLETE ALL TASKS>>")
            break

task()
