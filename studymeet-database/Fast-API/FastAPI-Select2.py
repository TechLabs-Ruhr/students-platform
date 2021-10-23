from fastapi import FastAPI
import uvicorn
from MySQL import execute_query, create_db_connection,read_query

app = FastAPI()

pw = "SlackTechie21"
db= "mysql_StudyMeet"
connection = create_db_connection("localhost", "root", pw, db)

@app.get("/user/{user}")
async def select_user(user:int): 
    befehl1= "SELECT * FROM mysql_studymeet.user WHERE user_id ="
    befehl2= str(user)
    last= ";"
    select=befehl1+befehl2+last
    return read_query(connection,select)

@app.get("/team/{team}")
async def select_tean(team:int): 
    befehl1= "SELECT * FROM mysql_studymeet.team WHERE team_id ="
    befehl2= str(team)
    last= ";"
    select=befehl1+befehl2+last
    return read_query(connection,select)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)   