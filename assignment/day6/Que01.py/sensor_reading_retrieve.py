import mysql.connector as myc

connection= myc.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_application",
    use_pure=True
)

temperature=int(input("Enter Temperature compare: "))

query="SELECT * FROM sensor_reading";
query1="SELECT * FROM sensor_reading WHERE temperature <25";

cursor=connection.cursor()

cursor.execute(query)

readings=cursor.fetchall()

print(readings)

cursor.execute(query1)

filtered_reading = cursor.fetchall()

print(filtered_reading)

cursor.close()

connection.close()