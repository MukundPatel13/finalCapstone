"""
This capstone project is to design program for small business which can be used to manage
tasks assigned to each member of the team
"""

# =====importing libraries===========
# Import datetime library which is used later on to find out the current date
import datetime
from datetime import date
import os

# ==================================
# define udf for registering new user , add task, view all task , view current user task,

# UDF for registering new user
def reg_user():
    """
    Registration a new user, i.e  a new user is added to the user.txt file
            - Request user  of a new username
            - Request user  of a new password
            - Request user for  password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add new username and password to the user.txt file,
            - else error message is presented that confirm password doesnt match to new password.
            - ensure the username is not duplicated while trying to register new user 
    """
    user = fetch_user_info()
    if user_name != 'admin':
        # user not permitted with admin access
        print("Not authorized with admin access, login required with admin credential\n")
    else:
        # register new user and password to user.txt file
        new_username = input("Please enter new username to be registered :\n")
        #check if user name already exist , if yes error message that username exist 
        if new_username in user:
            print("Username exist, please try a new user name !\n")
        else:
            new_password = input("Please enter new password to be registered : \n")
            while True:
                confirm_password = input("Please enter password again to confirm : \n")
                # check if new password matches the confirmed password
                if new_password == confirm_password:
                    break
                else:
                    # password and confirm password doesnt match , user asked to enter again
                    print("password and confirm password don't match ! Please enter confirm password again \n")

            # write the new user name and password to user.txt file
            with open('user.txt', 'a') as f:
                f.write(f"\n{new_username}, {new_password}")

# UDF for adding new task 
def add_task():
    """
        Allow a user to add a new task to task.txt file
            - Prompt a user for the following:
                    - A username of the person whom the task is assigned to,
                    - A title of a task,
                    - A description of the task and
                    - the due date of the task.
                - Get the current date.
                - Add the data to the file task.txt and
                - Completion status of task is defaulted to 'No'
    """
    #call to function to obtain existing user data 
    user = fetch_user_info()
    
    while True:
        add_username = input("Please enter username of the person the task is assigned to :\n ")
        if add_username in user:
            break
        else:
            print("User doesn't exist to define the task ,Please try with correct user name\n")
            
    #Ask details to user for adding the task 
    add_tile = input("Please enter the title of the task:\n ")
    add_description = input("Please enter description of the task:\n ")
    current_date = date.today()
    current_date = current_date.strftime("%d %b %Y")
    add_due_date = input("Please enter the due date in format; dd mmm yyyy:\n ")
    add_completed = 'No'
    
    # Write the data of new task to tasks.txt file
    with open('tasks.txt', 'a') as f:
        f.write(f"\n{add_username}, {add_tile}, {add_description}, {current_date}, {add_due_date}, {add_completed}")

# UDF for viewing all task 
def view_all():

    """
       The program will read the task from task.txt file and displays all tasks to console in the
       format of Output 2 in the task PDF(i.e. include spacing and labelling)
               - Read a line from the file.
               - Split that line where there is comma and space.
               - Then print the results in the format shown in the Output 2
    """
    # call to function to obtain details of task
    tasks = fetch_task_info()
    
    for i in range(0, len(tasks)):
        # Print task in a user friendly manner
        print("-" * 50)
        print(f"Task            :\t{tasks[i][1]}")
        print(f"Assigned to     :\t{tasks[i][0]}")
        print(f"Date assigned   :\t{tasks[i][3]}")
        print(f"Due date        :\t{tasks[i][4]}")
        print(f"Task complete?  :\t{tasks[i][5]}")
        print(f"Task description:\n{tasks[i][2]}")
    print("-" * 50)


