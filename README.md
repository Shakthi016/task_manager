# Task Manager CLI Application

## Description

This project implements a simple command-line tool for managing tasks. Users can leverage features like adding, viewing, marking tasks as complete, and deleting them. Additionally, the application provides the ability to save and load tasks from a JSON file for persistence.

## Features

* **User Login:** Requires a pre-defined email and password for security (for testing purposes only).
* **Task Management:**
    * **Add Task:** Create a new task by entering its title.
    * **View Tasks:** Display all tasks, indicating their completion status (complete or pending).
    * **Delete Task:** Remove a specific task by providing its ID.
    * **Mark Task as Complete:** Update a task's status to complete using its ID.
* **Data Persistence:** Saves tasks to a JSON file (`tasks.json`) for future use.

## How to Run

1. **Obtain the Project:** Clone or download this project to your local machine.
2. **Python Requirement:** Ensure you have Python 3.x installed on your system.
3. **Run the Application:** Open a terminal, navigate to the project directory, and execute:

```bash
python task_manager.py
```

**Login Credentials (Testing Only):**

* Email: tester@gmail.com
* Password: tester@123

## Usage

**Main Menu Options:**

1. **Add Task:** Create a new task by entering its title.
2. **View Tasks:** Display a list of all tasks with their ID, title, and completion status.
3. **Delete Task:** Remove a task by providing its specific ID.
4. **Mark Task as Complete:** Update a task's status to complete using its ID.
5. **Exit:** Terminate the application. Currently saved tasks will persist.

**Example Commands:**

* **Adding a Task:** Select option 1 and enter a title for your new task.
* **Viewing Tasks:** Choose option 2 to view all your existing tasks.
* **Deleting a Task:** Select option 3, then enter the ID of the task you want to remove.
* **Marking a Task as Complete:** Choose option 4, followed by entering the ID of the task you want to mark as completed.
* **Exiting:** Select option 5 to exit the application. Your tasks will be automatically saved.

## File Structure

* `task_manager.py`: The main application file containing all the program logic.
* `tasks.json`: The JSON file used to store task data in a structured format, allowing persistence across sessions.

## Additional Notes

The application incorporates basic error handling mechanisms for file operations and handling invalid task IDs.
```
