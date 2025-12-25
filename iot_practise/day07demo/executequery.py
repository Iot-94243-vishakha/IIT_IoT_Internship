from utils.dbConnection import getBDConnection

def executeQuery(query):
    """
    Executes CREATE, UPDATE, DELETE, or INSERT SQL queries.
    """

    # Establish connection to the database
    connection = getBDConnection()

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    try:
        # Execute the SQL query
        cursor.execute(query)

        # Save changes to the database
        connection.commit()

    except Exception as error:
        # Rollback if any error occurs
        connection.rollback()
        print("Error executing query:", error)

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()