# UDF for viewing task to logged in user , mark task as complete or edit the task 
def view_mine():
    """
        Read the task from task.txt file and display to the console task assigned to the logged in
        user in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
                - Read a line from the file
                - Split the line where there is comma and space.
                - Check if the username of the person logged in is the same as the username you have
                  read from the file.
                - If they are the same print it in the format of Output 2 in the task PDF
                - Each task is displayed with corresponding task reference number 
                - User allowed to choose specific task by entering the task reference number 
                - if user selects a valid task reference number then the option is provided to either
                  "mark the task as complete" or "edit the task".
                - Else the error message is shown : Invalid option and returns to main menu 
                - When user choose to mark the task as complete then that particular task is marked
                  as complete and saved in the file
                - When user choose to edit the task, then they can choose to either edit the username 
                  to whom the task is assigned or edit the due date of the task 
                - Ensure that the task can only be amended if its not marked as complete 
    """
    
    write_string = ''
    tasks = fetch_task_info()
    user_task_list = []
    
    for i in range(0, len(tasks)):
        # If user_name and user in the list match then  print each task with task reference number
        if user_name == tasks[i][0]:
            user_task_list.append(tasks[i][6])
            print("-" * 50)
            print(f"Task reference  :\t{tasks[i][6]}")
            print(f"Task            :\t{tasks[i][1]}")
            print(f"Assigned to     :\t{tasks[i][0]}")
            print(f"Date assigned   :\t{tasks[i][3]}")
            print(f"Due date        :\t{tasks[i][4]}")
            print(f"Task complete?  :\t{tasks[i][5]}")
            print(f"Task description:\n{tasks[i][2]}")

    print("-" * 50)

    while True:
        try:
            task_no = int(input("Please choose the task no to mark task as complete or edit the task or '-1' to return to menu:\n"))
        except ValueError:
            print( "Invalid option")
            return
        for i in range(0, len(tasks)):
            #username and task reference number check, when match then give option to users 
            # to either mark task as complete or edit the task 
            if user_name == tasks[i][0] and task_no == tasks[i][6] and tasks[i][5].lower() == "no":
                mc_edit = input("""Please choose from below option :
'mc': to mark task as complete
'et': to edit task
:""").lower()
                if mc_edit == 'mc':
                    #mark task as complete 
                    tasks[i][5] = "Yes"
                    print(f"task no : {task_no} set to complete for user :{user_name}")
                    
                #Under edit the task, give option to user to either edit the username or due date
                elif mc_edit == 'et':
                    while True:
                        user_duedt = input("""Please choose from below option :
'u' : to edit username for  task assignment 
'dd': to edit due date
: """).lower()
                        if user_duedt == 'u':
                            #ask new username for the task reassignment 
                            new_user = input("Please enter the new  username to which this task should be assigned:\n ")
                            #check if new username is valid or not 
                            if new_user in user_dict:
                                tasks[i][0] = new_user
                                print(f"user name changed to :{tasks[i][0]} for task number:{task_no}")
                                break
                            else:
                                print("username doesnt exist, thus the task cant be assigned \n")
                                return
                        elif user_duedt == 'dd':
                            #ask user for new due date 
                            new_due_dt = input("Please enter new due date  in dd mmm yyyy format:\n ")
                            tasks[i][4] = new_due_dt
                            print(f"due date changed to {tasks[i][4]} for task number {task_no}")
                            break
                elif mc_edit != 'mc' or mc_edit != 'et':
                    #error message , invalid option 
                    print("Invalid option")
                    return
            elif user_name == tasks[i][0] and task_no == tasks[i][6] and tasks[i][5].lower() == "yes":
                # error message that task has already been marked as complete
                print(F" task {task_no} reference for user name : {user_name} has already been marked as complete ")
                return
            elif task_no == -1:
                return
            elif task_no not in user_task_list:
                # error message , invalid task reference number 
                print("Invalid task number selected from the options above \n")
                return
            tasks[i].pop(6)
            write_string += ", ".join(tasks[i]) + "\n"
        
        #write the data back to tasks.txt file 
        with open("tasks.txt", "w") as f:
            f.write(write_string)
        return


#UDF to generate report 
def gen_reports():
    """
    Generate two reports task_overview and user_overview 
    Content of task_overview report : 
        - Total number of tasks 
        - Total number of completed tasks
        - Total number of incomplete tasks
        - Total number of overdue tasks which are incomplete 
        - Percentange of imcoplete tasks 
        - Percentage of overdue tasks 
        
    content of user_overview report: 
        - Total number of users 
        - Total number of Tasks 
        For each user : 
        - Total number of task 
        - Percentage of total number of tasks 
        - Percentage of completed tasks 
        - Percentage of incomplete tasks 
        - Percentage of overdue tasks 
    """
    
    tasks = fetch_task_info()
    total_task = len(tasks)
    not_completed = 0
    completed = 0
    over_due = 0
    not_comp_percent = 0
    over_due_percent = 0
    # Find out all the statistics for generating the report 
    for i in range(0, total_task):
        if tasks[i][5].lower() == "no" and datetime.datetime.strptime(tasks[i][4],
                                                                      '%d %b %Y') > datetime.datetime.today():
            not_completed += 1
            not_comp_percent = (not_completed / total_task) * 100
        elif tasks[i][5].lower() == "no" and datetime.datetime.strptime(tasks[i][4],
                                                                        '%d %b %Y') < datetime.datetime.today():
            not_completed += 1
            over_due += 1
            not_comp_percent = (not_completed / total_task) * 100
            over_due_percent = (over_due / total_task) * 100
        elif tasks[i][5].lower() == "yes":
            completed += 1
    
    #write task_overview.txt report 
    with open("task_overview.txt", "w") as f:
        f.write(f"Total number of tasks           \t- {total_task}\n")
        f.write(f"Total number of tasks completed \t- {completed}\n")
        f.write(f"Total number of tasks incomplete\t- {not_completed}\n")
        f.write(f"Total number of tasks overdue   \t- {over_due}\n")
        f.write(f"Percentage of tasks incomplete  \t- {not_comp_percent:.2f}%\n")
        f.write(f"Percentage of tasks overdue     \t- {over_due_percent:.2f}%\n")

    users = fetch_user_info()
    user_list = [k for k in users.keys()]
    total_user = len(user_list)
    
    with open("user_overview.txt", "w") as fu:
        fu.write(f"Total number of users\t\t\t- {total_user}\n")
        fu.write(f"Total number of tasks\t\t\t- {total_task}\n")
        for i in range(0, total_user):
            user_tasks = 0
            user_completed = 0
            user_not_completed = 0
            user_overdue = 0
            total_task_percent = 0
            user_complete_percent = 0
            user_incomplete_percent = 0
            user_overdue_percent = 0

            for j in range(0, total_task):
                if user_list[i] == tasks[j][0] and tasks[j][5].lower() == "yes":
                    user_tasks += 1
                    user_completed += 1
                elif user_list[i] == tasks[j][0] and tasks[j][5].lower() == "no" and datetime.datetime.strptime(
                        tasks[j][4], '%d %b %Y') > datetime.datetime.today():
                    user_tasks += 1
                    user_not_completed += 1
                elif user_list[i] == tasks[j][0] and tasks[j][5].lower() == "no" and datetime.datetime.strptime(
                        tasks[j][4], '%d %b %Y') < datetime.datetime.today():
                    user_tasks += 1
                    user_not_completed += 1
                    user_overdue += 1
                total_task_percent = (user_tasks / total_task) * 100
                if user_tasks != 0:
                    user_complete_percent = (user_completed / user_tasks) * 100
                    user_incomplete_percent = (user_not_completed / user_tasks) * 100
                    user_overdue_percent = (user_overdue / user_tasks) * 100

            # Write to user_overview report for each user 
            fu.write("-" * 50 + "\n")
            fu.write(f"User: {user_list[i]}\n\n")
            fu.write(f"Total number of task         \t- {user_tasks}\n")
            fu.write(f"Percentage of total tasks    \t- {total_task_percent:.2f}%\n")
            fu.write(f"Percentage of task completed \t- {user_complete_percent:.2f}%\n")
            fu.write(f"Percentage of task incomplete\t- {user_incomplete_percent:.2f}%\n")
            fu.write(f"Percentage of task overdue   \t- {user_overdue_percent:.2f}%\n")


