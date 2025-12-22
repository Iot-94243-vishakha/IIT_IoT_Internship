import mysql.connector as myc
from datetime import datetime
connection= myc.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture",
    
    use_pure=True
)

sensor_ID=int(input("Enter sensor_ID: "))
moisture_level=int(input("Enter moisture_level: "))

date_time= datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")

query=f"INSERT INTO smart_agriculture(sensor_ID,moisture_level,data_time ) VALUES({sensor_ID},{moisture_level},'{date_time.now()}')"

cursor=connection.cursor()
cursor.execute(query)

connection.commit()

cursor.close()
connection.close()