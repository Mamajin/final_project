# import database module
from database import ConvertCsv, DataBase, Table
import csv
import random


class Admin:
    def __init__(self, user_id, role):
        login_table = my_DB.search('login').table
        for i in login_table:
            if i['ID'] == user_id:
                self.username = i['username']
        self.role = role
        self.user_id = user_id
        self.all_table = [
            "persons", "login", "project_table", "advisor_pending_table",
            "member_pending_table"
        ]
        print(self.__str__())

    def __str__(self):
        return (f"----------------------------------------------\n"
                f"Welcome, {self.username} ID: {self.user_id:<7} "
                f"| Role: {self.role: <10}\n"
                f"----------------------------------------------")

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
            # get info about what user wants to change
            user_index = int(input("Enter which dict to change "
                                   "(from the number listed above): ")) - 1
            # display all the keys in the dict of the table
            print('These are the available keys: ')
            key_list = list(my_DB.search(table_name).table[0].keys())
            for i in key_list:
                print(f'{key_list.index(i) + 1}. {i}')
            user_key = input("Enter key to change (key name): ")
            new_value = input("Enter new value to change: ")
            # get id from the info given to use in the update method
            if 0 == _choice - 1 <= 1:
                search_key = 'ID'
            else:
                search_key = 'ProjectID'
            user_id = my_DB.search(table_name).table[user_index][search_key]
            # change info
            my_DB.search(table_name).update(
                user_id, search_key, user_key, new_value)
        # if table does not exist inform user
        else:
            print("That table does not exist. Please try again")

    def insert_dict(self):
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
            my_DB.search(table_name).insert(new_dict)

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
                                   "(from the number listed above): ")) - 1
            del my_DB.search(table_name).table[user_index]
        # if table does not exist inform user
        else:
            print("That table does not exist. Please try again")


