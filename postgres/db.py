# need postgres installation to install psycopg2
import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os
connection = psycopg2.connect(
    host = os.getenv('DB_HOST'), 
    user = os.getenv('DB_USERNAME'), 
    password = os.getenv('DB_PASSWORD'), 
    database = os.getenv('DB_NAME'),
    port = os.getenv('DB_PORT')
    );


# SQL queries
# What is a cursor? What is a cursor factory? 
# Do we have ORMs like Sequelize?

cursor = connection.cursor(); # client-side cursor, so we will do caching here, on client, OK for huge select queries
# + minimize overhead on server-side
# - client might have not enough memory to story fetched data

# cursor = connection.cursor(<name>); will be server-side cursor

#cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', ('Ivan', 'i@gmail.com'))
#connection.commit() # connection.set_session(autocommit=True)
cursor.execute('SELECT * FROM users');
rows = cursor.fetchall(); # result is a array of tuples
# what os the difference between cursor.fetchmany(50) and cursor.execute('SELECT * FROM users LIMIT 50');
for item in rows:
    print(f"id={item[0]}, name={item[1]}, email={item[2]}")

# Expected output
# id=1, name=John Doe, email=john@example.com
# id=2, name=Margo, email=m@gmail.com
# id=5, name=Ivan, email=i@gmail.com
connection.close()