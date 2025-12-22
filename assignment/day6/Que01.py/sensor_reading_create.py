import mysql.connector as myc
from datetime import datetime
connection= myc.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_application",
    use_pure=True
)
id=int(input("Enter id: "))
temperature=int(input("Enter Temperature: "))
humidity=int(input("Enter Humidity: "))

query=f"INSERT INTO sensor_reading (id,temperature,humidity,timestamp) VALUES({id},{temperature},{humidity},'{datetime.now()}')"

cursor=connection.cursor()
cursor.execute(query)

connection.commit()

cursor.close()
connection.close()