class Student:
    def __init__(self, std_id):
        login_table = my_DB.search('login').table
        for i in login_table:
            if i['ID'] == std_id:
                self.username = i['username']
                self.role = i['role']
        self.user_id = std_id
        print(self.__str__())

    def __str__(self):
        return (f"----------------------------------------------\n"
                f"Welcome, {self.username} ID: {self.user_id:<7} "
                f"| Role: {self.role: <10}\n"
                f"----------------------------------------------")

    def create_project(self):
        """
        In order create project must deny all member request first
        :return:
        """
        # updates the role of that student to lead
        my_DB.search('login').update(self.user_id, 'ID', 'role', 'lead')
        project_id = ''
        # generate projectID
        for i in range(6):
            project_id += str(random.randint(0, 9))
        # get title for the project
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
        # insert the new dict to table in the database
        my_DB.search('project_table').insert(new_dict)
        # show the info about the newly created group
        print(f"Group created, Here's the group info")
        for key, value in new_dict.items():
            print(f'{key}: {value}')
        # login again to see the refreshed database
        print('Please exit and login again to refresh the database.\n')

    def see_pending_request(self):
        """
        From the member_pending_table check if the user have pending
        request(s) or not
        :return:
        """
        # create a list of member pending
        pending_table = my_DB.search('member_pending_table').filter(
            lambda x: x['to_be_member'] == self.username
        ).table
        # if there are pending members display them
        if pending_table:
            print('These are the groups that invited you.')
            for i in pending_table:
                print(f'{pending_table.index(i) + 1}| '
                      f'ProjectID: {i["ProjectID"]} wants you to join them.')
        # if there's no invitations yet
        else:
            print("You don't have any invitation yet.\n")
        print()

    def accept_or_deny_request(self):
        """
        Choose to accept or deny requests From the pending
        :return:
        """
        # display the pending members
        pending_table = my_DB.search('member_pending_table').filter(
            lambda x: x['to_be_member'] == self.username
        ).table
        # if you are invited show that which group(s) invited them
        if pending_table:
            print('These are the groups that invited you.')
            # print all the groups that invited
            for i in pending_table:
                print(f'{pending_table.index(i) + 1:<3}| '
                      f'ProjectID: {i["ProjectID"]} wants you to join them.')
            _choice = int(
                input('Which group to you want to update your status?: ')
            ) - 1
            if _choice < len(pending_table):
                join_choice = input(f'Would you like to join '
                                    f'{pending_table[_choice]["ProjectID"]}? '
                                    f'type(Y/N): '
                                    ).lower()
                project_id_selected = pending_table[_choice]['ProjectID']
                # if the user excepts the request
                if join_choice == 'y':
                    mem1 = my_DB.search(
                        'project_table').table[_choice - 1]["Member1"]
                    mem2 = my_DB.search(
                        'project_table').table[_choice - 1]["Member2"]
                    if mem1 == "" or mem2 == "":
                        print('You have accepted their request. '
                              'You have now joined the group')
                        # update the member_pending_table
                        my_DB.search('member_pending_table').update(
                            project_id_selected, 'ProjectID', 'Response',
                            'Accepted'
                        )
                        my_DB.search('member_pending_table').update(
                            project_id_selected, 'ProjectID', 'Response_date',
                            '16/12/23'
                        )
                        my_DB.search('login').update(self.username, 'username',
                                                     'role', 'member')
                        # put the user's name in the slot available
                        if my_DB.search(
                                'project_table'
                        ).table[_choice - 1]["Member1"] == "":
                            my_DB.search(
                                'project_table'
                            ).table[_choice - 1]["Member1"] = self.username
                        # if slot 2
                        elif my_DB.search(
                                'project_table'
                        ).table[_choice - 1]["Member2"] == "":
                            my_DB.search(
                                'project_table'
                            ).table[_choice - 1]["Member2"] = self.username
                    # if group is full
                    else:
                        print("Sorry this group is full.")
                # if the user denies the request
                else:
                    print('You have denied their request.\n')
                    # update the member_pending_table
                    my_DB.search('member_pending_table').update(
                        self.user_id, 'ProjectID', 'Response', 'Denied'
                    )
                    my_DB.search('member_pending_table').update(
                        self.user_id, 'ProjectID', 'Response_date', '16/12/23'
                    )

        else:
            print("You don't have any invitation yet.\n")

    def send_request(self):
        """
        Send out requests and update the member_pending_request table
        request can only go to those whose role is student i.e. not yet
        become a member or lead
        :return:
        """
        print('These are the groups you can join')
        project_table = my_DB.search('project_table').table.filter(
            lambda x: x['Member2'] == "")
        # display the group that you can join
        for i in project_table:
            print(f'{project_table.index(i) + 1:<3}| {i}')
        _choice = int(input('Which group do you want to join? (in number): '))
        if _choice - 1 < len(project_table):
            # create new_dict to be inserted in member_pending_table
            new_dict = {
                'ProjectID': project_table[_choice - 1]['ProjectID'],
                'to_be_member': self.username,
                'Response': 'Pending',
                'Response_date': "16/12/2023"
            }
            my_DB.search('member_pending_table').insert(new_dict)
        # if the group does not exist
        else:
            print('Sorry, group does not exist.')


