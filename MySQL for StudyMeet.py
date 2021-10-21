#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install mysql-connector-python


# In[3]:


pip install pandas


# In[4]:


# Import libraries

import mysql.connector
from mysql.connector import Error
import pandas as pd


# In[5]:


# Function: Connecting to server

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# In[6]:


# Function: Creating a new Database

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


# In[7]:


# Function: Connecting to Database

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# In[8]:


# Function: Execute Query 

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# In[9]:


# Function: Read Query

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


# In[10]:


# Connection with server

pw = "SlackTechie21"
db= "mysql_StudyMeet"

connection=create_server_connection("localhost","root",pw)


# In[11]:


# Create mysql_StudyMeet 

create_database_query = "Create database mysql_StudyMeet"

create_database(connection, create_database_query)


# In[20]:


# Create a table "User"

create_user_table= """
create table user(
user_id int primary key,
user_name varchar(30) not null,
user_password varchar(30) not null,
user_email varchar(50) not null);
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_user_table)


# In[21]:


# Insert data in "User"

insert_user = """
insert into user values (1,'Tim','12345','Tim.Müller@tu-dortmund.de');
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, insert_user)


# In[22]:


# Select statement

q1="""
select * from user;
"""

connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q1)

for result in results:
    print(result)


# In[24]:


# Create a table "Group"

create_group_table= """
create table team(
team_id int primary key,
team_name varchar(30) not null,
team_topic varchar(50) not null,
team_member int);
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_group_table)


# In[25]:


# Create a table "Membership"

create_membership_table= """
create table membership(
membership_id int primary key,
team_id int,
user_id int,
constraint fk_team foreign key (team_id) references team(team_id),
constraint fk_user foreign key(user_id) references user(user_id));
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_membership_table)


# In[ ]:




