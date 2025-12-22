import mysql.connector as myc
def getIOTConnection():
    connection=myc.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root',
        database='iot_application',
        use_pure=True
    )

    return connection