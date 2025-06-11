# ===== Importing external modules ===========
from datetime import date
from datetime import datetime


class User:


    def __init__(self, username, password):
        '''
        initialises the following attributes:
            ● username,
            ● password,
        '''
        self.username = username
        self.password = password


    def __str__(self):
        return f"Username: {self.username}\n\
Password: {self.password}"


class Task:


    def __init__(self, username, task_name,
    task_description, task_assigned, task_due, task_status):
        '''
        initialises the following attributes:
            ● username,
            ● password,
        '''
        self.username = username
        self.task_name = task_name
        self.task_description = task_description
        self.task_assigned = task_assigned
        self.task_due = task_due
        self.task_status = task_status


    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"\
____________________________________________\n\
\nTask:                         {self.task_name}\
\nAssigned to:                  {self.username}\
\nDate assigned:                {self.task_assigned}\
\nDue date:                     {self.task_due}\
\nTask completed?               {self.task_status}\
\nTask description:\
\n {self.task_description}\n"


user_info = {}
task_info = []
completed_tasks = []


def read_user_info():
    ''' Adds all the users in the user.txt file to a dictionary for use. '''
    try:
        with open("user.txt", "r", encoding="utf-8") as f:
            for lines in f:
                username = lines.strip().split(", ")[0]
                password = lines.strip().split(", ")[1]
                user_info[username] = User(username, password)
        return user_info
    except FileNotFoundError:
        print("The files doesn't exist. Check again.")


def reg_user(username, password, user_list):
    ''' Adds a new user to the dictionary and adds it to the user.txt file. '''
    try:
        with open("user.txt", "a+", encoding="utf-8") as f:
            f.write(f"\n{username}, {password}")
            user_info[username] = User(username, password)
    except FileNotFoundError:
        print("The files doesn't exist. Check again.")
    user_info.clear()
    return read_user_info() 


def read_task_info():
    ''' Reads the tasks.txt file and saves it in a list for use. '''
    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            for lines in f:
                task_info.append(Task(
                    username = lines.split(", ")[0],
                    task_name = lines.split(", ")[1],
                    task_description = lines.split(", ")[2],
                    task_assigned = lines.split(", ")[3],
                    task_due = lines.split(", ")[4],
                    task_status = lines.strip().split(", ")[5],
                    ))

            return task_info

    except FileNotFoundError:
        print("The files doesn't exist. Check again.")


def add_task(username, task_name, task_description, task_assigned, 
    task_due, task_status):
    '''Adds new task to list and adds it to the tasks.txt file'''
    try:
        with open("tasks.txt", "a+", encoding="utf-8") as f:
            f.write(f"\n{username}, {task_name},\
 {task_description}, {task_assigned}, {task_due}, {task_status}")
            task_info.append(Task(username, task_name, task_description, 
                task_assigned, task_due, task_status))
    except FileNotFoundError:
        print("The files doesn't exist. Check again.")

    task_info.clear()
    return read_task_info()

read_user_info()
for user in user_info:
    print(user)

read_task_info()


def view_all(task_list):
    for task in task_info:
        print(task)


def update_task_list(task_list):
    # writes the newest information to the tasks.txt file
    try:
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for task in task_list:
                f.write(f"{task.username}, \
{task.task_name}, {task.task_description}, {task.task_assigned}, \
{task.task_due}, {task.task_status}\n")
    except FileNotFoundError:
        print("The file doesn't exist. Please try again.")


def view_mine(user_name, task_list):
    # adds the user's task to a list
    def get_valid_task_number(choice, user_tasks):
        # Recursively search for the first correct index out of bounds is given
        # Returns to menu if non-integer or negative index given
        if choice >= len(user_tasks):
            return get_valid_task_number(choice - 1, user_tasks)

        elif choice < -1:
            print("There are no negative indexes")
            return -1

        return choice

    user_tasks = []
    for task in task_list:
        if task.username == user_name:
            user_tasks.append(task)

    if user_tasks == []:
        print("\nNo current tasks assigned")
        return

# Goes through each task and gives it an index
    for index, task in enumerate(user_tasks):
        print(f"\nTask Index: {index}\n{task}")

    while True:
    # Present choices to the user.
        try:
            choice = int(input(
            '''\nSelect one of the following options:
the index number of the task 
or type '-1' to go back to main menu
: '''))

        # Exit back to the main menu
            choice = get_valid_task_number(choice, user_tasks)
            if choice == -1:
                return 
        # Check if the index is valid
        # Gives additional steps to modify task chosen.
            task = user_tasks[choice]
            print(f"\nYou have selected task index: {choice}\n{task}") 

            while True:
                mod_choice = input('''Select one of the following options:
    e - edit a task
    m - mark a task as complete
    : ''').lower()

