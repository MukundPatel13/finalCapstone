# Capstone Project III - Manage task Alloction ( using Function , List ) 
This capstone project is to design program for small business which can be used to manage
tasks assigned to each member of the team

## Content
- [task manager](https://github.com/MukundPatel13/finalCapstone/blob/master/CapstoneProject3/task_manager.py)
- [Task file](https://github.com/MukundPatel13/finalCapstone/blob/master/CapstoneProject3/tasks.txt)
- [User file](https://github.com/MukundPatel13/finalCapstone/blob/master/CapstoneProject3/user.txt)
- [ReadMe](https://github.com/MukundPatel13/finalCapstone/blob/master/CapstoneProject3/README.md)

## Installation
- Install [Python 3](https://www.python.org/downloads/)
- Install [Pycharm ](https://www.jetbrains.com/help/pycharm/installation-guide.html)
- Clone the project in pycharm [Clone Project ](https://github.com/MukundPatel13/finalCapstone.git)
--------------------------------------------------------------------------------------------------------------------------------------
**************************************************************************************************************************************
--------------------------------------------------------------------------------------------------------------------------------------
## Usage based on below description : 

## Log In Section
- Asks user to input their username and checks it against the data in the user.txt file.
- Asks user to input their password and checks it against the corresponding value for their username
- If the user enters either wrong, allows them to try again until they get it correct

## Menu Selection
### Admin
If the user is admin, allows them to access the following menu with additional features:
- r  -  Register a new user
- a  -  Add a task
- va - View all tasks
- vm - View my tasks
- gr - Generate reports
- ds - Display statistics
- e -  Exit

### Regular User
If the user is not admin, displays a restricted menu:
- a  -  Add a task
- va - View all tasks
- vm - View my tasks
- e  -  Exit

## Features
### Register a New User*
Allows the user to add a user to the user.txt file
- User is prompted to enter a new username
- If the username is already in use, allows them to try again until they enter a username that is not used
- Prompts user to enter a password
- Prompts user to confirm password
- Writes new user details to user.txt

### Add a Task
Allows the user to add details of a task to the tasks.txt file.
  - Prompts user for task data
  - Who the task is assigned to
  - If the user is not in user.txt, gives an error message and allows them to try again
  - The title of the task
  - A description of the task
  - The due-date, written as: DD Mon YYYY (e.g 19 Sep 2022)
  - Gets today's date
  - Marks task automatically as incomplete
  - Writes task info to tasks.txt

### View All Tasks
Allows user to view tasks for every user in an easy to read format.

### View My Tasks
Allows user to view their own tasks in an easy to read format and give them the option to edit them.
- If user chooses to edit a task, allows them to choose to either mark as complete, change the due date or change who the task is assigned to

### Generate Reports*
Allows user to generate two new text files 'task_overview.txt' and 'user_overview.txt' which contain the following information:
#### Task Overview
- The total number of tasks that have been generated and tracked using the task_manager.py.
- The total number of completed tasks.
- The total number of uncompleted tasks.
- The total number of tasks that haven???t been completed and
that are overdue.
- The percentage of tasks that are incomplete.
- The percentage of tasks that are overdue.
#### User Overview
- The total number of users registered with task_manager.py.
- The total number of tasks that have been generated and
tracked using the task_manager.py.
- For each user also describes:
  - The total number of tasks assigned to that user.
  - What percentage of the total number of tasks have
  been assigned to that user?
  - What percentage of the tasks assigned to that user
  have been completed?
  - What percentage of the tasks assigned to that user
  must still be completed?
  - What percentage of the tasks assigned to that user
  have not yet been completed and are overdue?

### Display Statistics*
Views information from user_overview.txt and task_overview.txt in an easy to read format.

\* User must be admin to use these features
