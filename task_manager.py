import json

# Predefined dummy login credentials for testing
dummyEmail='tester@gmail.com'
dummyPassword='tester@123'


# Function for login
def login():
    print("Login to access task manager.")
    email=input("\nEnter the email: ")
    password=input("Enter the password: ")

    if email==dummyEmail and password==dummyPassword:
        print("\nLogin successful")
        return True
    else:
        print("\nInvalid email/password.Access Denied!!!")
        return False



# A class to represent each task
class Task:
    def __init__(self,id,title,completed=False):
        #Initialize each task with an id,title,completed status
        self.id=id             
        self.title=title
        self.completed=completed
    
    #Method to print task details
    def __str__(self):
        # return task details in string format
        return f"ID:{self.id},Title:{self.title},Completed:{self.completed}"
    

#Function to add new task to the list
def addTask(taskList,title):
    taskId=len(taskList)+1   # Set unique id based on the current count of tasks
    task=Task(taskId,title)  # Create a new Task object
    taskList.append(task)    # Add the new task to the list
    print('Task {} added with ID {}'.format(title,taskId))

#Function to view all the tasks
def viewTask(taskList):
    if not taskList:  # Check if task list is empty
        print('\nNo tasks available')
    else:
        for task in taskList:
            status="Done" if task.completed else "Pending"  # Show status as done or pending
            print(f'\n{task.id}. {task.title} - {status}')  # Print task details

#Function to delete a task 
def deleteTask(taskList,taskId):
    for task in taskList:   # Loop through  the task to find matching Id
        if task.id==taskId: # If the Id matches mark as completed
            taskList.remove(task)
            saveTasks(taskList)
            print(f'task Id {taskId} deleted successfully')
            return
    print('task not found') #If no matching id is found show an error

#Function to mark task as complete
def markTaskComplete(taskList,taskId):
    for task in taskList:   # Loop through  task list to find matching id
        if task.id==taskId: # if the id matches,mark as completed
            task.completed=True
            print(f'\ntask id {taskId} marked as complete')
            return
    print("\ntask not found") # if no matching id is found show an error


# Function to save the tasks to json file
def saveTasks(taskList,filename="tasks.json"):
    try:
        # Convert each task to a dictionary
        file=open(filename,'w')   #Open the file in write mode
        jsonData=([task.__dict__ for task in taskList]) # Prepare data to be saved
        json.dump(jsonData,file)  # write data to the file
        file.close()              # Close the file
        print("\nTask saved successfully")
    except Exception as e:
        print(f'Error saving tasks: {e}')  # handle file writing errors

# Function to load tasks from a Json File 
def loadTasks(filename="tasks.json"):
    taskList=[]
    try:
        # try to open and read the file
        file=open(filename,'r')
        data=json.load(file)
            # convert dictionary data back to task object
        for item in data:
            task=Task(**item)
            taskList.append(task) # add the task to task list
        file.close()
    except Exception as e:
        print("Error loading tasks:",e) # Print any error that occurs
    
    return taskList
    

# Main Function to run the task manager program

def main():
    # call the login function first
    if not login():
        return  #Exit if login fails

    taskList=[] #initialize an empty list to store tasks
    while True:
        # Display menu
        print("\n\nTask Manager\n\n1.Add task\n2.view task\n3.Delete task\n4.Mark task as completed\n5.Exit")

        choice=input("\nEnter your choice: ") # Take user input for menu selection

        # Call functions based on user's choice
        if choice=="1":
            title=input("Enter task title: ")
            addTask(taskList,title)
            saveTasks(taskList)
        elif choice=="2":
            viewTask(taskList)
        elif choice=="3":
            taskId=int(input("Enter task id to delete: "))
            deleteTask(taskList,taskId)
        elif choice=="4":
            taskId=int(input("Enter the task id to mark as completed:"))
            markTaskComplete(taskList,taskId)
        elif choice=="5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again...")

# Run the program by calling the main function
if __name__=="__main__":
    main()

