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

id=int(input("Enter id whose temperature to be updated :"))
temperture=int(input("Enter new Temperature: "))

query=f"UPDATE sensor_reading SET temperature={temperture} WHERE id={id};"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()