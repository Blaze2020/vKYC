# Performing Database operations

import sqlite3 as sql


# Inserting into Database
def insert_data(username, password):
    global connection
    try:
        connection = sql.connect('E:\\Development\\Python_Projects\\vKYC\\databases\\UserData')
        print('Connected To Database')
        cursor = connection.cursor()
        insertdata = """INSERT INTO User_Table (EMAIL,PASSWORD) VALUES (?,?)"""
        user_data = (username, password)
        cursor.execute(insertdata, user_data)
        connection.commit()
    except Exception:
        print('Data Not Inserted')
    else:
        print("Data Inserted")
    finally:
        connection.close()
        print('Connection Closed')


# Fetching Data From Database
def fetch_data(username, password):
    global connection
    try:
        connection = sql.connect('E:\\Development\\Python_Projects\\vKYC\\databases\\UserData')
        print('Connected To Database')
        cursor = connection.cursor()
        fetchdata = """SELECT * FROM User_Table WHERE EMAIL='{0}' AND PASSWORD='{1}'""".format(username, password)
        cursor.execute(fetchdata)
        # connection.commit()
        user_data = cursor.fetchone()
        # print(user_data)
        if user_data is not None:
            print(user_data)
            print('Data Fetched')
            return True
        else:
            return False
    except Exception:
        print('Data Not Fetched')
    finally:
        connection.close()
        print('Connection Closed')

