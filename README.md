# Final project: Senior Project Submissions Program

### 1.) Files in this repository ###
    1. database.py
    2. project_manage.py
    3. persons.csv
    4. login.csv
    5. member_pending_table.csv
    6. advisor_pending_table.csv
    7. TODO.md
    8. Proposal.md
    9. README.md

1. [*** database.py ***]
   - class ConvertCsv:
        This class is used to convert csv files into table.
   - class Database:
        This class is a database used to store objects created from the Table
        class. You can also pull out tables from this class object to use.
   - class Table:
        This class is used to store a list of dictionaries in an object. This
        class also provide users with useful methods make data management easier.

2. [*** project_manage.py ***]
   - class Admin:
        This class has can edit, update, view, insert and delete every table in
        the database.
   - class Student:
        This class has methods corresponding to the action a student role can do.
   - class Lead:
        After the student creates a project they are then given the lead role.
        In this role, they are given new sets of actions.
   - class Member:
        This class Inherits from the Lead class since all the actions in this
        class are what the Lead can already do, although this role has a more
        limited set of actions.
   - class Faculty:
        This class has methods corresponding to the actions a faculty can do.
   - class Advisor:
        This class Inherits from the Faculty class. Once a faculty have accepted
        the become an advisor, they are changed to this role  This class can do 
        everything the faculty can do, but this role can also Approve or Deny 
        the students' projects.
   
   Additional functions in this file:
   - initializing:
        This functions creates and store all the tables needed for the program.
   - login:
        This function prompts the user to input their username and password then
        returns their id and role in a list.
   - exit_program:
        This function runs at the end when a user is no longer using the program.
        It updates and store the changes made from the tables in the database in
        .csv files.
        

### 2.) How to run this project ###
    1. Clone this repo on your local IDE
    2. Run project_manage.py
    3. Login to any account
    4. Do you tasks corresponding to your role
    5. Exit the program once you are finished
    6. See the changes made corresponding to what you did in the csv files


|  Role   |                   Action                    |         Method         |  Class  | Completion percentage |
|:-------:|:-------------------------------------------:|:----------------------:|:-------:|:---------------------:|
|  Admin  |                 View table                  |      check_table       |  Admin  |         100%          |
|  Admin  |                 Edit table                  |       edit_table       |  Admin  |         100%          |
|  Admin  |     Insert a new dictionary into table      |      insert_dict       |  Admin  |         100%          |
|  Admin  |       delete a dictionary from table        |      delete_dict       |  Admin  |         100%          |
| Student |              Create a project               |     create_project     | Student |         100%          |
| Student |    See pending request to become member     |  see_pending_request   | Student |         100%          |
| Student |       Accept or deny to become member       | accept_or_deny_request | Student |         100%          |
| Student |      Send a request to become a member      |      send_request      | Student |         100%          |
|  Lead   |         See their project's status          |   see_project_status   |  Lead   |         100%          |
|  Lead   |       See their project's information       |    see_project_info    |  Lead   |         100%          |
|  Lead   |     Modify their project's information      |  modify_project_info   |  Lead   |         100%          |
|  Lead   |         See member request response         |  see_request_response  |  Lead   |         100%          |
|  Lead   |      Send member request to a student       |  send_member_request   |  Lead   |         100%          |
|  Lead   |      Send advisor request to a faculty      |  send_advisor_request  |  Lead   |         100%          |
|  Lead   |      Send advisor request to a faculty      |  send_advisor_request  |  Lead   |         100%          |
| Member  |         See their project's status          |   see_project_status   | Member  |         100%          |
| Member  |       See their project's information       |    see_project_info    | Member  |         100%          |
| Member  |         See member request response         |  see_request_response  | Member  |         100%          |
| Faculty |              View all projects              |   view_all_projects    | Faculty |         100%          |
| Faculty |    See pending advisor request for them     |  see_advisor_request   | Faculty |         100%          |
| Faculty |           Accept or deny request            | accept_or_deny_request | Faculty |         100%          |
| Advisor |              View all projects              |   view_all_projects    | Advisor |         100%          |
| Advisor | Change the project status for their project | change_project_status  | Advisor |         100%          |


### 3.) Missing features and Outstanding bugs ###

1. [*** Missing features ***]
    - No private comment sending method for the advisor role to send to the 
      group.
    - More in depth grading system for advisors and faculties. This will allow
      Faculties and advisor to grade projects beyond just the current Approve 
      And denying the project

2. [*** Known Bugs ***]
    - For all the roles, if you do not use the exit in the program the csv files
      will not update according to the changes made in your table
    - Students can send request and accept themselves into the group


If there are any further questions please contact me via email, phasit.r@ku.th