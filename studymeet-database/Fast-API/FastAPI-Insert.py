from fastapi import FastAPI
import uvicorn
from MySQL import execute_query, create_db_connection,read_query

app = FastAPI()

pw = "SlackTechie21"
db= "mysql_StudyMeet"
connection = create_db_connection("localhost", "root", pw, db)

@app.get("/insuser/{id}/{name}/{pw}/{mail}")
async def insert_user(id:int,name:str,pw:str,mail:str):
    befehl1="INSERT INTO user VALUES ("
    b_id=str(id)
    befehl2=", '"
    b_name=name
    befehl3= "','"
    b_pw=pw
    b_mail=mail
    befehl4="');"
    insert=befehl1 + b_id + befehl2 + b_name + befehl3 + b_pw + befehl3 + b_mail + befehl4
    return execute_query(connection,insert)

@app.get("/inteam/{team_id}/{team_name}/{team_specialization}/{team_member}/{team_type}/{team_place}/{team_description}/{team_language}/{team_date}")
async def insert_team(team_id:int,team_name:str,team_specialization:str,team_member:int, team_type:str,team_place:str,team_description:str,team_language:str,team_date:str):
    befehl1="INSERT INTO team VALUES ("
    b_id=str(team_id)
    befehl2=", '"
    b_name=team_name
    befehl3= "','"
    b_spec=team_specialization
    b_member=str(team_member)
    b_type=team_type
    b_place=team_place
    b_des=team_description
    b_language=team_language
    b_date= team_date
    befehl4="');"
    insert= befehl1 + b_id + befehl2 + b_name + befehl3 + b_spec + befehl3 + b_member + befehl3 + b_type + befehl3 + b_place + befehl3 + b_des + befehl3 + b_language + befehl3 + b_date + befehl4
    return execute_query(connection,insert)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)   