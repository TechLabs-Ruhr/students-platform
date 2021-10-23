# StudyMeet - Database

## MySQL.py
MySQL Database script
**Important:** The MYSQL_Server has to run locally

Setup:
- user name: 'root'
- Password: 'SlackTechie21'
- Database name: 'mysql_StudyMeet'
- host name: 'localhost'

When changing data, edit in code!

## FastAPI-Select2.py
Function to select wanted groups or users.

Setup process:
- console: python3 FastAPI-Select2-py
- go to browser, to select an user: http://127.0.0.1:8000/user/2 (2 stands for the user-id)
- go to browser, to select a grouop: http://127.0.0.1:8000/team/2 (2 stand for the group-id)
- to see the documentation, go to http://127.0.0.1:8000/docs

To end the process, in console: Strg + C

## FastAPI-Insert.py
Function to insert new group or user

Setup process:
- console: python3 FastAPI-Insert.py
- go to browser, to insert a new user: http://127.0.0.1:8000/insuser/{id}/{name}/{pw}/{mail} with wanted attributes (**WARNING:** ID can't be given twice!); return is null
- go to browser, to insert a new group: http://127.0.0.1:8000/inteam/{team_id}/{team_name}/{team_specialization}/{team_member}/{team_type}/{team_place}/{team_description}/{team_language}/{team_date} with wanted attributes (same notes as user)
- to see the documentation, go to http://127.0.0.1:8000/docs

To end the process, in console: Strg + C
