print("__To-Do-List__")
def menu():
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Remove all tasks")
    print("5. Remove completed tasks")
    print("6. Remove a specific task")
    print("7. Exit")
menu()
Tasks=[]
#add task
def add_task():
        task=input("Enter the task:")
        status=(input("Enter the status of the task (True/False):"))
        Tasks.append({"task":task,"done":status})
        main()
#view task
def view_task():
    if(Tasks==[]):
        print("No tasks available")
    else:
        for i in Tasks:
            print("Task:",i.get("task"),",Status:",i.get("done"))
    main()
#mark a task as completed
def mark_done():
    if(Tasks==[]):
        print("No tasks available")
        main()
    else:    
        task_number=int(input("Enter the task number you want to mark as completed:"))
        task_index=task_number-1
        if 0 <= task_index < len(Tasks):
            if Tasks[task_index].get("done") == "False":
                Tasks[task_index].update({"done": "True"})
                print("Task",task_number,"is updated succesfully")
            else:
                print("Task is already completed")
        else:
            print("Invalid task number")
    main()
#remove task
def remove_all_tasks():
    if Tasks:
        Tasks.clear()
        print("all tasks are removed")
    else:
        print("no tasks to remove")
    main()
def remove_completed_tasks():
    if Tasks:
        for i in Tasks:
            if(i.get("done")=="True"):
                    Tasks.remove(i)
        print("Completed tasks are removed")
    else:
        print("No tasks to remove")
    main()
def remove_a_task():
    if(Tasks==[]):
        print("No tasks to remove")
        main()
    else:
        task_number=int(input("Enter task number to delete"))
        task_index=task_number-1
        if(0 <= task_index and task_index < len(Tasks)):
            for i in Tasks:
                if Tasks[task_index]==i:
                    Tasks.remove(i)
            print("Task",task_number,"is deleted")
        else:
            print("Invalid Task number")
    main()
#exit
import sys
def exit_program():
    print("exit_succesful")
    sys.exit()
def main():
    x=input("Enter your choice(1/2/3/4/5/6/7):")
    if(x=="1"):
        add_task()
    elif(x=="2"):
        view_task()
    elif(x=="3"):
        mark_done()
    elif(x=="4"):
        remove_all_tasks()
    elif(x=="5"):
        remove_completed_tasks()
    elif(x=="6"):
        remove_a_task()
    elif(x=="7"):
        exit_program()
    else:
        print("not a valid choice")
        return
main()
