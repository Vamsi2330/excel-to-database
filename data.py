
import pandas as pd
import mysql.connector


data = pd.read_excel(r"D:\vs code\profile\covi.xlsx")
val = data.values

try:
    connection = mysql.connector.connect(user ="root",password = "root",host = "localhost",db= "covid")
    cusor = connection.cursor()

    #cusor.execute("create table covi(State_Name varchar(50),Confiremd int(10),Cuired int(10),Deaths int(10),State_Code int(5))")
    query = "INSERT INTO covi (State_Name,Confiremd,Cuired,Deaths,State_code) VALUES(%s,%s,%s,%s,%s)"

    for i in range(len(val)) :
        State_name = val[i][0]
        Confiremd = val[i][1]
        Cuired = val[i][2]
        Deaths = val[i][3]
        State_Code = val[i][4]
        i = i+1
        values = [State_name,Confiremd,Cuired,Deaths,State_Code]
        cusor.execute(query,values)
        
    cusor.execute("select * from covi")
    
    print(cusor.fetchall())
    print(str(cusor.rowcount)+" are inserted.")
except Exception  as e:
    print(e)

