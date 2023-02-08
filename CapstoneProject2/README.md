#Capstone Project II 
This capstone project is to design program for small business which can be used to manage 
tasks assigned to each member of the team

## Log In Section
- Asks user to input their username and checks it against the data in the user.txt file.
- Asks user to input their password and checks it against the corresponding value for their username
- If the user enters either wrong, allows them to try again until they get it correct

## Menu Selection
If the user is admin, allows them to access the following menu with additional features:
- r -  Register a new user
- a -  Add a task
- va - View all tasks
- vm - View my tasks
- e -  Exit


## Features
### Register a New User*
Registration a new user, i.e  a new user is added to the user.txt file
            - Request user  of a new username
            - Request user  of a new password
            - Request user for  password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add new username and password to the user.txt file,
            - else eror message is presented that confirm password doesnt match to new password
If the user is admin , then the user is allowed to register and display statistics of total number of users and task 
else the user is not authorized to register a new user 

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

