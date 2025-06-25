#This function is use to add the tasks in the Todo text file...
def addTask():
    file = open("todo.txt","a+")
    file.seek(0)
    a=file.readlines()
    #Use to get the last record
    b= a[-1].split()
    if b[0]== "Sr.No.":
        i = 1
    else:
        #Getting last serial number...
        i = int(b[0])+1
    while True:
        task = input("Enter the task (or press enter to  stop): ")
        if task =="":
            break
        data = ["   "+str(i),"\t\t"+task+"\n"]
        file.writelines(data)
        i +=1 
    print("Adding the tasks is done!")
    file.close()
    
#This function used tho delete the task 
def removeTask():
    file = open("todo.txt", "r")
    lines = file.readlines()
    file.close()
    
    # Display all tasks
    for line in lines:
        print(line.strip())
    
    # Ask for the sr. no. that task want to remove
    inSerial = int(input("Enter the Serial No. which task you want to remove: "))
    
    found = False
    # Only search and remove in lines after the first line
    for i, line in enumerate(lines[1:], start=1):
        sr = line.split()
        if sr[0] == str(inSerial):
            print("Task found:", line.strip())
            del lines[i]  # Remove the task
            print("Task removed successfully.")
            found = True
            break
        
    if not found:
        print("Task with that serial number not found.")
    
    # Renumber the remaining tasks, keeping the first line unchanged
    updated_lines = [lines[0]]  # Keep the first line as is
    for idx, line in enumerate(lines[1:], start=1):
        parts = line.split(maxsplit=1)
        if len(parts) > 1:
            updated_lines.append(f"\t{idx} \t\t{parts[1]}")
        else:
            updated_lines.append(f"{idx}")
    
    file = open("todo.txt", "w")
    file.writelines(updated_lines)
    file.close()


def viewTasks():
    print('\n')
    print('----- Your Tasks -----')
    try:
        file = open("todo.txt", "r")
        tasks = file.readlines()
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(task.strip()+ "\n")
        else:
            print("No task found ! \n")
    except FileNotFoundError:
        print("Tasks File not found ! please start by adding a task \n")


while True:
    print('\n')
    print("===== To-Do List Menu =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        viewTasks()
    elif choice == "2":
        addTask()
    elif choice == "3":
        removeTask()
    elif choice == "4":
        break
    else:
        print("Invalid option. Please try again.\n")