# Allows the user to edit the user assigned/due date or both.
                if mod_choice == 'e':
                    print("\nEditing task details...")
                    while True:
                        edit_option1 = input('''
Do you want to edit the user assigned? (Yes/No)
: ''').lower()

                        if edit_option1 == 'yes':
                            new_user = input(
f"Enter the username who the task will be assigned to:\n").lower()

                            if new_user not in user_info:
                                print("Invalid username")
                            else:
                                task.username = new_user
                                break
                        elif edit_option1 == "no":
                            print("Skipping username change")
                            break
                        else:
                            print("Choose 'yes' or 'no'.")

                    while True:
                        edit_option2 = input('''
Do you want to edit the due date? (Yes/No)
: ''').lower()
                        if edit_option2 == 'yes':    
                            task.task_due = input(
f"Enter the new due date for the task:\n").title()
                            break
                        elif edit_option2 == 'no':
                            print("Skipping due date change")
                            break
                        else:
                            print("Choose 'yes' or 'no'.")

                    print("Task updated successfully!")
                    update_task_list(task_list)

                # Marks the chosen task as complete
                elif mod_choice == 'm':
                    task.task_status = 'Yes'
                    print(f"\nTask {task.task_name} marked as completed!")
                    update_task_list(task_list)

                else:
                    print("You have entered an invalid input.\
Please try again.")

                # Break out of the inner menu and continue with other tasks
                break

        except ValueError:
            print("\nNot a valid index input. Returning.")
            return


def view_completed(completed_list):
    ''' view the tasks deleted'''
    if completed_list == []:
        print("No completed tasks to display. Delete tasks first")
    for task in completed_list:
        print(task)


def delete_task(task_title, task_list):
    ''' deletes a specific task and adds it to the
    completed tasks list.'''
    for task in task_list:
        if task.task_name == task_title:
            completed_tasks.append(task)
            task_list.remove(task)
            print(f"{task}\n\
has been successfully deleted")

            update_task_list(task_list)
            task_list.clear()
            return read_task_info()


def generate_reports(task_list, user_list, completed_tasks_list):
    ''' Calls task lists and user lists. It records the crucial data and
    does a few calculations for percentages. Then writes data to task_overview.txt
    and user_overview.txt.
    '''
    incomplete_count = 0
    overdue_count = 0
    total_tasks_count = len(task_list) + len(completed_tasks)
    for task in task_list:
        if task.task_status == "No":
            incomplete_count += 1
            if datetime.strptime(task.task_due, '%d %b %Y') < datetime.today():
                overdue_count += 1

        with open("task_overview.txt", "w", encoding="utf-8") as f:
            f.write(f"{total_tasks_count}, {len(completed_tasks)}, \
{incomplete_count}, {overdue_count}, \
{int((incomplete_count/total_tasks_count)*100)}, \
{int((overdue_count/total_tasks_count)*100)}")

    total_user_count = len(user_info)
    
    user_task_stats = {}
    for user in user_info.values():
        user_task_stats[user.username] = {
        'total_tasks': 0,
        'completed': 0,
        'incomplete': 0,
        'overdue_incomplete': 0
        }
    
    for task in task_list:
        if task.username in user_task_stats:
            user_task_stats[task.username]['total_tasks'] += 1

        if task.task_status == 'Yes':
            user_task_stats[task.username]['completed'] += 1
        
        else:
            user_task_stats[task.username]['incomplete'] += 1

            if datetime.strptime(task.task_due, '%d %b %Y') < datetime.today():
                user_task_stats[task.username]['overdue_incomplete'] += 1

    with open("user_overview.txt", "w", encoding="utf-8") as f:
        f.write(f"{total_user_count}, {total_tasks_count}")

        for user in user_task_stats:
            try:
                percent_total_tasks = int((
user_task_stats[user]['total_tasks']/total_tasks_count)*100)
                percent_completed = int((
user_task_stats[user]['completed']/user_task_stats[user]['total_tasks'])*100)
                percent_incomplete = int((
user_task_stats[user]['incomplete']/user_task_stats[user]['total_tasks'])*100)
                percent_overdue_incomplete = int((
user_task_stats[user]['overdue_incomplete']/
user_task_stats[user]['total_tasks'])*100)
            except ZeroDivisionError:
                percent_total_tasks = 0
                percent_completed = 0
                percent_overdue_incomplete = 0
                percent_incomplete = 0

            f.write(f"\n{user}, {user_task_stats[user]['total_tasks']}, \
{percent_total_tasks}, {percent_completed}, \
{percent_incomplete}, {percent_overdue_incomplete}")
           

def display_statistics(task_list, user_list, completed_tasks_list):
    ''' Generates report first and then reads the 2 files task_overview.txt
    and user_overview.txt. and prints out the 2 reports.
    '''
    generate_reports(task_list, user_list, completed_tasks_list)
    try:
        with open("task_overview.txt", "r", encoding="utf-8") as f:
            for lines in f:
                print(f'''\n
                    Tasks Overview
________________________________________________________

Number of tasks:                {lines.split(", ")[0]}
Number of completed:            {lines.split(", ")[1]}
Number of uncompleted:          {lines.split(", ")[2]}
Number of overdue uncompleted:  {lines.split(", ")[3]}
precentage incomplete:          {lines.split(", ")[4]}%
precentage overdue:             {lines.split(", ")[5]}%
________________________________________________________
''')

    except FileNotFoundError:
        print("The file doesn't exist.")

    try:
        with open("user_overview.txt", "r", encoding="utf-8") as f:
            for i, lines in enumerate(f):
                if i == 0:
                    print(f'''\n
                    Users Overview

Total users registered:             {lines.split(", ")[0]}
Total tasks:                        {lines.split(", ")[1]}
________________________________________________________''')
                else:
                    print(f'''              {lines.split(",")[0]}\n
Total tasks assigned:              {lines.split(", ")[1]}
precentage of tasks assigned:      {lines.split(", ")[2]}% 
precentage of tasks completed:     {lines.split(", ")[3]}% 
precentage of tasks incomplete:    {lines.split(", ")[4]}% 
precentage of tasks overdue:       {lines.strip().split(", ")[5]}% 
________________________________________________________
''')
    except FileNotFoundError:
        print("The file doesn't exist.")