class Lead:
    def __init__(self, std_id):
        login_table = my_DB.search('login').table
        for i in login_table:
            if i['ID'] == std_id:
                self.username = i['username']
                self.role = i['role']
        self.user_id = std_id
        project_id = my_DB.search('project_table').filter(
            lambda x: x['Lead'] == self.username).table[0]['ProjectID']
        self.project_id = project_id
        print(self.__str__())

    def __str__(self):
        return (f"----------------------------------------------\n"
                f"Welcome, {self.username} ID: {self.user_id:<7} "
                f"| Role: {self.role: <10}\n"
                f"----------------------------------------------")

    def see_project_status(self):
        """
        pending member, pending advisor or ready to solicit an advisor
        """
        print("Here's your project status")
        # member pending
        print("Member Pending:")
        pending_member = my_DB.search('member_pending_table').filter(
            lambda x: x['ProjectID'] == self.project_id).table
        for i in pending_member:
            print(f'{pending_member.index(i) + 1:<3}| {i}')
        # advisor pending
        print("Advisor Pending:")
        pending_advisor = my_DB.search('advisor_pending_table').filter(
            lambda x: x['ProjectID'] == self.project_id).table
        for i in pending_advisor:
            print(f'{pending_advisor.index(i) + 1:<3}| {i}')
        print("Is group ready to solicit an advisor?:")
        pending_member = my_DB.search('member_pending_table').filter(
            lambda x: x['ProjectID'] == self.project_id).filter(
            lambda x: x['Response'] == 'Pending'
        ).table
        if not pending_member:
            print('Your project is ready to solicit an advisor.')
        else:
            print('Your project is not ready to solicit an advisor.\n'
                  'Please clear your member pending.')
        print()

    def see_project_info(self):
        print("Here's your project")
        project = my_DB.search('project_table').filter(
            lambda x: x['ProjectID'] == self.project_id).table[0]
        for key, value in project.items():
            print(f'{key}: {value}')
        print()

    def modify_project_info(self):
        self.see_project_info()
        new_title = input('Enter new Title: ')
        my_DB.search('project_table').filter(
            lambda x: x['ProjectID'] == self.project_id
        ).table[0] = new_title
        print(f'Project Title changed to {new_title}')
        print()

    def see_request_response(self):
        """
        See who has responded to the requests sent out
        :return:
        """
        response = my_DB.search('member_pending_table').filter(
            lambda x: x['ProjectID'] == self.project_id).table
        if response:
            print("Here are the the request response")
            for i in response:
                print(f"Name: {i['to_be_member']}\n"
                      f"Response: {i['Response']}\n"
                      f"Response Date: {i['Response_date']}\n")
        else:
            print('You have no response yet.')
        print()

    def send_member_request(self):
        """
        The one who gets the request must be a student
        Member_pending_request table needs to be updated
        """
        # create table for the students
        student_table = my_DB.search('login').filter(
            lambda x: x['role'] == 'student'
        ).table
        print('These are the students you can send request to')
        # display the students you can send the request to
        for i in student_table:
            print(f'{student_table.index(i) + 1:<3}| {i["username"]} '
                  f'ID: {i["ID"]}')
        _choice = int(input('Which student do you want to join your group? '
                            '(in number): '))
        if _choice - 1 < len(student_table):
            # create new_dict to be inserted in advisor_pending_table
            _student = student_table[_choice - 1]['username']
            new_dict = {
                'ProjectID': self.project_id,
                'to_be_member': _student,
                'Response': 'Pending',
                'Response_date': "16/12/2023"
            }
            # insert request to table
            my_DB.search('member_pending_table').insert(new_dict)
            print(f"Successfully requested {_student} to join your group.")
        print()

    def send_advisor_request(self):
        """
        send request to potential advisor; can only do one at a time
        after all potential have accepted or denied the requests
        Advisor_pending_request table needs to be updated
        :return:
        """
        faculty_table = my_DB.search('login').filter(
            lambda x: x['role'] == 'faculty'
        ).table
        print('These are the faculty staff you can send request to')
        for i in faculty_table:
            print(f'{faculty_table.index(i) + 1:<3}| {i["username"]} '
                  f'ID: {i["ID"]}')
        _choice = int(input('Which staff do you want to join your group? '
                            '(in number): '))
        print('Request sent awaiting for confirmation')
        if _choice - 1 < len(faculty_table):
            # create new_dict to be inserted in advisor_pending_table
            _advisor = faculty_table[_choice - 1]['username']
            new_dict = {
                'ProjectID': self.project_id,
                'to_be_advisor': _advisor,
                'Response': 'Pending',
                'Response_date': "16/12/2023"
            }
            # insert request into dict
            my_DB.search('advisor_pending_table').insert(new_dict)
        print()


class Member(Lead):
    def __init__(self, std_id):
        super().__init__(std_id)


