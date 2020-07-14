import os
import pymysql

# Get username from cloud9 workspace
# (modify this variable if runnin on another enviroment)
username = os.getenv('C9_USER')

# connect to the database
connection = pymysql.connect(host = 'localhost',
                            user = username,
                            password='',
                            db = 'Chinook')

try:
    #run aquery
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()