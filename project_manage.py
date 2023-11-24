# import database module
from database import ConvertCsv, DataBase, Table
import csv

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
    project_table = Table('project_table', [])
    my_DB.insert(project_table)
    # create advisor_pending_request object and insert into database
    advisor_pending_request = Table('advisor_pending_table', [])
    my_DB.insert(advisor_pending_request)
    # create  object and insert into database
    member_pending_request = Table('member_pending_table', [])
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
    # print(username_ls)
    # print(password_ls)
    if username in username_ls:
        user_index = username_ls.index(username)
        if password == password_ls[user_index]:
            return (
                my_DB.search('login').select(['person_id', 'role'])[user_index]
            )
        else:
            return None
    else:
        return None


# define a function called exit
def exit():
    print('Table: persons')
    for i in my_DB.search('persons').table:
        print(i)
    print('-----')
    print('Table: login')
    for i in my_DB.search('login').table:
        print(i)
    print('-----')

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list
   # of dictionaries. For this project, you also need to know how to do the reverse,
   # i.e., writing out to a csv file given a list of dictionaries. See the link below
   # for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()


# based on the return value for login, activate the code that performs
# activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everything is done, make a call to the exit function
exit()
