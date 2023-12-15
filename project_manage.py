# import database module
from database import ConvertCsv, DataBase, Table
import csv
import random


class Admin(DataBase):
    def __init__(self, user_id, role):
        super().__init__()
        self.role = role
        self.user_id = user_id
        self.all_table = [
            "persons", "login","project_table", "advisor_pending_table",
            "member_pending_table"
        ]
        print(self.__str__())

    def check_table(self):
        """
        this function views table that the user wants to view
        :return:
        """
        # get choice from user
        _choice = int(input("Choose table do you want to view:\n"
                            "(1) persons\n"
                            "(2) login\n"
                            "(3) project\n"
                            "(4) advisor_pending_table\n"
                            "(5) member_pending_table\n"
                            "Enter action(numbers only): "))
        print()
        # if table exist
        if _choice <= 5:
            table_name = self.all_table[_choice - 1]
            # shows all the information in the table
            print(f"Here's the {table_name} table")
            for i in my_DB.search(table_name).table:
                print(f'{my_DB.search(table_name).table.index(i) + 1:<3}| {i}')
            print()
        # if table does not exist inform user
        else:
            print("That table does not exist. Please try again\n")

    def edit_table(self):
        """
        This function edits the table
        :return:
        """
        # get choice from user
        _choice = int(input("Choose table do you want to edit?:\n"
                            "(1) persons\n"
                            "(2) login\n"
                            "(3) project\n"
                            "(4) advisor_pending_table\n"
                            "(5) member_pending_table\n"
                            "Enter table (numbers only): "))
        print()
        # if table exist
        if _choice <= 5:
            table_name = self.all_table[_choice - 1]
            print(f"Here's the {table_name} table")
            # display the table chosen
            for i in my_DB.search(table_name).table:
                print(f'{my_DB.search(table_name).table.index(i) + 1:<3}| {i}')
            print()
            # display all the keys in the dict of the table
            print('These are the available keys: ')
            key_list = list(my_DB.search(table_name).table[0].keys())
            for i in key_list:
                print(f'{key_list.index(i) + 1}. {i}')
            # get info about what user wants to change
            user_index = int(input("Enter which dict to change "
                                   "(from the number listed above):")) - 1
            user_key = input("Enter key to change: ")
            new_value = input("Enter new value to change: ")
            # get id from the info given to use in the update method
            user_id = my_DB.search(table_name).table[user_index]['ID']
            # change info
            my_DB.search(table_name).table.update(user_id, user_key, new_value)
        # if table does not exist inform user
        else:
            print("That table does not exist. Please try again")

    def insert_table(self):
        """
        insert new dict into a table
        :return:
        """
        # get choice from user
        _choice = int(input("Choose table do you want to insert?:\n"
                            "(1) persons\n"
                            "(2) login\n"
                            "(3) project\n"
                            "(4) advisor_pending_table\n"
                            "(5) member_pending_table\n"
                            "Enter table (numbers only): "))
        print()
        if _choice <= 5:
            table_name = self.all_table[_choice - 1]
            print(f"Here's the {table_name} table")
            # display the table chosen
            for i in my_DB.search(table_name).table:
                print(f'{my_DB.search(table_name).table.index(i) + 1:<3}| {i}')
            print()
            # display all the keys in the dict of the table
            print('Please enter values for these keys: ')
            # create a empty dict
            new_dict = {}
            key_list = list(my_DB.search(table_name).table[0].keys())
            print(key_list)
            # prompt the user to enter the value for each keys
            for i in key_list:
                value = input(f'{i}: ')
                new_dict[i] = value
            # insert the new dict into table
            my_DB.search(table_name).table.insert(new_dict)

        # if table does not exist inform user
        else:
            print("That table does not exist. Please try again")

    def delete_dict(self):
        _choice = int(input("Choose table do you want to delete dict?:\n"
                            "(1) persons\n"
                            "(2) login\n"
                            "(3) project\n"
                            "(4) advisor_pending_table\n"
                            "(5) member_pending_table\n"
                            "Enter table (numbers only): "))
        print()
        if _choice <= 5:
            table_name = self.all_table[_choice - 1]
            print(f"Here's the {table_name} table")
            # display the table chosen
            for i in my_DB.search(table_name).table:
                print(f'{my_DB.search(table_name).table.index(i) + 1:<3}| {i}')
            print()
            user_index = int(input("Enter which dict to delete "
                                   "(from the number listed above):")) - 1
            del my_DB.search(table_name).table[user_index]
        # if table does not exist inform user
        else:
            print("That table does not exist. Please try again")

    def __str__(self):
        return (f"--------------\n"
                f"Welcome, ID: {self.user_id:<7} | Role: {self.role: <10}\n"
                f"--------------")


class Student(DataBase):
    def __init__(self, std_id):
        super().__init__()
        login_table = my_DB.search('login').table
        for i in login_table:
            if i['ID'] == std_id:
                self.username = i['username']
                self.role = i['role']
        self.ID = std_id
        self.project = False

    def create_project(self):
        self.role = 'Lead'
        self.project = True
        project_id = ''
        for i in range(6):
            project_id += str(random.randint(0,9))
        title = input('Enter your project title: ')
        new_dict = {
            "ProjectID": project_id,
            "Title": title,
            "Lead": self.username,
            "Member1": "",
            "Member2": "",
            "Advisor": "",
            "Status": "Pending"
        }
        my_DB.search('project_table').insert(new_dict)


    # def see_pending_request(self):
    #     if self.project == True and self.lead == True:
    #         my_table = my_DB.search('member_pending_table').table
    #         pass
    #     else:
    #         if self.lead == False and self.project == True:
    #             print("Sorry, you don't have to permission to view this")
    #         else:
    #             print("Sorry, you are not in any project.")