#Login Check
menu_count = 0
login_count = 0
while login_count < 3:
    user_login = input("Please enter your username:\n")
    user_password = input("Please enter your password:\n")
    user = user_info.get(user_login)
    if not user:
        print("Incorrect username, try again")
        continue
    if user.password == user_password:
        print("Successfully logged in!")
        menu_count = 1
        login_count = 3
    else: 
        print("Incorrect password.")
        login_count += 1

#Opens menu based on the logged in username
while menu_count == 1:
    if user_login == "admin":
        menu = input(
            '''\nSelect one of the following options:
r - register a users
a - add task
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete tasks
ds - display statistics
gr - generate reports
e - exit
: '''
        ).lower()

        if menu == 'r':
            # TODO: Implement the following functionality
            '''Registers a new user with a username and password.
            Checks that a username doesn't get duplicated'''
            new_username = str(input("\nEnter the new username:\n"))
            while new_username in user_info:
                print("Username already exists")
                new_username = str(input("\nEnter the new username:\n"))
            new_password = str(input("Enter the password:\n"))
            reg_user(new_username,new_password,user_info)

        elif menu == 'a':
            '''This will add a new task to be tracked. It
            will check if the username exists, prevent double
            task titles and force the date input'''
            while True:
                new_username = str(input("\nEnter the person doing the task:\n"))
                if new_username not in user_info:
                    print("Invalid username")
                else:
                    break
            while True:
                task_name = str(input("Enter the title of the task:\n"))
                if task_name in task_info:
                    print("Task title already exists")
                else:
                    break
            task_description = str(input("Describe the task\n"))
            task_assigned = date.today().strftime('%d %b %Y')
            while True:
                task_due_input = str(input
                    ("Enter the task due date (dd-mm-yyyy):\n"))
                try:
                    task_due = datetime.strptime(
                        task_due_input, '%d-%m-%Y').strftime('%d %b %Y')
                    break
                except ValueError:
                    print("Invalid date format.")
            task_status = "No"
            add_task(new_username, task_name, task_description, 
                task_assigned, task_due, task_status)

        elif menu == 'va':
            '''View all the tasks being tracked.'''

            view_all(task_info)

        elif menu == 'vm':
            '''View all the tasks the current logged in user has,
            the user can then choose a specific task to either mark as completed
            or to edit who the task is assigned to and/or the due date.'''  

            view_mine(user_login, task_info)

        elif menu == 'vc':
            ''' View completed tasks'''

            view_completed(completed_tasks)

        elif menu == 'del':
            ''' Deletes tasks'''
            task_title = str(input(
                "Please enter the task you want to delete:\n"))
            delete_task(task_title, task_info)

        elif menu == 'ds':
            '''Displays statistics about tasks
            and users'''
            display_statistics(task_info, user_info, completed_tasks)

        elif menu == 'gr':
            ''' Generates reports and writes them to txt files.'''
            generate_reports(task_info, user_info, completed_tasks)

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again")

# Non-admin menu
    else:
        menu = input(
                    '''\nSelect one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: '''
                ).lower()

        if menu == 'a':
            '''This will add a new task to be tracked. It
            will check if the username exists, prevent double
            task titles and force the date input'''
            while True:
                new_username = str(input
                    ("\nEnter the person doing the task:\n"))
                if new_username not in user_info:
                    print("Invalid username")
                else:
                    break           
            while True:
                task_name = str(input("Enter the title of the task:\n"))
                if task_name in task_info:
                    print("Task title already exists")
                else:
                    break
            task_description = str(input("Describe the task\n"))
            task_assigned = date.today().strftime('%d %b %Y')
            while True:
                task_due_input = str(input
                    ("Enter the task due date (dd-mm-yyyy):\n"))
                try:
                    task_due = datetime.strptime(
                        task_due_input, '%d-%m-%Y').strftime('%d %b %Y')
                    break
                except ValueError:
                    print("Invalid date format.")
            task_status = "No"
            add_task(new_username, task_name, task_description, task_assigned, 
                task_due, task_status)

        elif menu == 'va':
            ''' View all the tasks being tracked.'''
            view_all(task_info)

        elif menu == 'vm':
            '''View all the tasks the current logged in user has,
            the user can then choose a specific 
            task to either mark as completed or to edit who the 
            task is assigned to and/or the due date. 
            '''      
            view_mine(user_login, task_info)

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again")