#UDF to display statistics from the task_overview and user_overview report , if it doesnt exist 
# geenrate the report first and then display the statistics 

def disp_stats():
    
    #genetate the reports first if they dont exist 
    if (os.path.exists('./task_overview.txt') == False) or (os.path.exists('./user_overview.txt') == False):
        gen_reports()

    # Print the statistics from the report files 
    print("-" * 50)
    with open('task_overview.txt', 'r') as f:
        for line in f:
            print(line, end='')
    print("-" * 50)
    with open('user_overview.txt', 'r') as fu:
        for line in fu:
            print(line, end='')
    print("-" * 50)

#UDF to obtain user information 
def fetch_user_info():
    user_dict = {}
    # read the user.txt file and extract the username and password
    with open('user.txt', 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(", ")
            user_dict.update({line[0]: line[1]})
    return user_dict


#UDF to obtains task information 
def fetch_task_info():
    count = 1
    tasks = []
    with open('tasks.txt', 'r') as f:
        for line in f:
            line = line.strip("\n")
            tasks.extend([line.split(", ") + [count]])
            count += 1
    return tasks


# ====Login Section====
'''
below code which will allow the user to login 
    - read usernames and password from the user.txt file and store it in dictionary called user_dict
    - while loop to validate your user name and password.
'''


user_dict = fetch_user_info()
while True:
    # Ask username and password from the user
    user_name = input("Please enter username : ")

    """
    check if username entered by user is found in the data of users obtained from the user.txt file , 
    if its valid then progress further, else give error message that user name not found 
    and continue until the user has entered the correct user name
    """

    if user_name in user_dict:
        # ask user to enter the password for the user name which is valid
        password = input("Please enter password : ")
        # check if the password entered by user matches the password obtained from user.txt file
        if password == user_dict[user_name]:
            # password matched for the username
            print("Username and password match ")
            break
        else:
            # print error message ,if password not matched
            print("username found but password doesnt match, please try again ")

    else:
        # print username not found
        print("Entered username not found , please try again")

"""
presenting the menu to the user, once the login is successful and making sure that the user input is 
converted to lower case.
Admin user gets the option to generate report and display statistics as well as compared to other users
"""

while True:
    if user_name == 'admin':
        menu = input('''Select one of the following Options below:
r  - Registering a user
a  - Adding a task
va - View all tasks
vm - view my task
gr - generate reports 
ds - display statistics 
e  - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r  - Registering a user
a  - Adding a task
va - View all tasks
vm - view my task
e  - Exit
: ''').lower()

    if menu == 'r':
        # Call to reg_user function for registering a new user
        reg_user()
    elif menu == 'a':
        # call to add_task function for adding a new task
        add_task()
    elif menu == 'va':
        # call to view_all function to view all the task
        view_all()
    elif menu == 'vm':
        # call to view_mine function to view task associated to current logged in user
        view_mine()
    elif menu == 'gr':
        gen_reports()
    elif menu == 'ds':
        disp_stats()
    elif menu == 'e':
        # Option to exit the program
        print('Goodbye!!!')
        break

    else:
        # Message to user that valid option has not been chosen
        print("You have made a wrong choice, Please Try again")