my_DB = DataBase()


# define a function called initializing
def initializing():
    # converter object
    converter = ConvertCsv()

    # convert persons.csv to table and insert in database
    converted_person = converter.csv_to_table('persons.csv')
    persons = Table('persons', converted_person)
    my_DB.insert(persons)

    # convert persons.csv to table and insert in database
    converted_login = converter.csv_to_table('login.csv')
    login = Table('login', converted_login)
    my_DB.insert(login)

    # create project_table object and insert into database
    converted_project_table = converter.csv_to_table('project_table.csv')
    project_table = Table('project_table', converted_project_table)
    my_DB.insert(project_table)

    # create advisor_pending_request object and insert into database
    converted_advisor_pending_table = converter.csv_to_table(
        'advisor_pending_table.csv'
    )
    advisor_pending_request = Table(
        'advisor_pending_table', converted_advisor_pending_table
    )
    my_DB.insert(advisor_pending_request)

    # create member_pending_request object and insert into database
    converted_member_pending_table = converter.csv_to_table(
        'member_pending_table.csv'
    )
    member_pending_request = Table(
        'member_pending_table', converted_member_pending_table
    )
    my_DB.insert(member_pending_request)

    # here are things to do in this function:
    # write out all the tables that have been modified to the corresponding csv files
    # By now, you know how to read in a csv file and transform it into a list
    # of dictionaries. For this project, you also need to know how to do the reverse,
    # i.e., writing out to a csv file given a list of dictionaries. See the link below
    # for a tutorial on how to do this:

    # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# define a function called login
def login():
    """
    check if username and password match
    :return:
    """
    username = input('Enter username: ')
    password = input('Enter password: ')
    username_ls = [x['username'] for x in my_DB.search('login').table]
    password_ls = [x['password'] for x in my_DB.search('login').table]
    # print(username_ls)
    # print(password_ls)
    if username in username_ls:
        user_index = username_ls.index(username)
        if password == password_ls[user_index]:
            return (
                list(my_DB.search('login').select(
                    ['ID', 'role'])[user_index].values()
                     )
            )
        else:
            return None
    else:
        return None


# define a function called exit
def exit_program():
    print('Table: persons')
    for i in my_DB.search('persons').table:
        print(i)
    print('-----')

    print('Table: login')
    for i in my_DB.search('login').table:
        print(i)
    print('-----')

    print('Table: project_table')
    # Add converter table to csv here
    project_table = open('project_table.csv', 'w')
    writer = csv.writer(project_table)
    writer.writerow([
        'ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor',
        'Status'
    ])
    for dictionary in my_DB.search('project_table').table:
        writer.writerow(dictionary.values())
    project_table.close()
    project_table = open('project_table.csv', 'r')
    print("The content of the csv file is:")
    print(project_table.read())
    project_table.close()
    print('-----')

    print('Table: advisor_pending_table')
    # Add converter to csv here
    advisor_pending_table = open('advisor_pending_table.csv', 'w')
    writer = csv.writer(advisor_pending_table)
    writer.writerow([
        'ProjectID', 'to_be_advisor', 'Response', 'Response_date'
    ])
    for dictionary in my_DB.search('advisor_pending_table').table:
        writer.writerow(dictionary.values())
    advisor_pending_table.close()
    advisor_pending_table = open('advisor_pending_table.csv', 'r')
    print("The content of the csv file is:")
    print(advisor_pending_table.read())
    advisor_pending_table.close()
    print('-----')

    print('Table: member_pending_table')
    # Add converter table to csv here
    member_pending_table = open('member_pending_table.csv', 'w')
    writer = csv.writer(member_pending_table)
    writer.writerow([
        'ProjectID', 'to_be_member', 'Response', 'Response_date'
    ])
    for dictionary in my_DB.search('member_pending_table').table:
        writer.writerow(dictionary.values())
    member_pending_table.close()
    member_pending_table = open('member_pending_table.csv', 'r')
    print("The content of the csv file is:")
    print(member_pending_table.read())
    member_pending_table.close()
    print('-----')


# make calls to the initializing and login functions defined above

initializing()
val = login()
while val is None:
    print("username or password is incorrect")
    val = login()

# based on the return value for login, activate the code that performs
# activities according to the role defined for that person_id

if val[1] == 'admin':
    in_program = True
    while in_program:
        admin = Admin(val[0], val[1])
        choice = int(input("What would you like to do?\n"
                           "(1) View table\n"
                           "(2) Edit table\n"
                           "(3) Add dict to table\n"
                           "(4) Delete dict from table\n"
                           "(0) Exit\n"
                           "Enter choice (numbers only): "))
        # view table
        if choice == 1:
            admin.check_table()
        # edit table
        elif choice == 2:
            admin.edit_table()
        # insert dict in table
        elif choice == 3:
            admin.insert_table()
        # delete dict in table
        elif choice == 4:
            admin.delete_dict()
        # exit program
        elif choice == 0:
            in_program = False
        # inform user that the action does not exist
        else:
            print('That action does not exist. Please try again')
elif val[1] == 'student':
    in_program = True
    while in_program:
        student = Student(val[0])
        choice = int(input("What would you like to do?:\n"
                           "(1) Create project\n"
                           "(0) Exit\n"
                           "Enter choice (numbers only): "))
        # create project
        if choice == 1:
            student.create_project()
        elif choice == 0:
            in_program = False
        else:
            print('That action does not exist. Please try again')
elif val[1] == 'member':
    pass
elif val[1] == 'lead':
    pass
elif val[1] == 'faculty':
    pass
elif val[1] == 'advisor':
    pass

# once everything is done, make a call to the exit function
exit_program()