class Faculty:
    def __init__(self, user_id):
        login_table = my_DB.search('login').table
        for i in login_table:
            if i['ID'] == user_id:
                self.username = i['username']
                self.role = i['role']
        self.user_id = user_id
        print(self.__str__())

    def __str__(self):
        return (f"----------------------------------------------\n"
                f"Welcome, {self.username} ID: {self.user_id:<7} "
                f"| Role: {self.role: <10}\n"
                f"----------------------------------------------")

    @staticmethod
    def view_all_projects():
        """
        View all projects in project_table.csv
        :return:
        """
        print("Here's all the project tables")
        for i in my_DB.search('project_table').table:
            print(
                f'{my_DB.search("project_table").table.index(i) + 1:<3}| {i}')

    def see_advisor_request(self):
        """
        See request if a Lead request them to be a supervisor
        :return:
        """
        print("Here are the the requests")
        response = my_DB.search('advisor_pending_table').filter(
            lambda x: x['to_be_advisor'] == self.username).table
        for i in response:
            print(f"Name: {i['ProjectID']}\n"
                  f"Request: {i['Response']}\n")

    def accept_or_deny_request(self):
        """
        Accept or deny request to be an advisor
        :return:
        """
        pending_table = my_DB.search('advisor_pending_table').filter(
            lambda x: x["to_be_advisor"] == self.username).table
        if pending_table:
            print('These group wants you as their advisor.')
            for i in pending_table:
                print(f'{pending_table.index(i) + 1:<3}| ProjectID: '
                      f'{i["ProjectID"]} wants you as their advisor.')
            _choice = int(
                input('Which group to you want to update your status?: ')
            ) - 1
            if _choice < len(pending_table):
                join_choice = input(f'Would you like to advise '
                                    f'{pending_table[_choice]["ProjectID"]}? '
                                    f'type(Y/N): '
                                    ).lower()
                project_id_selected = pending_table[_choice]['ProjectID']
                # if the user excepts the request
                if join_choice == 'y':
                    adv = my_DB.search(
                        'project_table').table[_choice - 1]["Advisor"]
                    if adv == "":
                        print('You have accepted their request. '
                              'You are now their advisor.')
                        # update the member_pending_table
                        my_DB.search('advisor_pending_table').update(
                            project_id_selected, 'ProjectID', 'Response',
                            'Accepted'
                        )
                        my_DB.search('advisor_pending_table').update(
                            project_id_selected, 'ProjectID', 'Response_date',
                            '16/12/23'
                        )
                        my_DB.search('login').update(self.username,
                                                     'username', 'role',
                                                     'advisor')
                        my_DB.search('project_table').update(
                            project_id_selected, 'ProjectID', 'Advisor',
                            self.username)
                    else:
                        print("Sorry this group already got an advisor .")
                # if the user denies the request
                else:
                    print('You have denied their request.\n')
                    # update the member_pending_table
                    my_DB.search('advisor_pending_table').update(
                        self.user_id, 'ProjectID', 'Response', 'Denied'
                    )
                    my_DB.search('advisor_pending_table').update(
                        self.user_id, 'ProjectID', 'Response_date', '16/12/23'
                    )
        else:
            print("You don't have any invitation yet.\n")


class Advisor(Faculty):
    def __init__(self, user_id):
        super().__init__(user_id)

    def change_project_status(self):
        """
        Change to project status to approve deny or pending
        :return:
        """
        project_table = my_DB.search('project_table').filter(
            lambda x: x['Advisor'] == self.username).table
        print('Here are the project(s) you are advising')
        for i in project_table:
            print(f'{project_table.index(i) + 1:<3}| {i}')
        _choice = int(input('Which project would you like to approve?: ')) - 1
        if _choice < len(project_table):
            chosen_project = project_table[_choice]
            result = input('How would you like to approve this project? '
                           '(A)Approve/(D)Deny: ').lower()
            if result == 'a':
                print(f"Project {chosen_project['Title']} has been Approved")
                new_status = 'Approve'
            else:
                print(f"Project {chosen_project['Title']} has been Denied")
                new_status = 'Deny'
            my_DB.search('project_table').table[_choice]['Status'] = new_status
        else:
            print('Project does not exist please try again.')


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
    _login = Table('login', converted_login)
    my_DB.insert(_login)

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
    print('------------------------------------------')

    print('Table: persons')
    for i in my_DB.search('persons').table:
        print(i)
    print('------------------------------------------')

    print('Table: login')
    login_table = open('login.csv', 'w')
    writer = csv.writer(login_table)
    writer.writerow([
        'ID', 'username', 'password', 'role'
    ])
    for dictionary in my_DB.search('login').table:
        writer.writerow(dictionary.values())
    login_table.close()
    login_table = open('login.csv', 'r')
    print("The content of the csv file is:")
    for i in my_DB.search('login').table:
        print(i)
    login_table.close()
    print('------------------------------------------')

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
    for i in my_DB.search('project_table').table:
        print(i)
    project_table.close()
    print('------------------------------------------')

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
    for i in my_DB.search('advisor_pending_table').table:
        print(i)
    advisor_pending_table.close()
    print('------------------------------------------')

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
    for i in my_DB.search('member_pending_table').table:
        print(i)
    member_pending_table.close()
    print('------------------------------------------')
    # the link below is how to change table to csv
    # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()
while val is None:
    print("Username or password is incorrect try again.")
    val = login()

# based on the return value for login, activate the code that performs
# activities according to the role defined for that person_id

# admin actions
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
        print()
        # view table
        if choice == 1:
            admin.check_table()
        # edit table
        elif choice == 2:
            admin.edit_table()
        # insert dict in table
        elif choice == 3:
            admin.insert_dict()
        # delete dict in table
        elif choice == 4:
            admin.delete_dict()
        # exit program
        elif choice == 0:
            in_program = False
        # inform user that the action does not exist
        else:
            print('That action does not exist. Please try again')
# student action
elif val[1] == 'student':
    in_program = True
    while in_program:
        student = Student(val[0])
        choice = int(input("What would you like to do?:\n"
                           "(1) See pending request\n"
                           "(2) Accept or Decline request\n"
                           "(3) Create project\n"
                           "(0) Exit\n"
                           "Enter choice (numbers only): "))
        print()
        # see pending requests
        if choice == 1:
            student.see_pending_request()
        # accept or deny requests
        elif choice == 2:
            student.accept_or_deny_request()
        # create project
        elif choice == 3:
            student.create_project()
        # exit program
        elif choice == 0:
            in_program = False
        else:
            print('That action does not exist. Please try again')
elif val[1] == 'lead':
    in_program = True
    while in_program:
        lead = Lead(val[0])
        choice = int(input("What would you like to do?:\n"
                           "(1) See project status\n"
                           "(2) See project info\n"
                           "(3) Modify project info\n"
                           "(4) See request response\n"
                           "(5) Send member request\n"
                           "(6) Send advisor request\n"
                           "(0) Exit\n"
                           "Enter choice (numbers only): "))
        print()
        # see project status
        if choice == 1:
            lead.see_project_status()
        # see project info
        elif choice == 2:
            lead.see_project_info()
        # modify project info
        elif choice == 3:
            lead.modify_project_info()
        # see request respond
        elif choice == 4:
            lead.see_request_response()
        # send member request
        elif choice == 5:
            lead.send_member_request()
        # send send advisor request
        elif choice == 6:
            lead.send_advisor_request()
        # exit program
        elif choice == 0:
            in_program = False
        else:
            print('That action does not exist. Please try again')
# member action
elif val[1] == 'member':
    in_program = True
    while in_program:
        member = Member(val[0])
        choice = int(input("What would you like to do?:\n"
                           "(1) See project status\n"
                           "(2) See project info\n"
                           "(3) See request respond\n"
                           "(0) Exit\n"
                           "Enter choice (numbers only): "))
        print()
        # see project status
        if choice == 1:
            member.see_project_status()
        # see project info
        elif choice == 2:
            member.see_project_info()
        # modify project info
        elif choice == 3:
            member.see_request_response()
        elif choice == 0:
            in_program = False
        else:
            print('That action does not exist. Please try again')
# faculty actions
elif val[1] == 'faculty':
    in_program = True
    while in_program:
        faculty = Faculty(val[0])
        choice = int(input("What would you like to do?:\n"
                           "(1) View all projects\n"
                           "(2) See advisor request\n"
                           "(3) Accept or deny request\n"
                           "(0) Exit\n"
                           "Enter choice (numbers only): "))
        print()
        # view all projects
        if choice == 1:
            faculty.view_all_projects()
        # see advisor requests
        elif choice == 2:
            faculty.see_advisor_request()
        # accept or deny request
        elif choice == 3:
            faculty.accept_or_deny_request()
        # exit program
        elif choice == 0:
            in_program = False
        else:
            print('That action does not exist. Please try again')
# advisor actions
elif val[1] == 'advisor':
    in_program = True
    while in_program:
        advisor = Advisor(val[0])
        choice = int(input("What would you like to do?:\n"
                           "(1) View all projects\n"
                           "(2) Change project status\n"
                           "(0) Exit\n"
                           "Enter choice (numbers only): "))
        print()
        # view all projects
        if choice == 1:
            advisor.view_all_projects()
        # update the project status
        elif choice == 2:
            advisor.change_project_status()
        # exit program
        elif choice == 0:
            in_program = False
        else:
            print('That action does not exist. Please try again')

# once everything is done, make a call to the exit function
exit_program()
