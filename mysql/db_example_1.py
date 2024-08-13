import mysql.connector;
# Django users can get the instance of the connection used by the ORM from django.db.connection
# from django.db import connection

# Load environment variables
# https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv
load_dotenv()

import os

connection = mysql.connector.connect(
    host = os.getenv('DB_HOST'), 
    user = os.getenv('DB_USERNAME'), 
    password = os.getenv('DB_PASSWORD'), 
    database = os.getenv('DB_NAME'),
    port = os.getenv('DB_PORT')
    )

print('Hi');
cursor = connection.cursor();

cursor.execute('SELECT COUNT(*) FROM users')
result = cursor.fetchone()
print(result)
# (1,)

cursor.execute('SELECT name, email FROM users');
rows = cursor.fetchall(); # result is a array of tuples
for item in rows:
    print(f"name={item[0]}, email={item[1]}")
    # name=Margo, email=m@gmail.com
    
# secure usage of parameters to avoid sql injections like
# name = '"Bob; DROP TABLE users"';
# or 
# name = '"Bob; SELECT true"';
# e.g. here: https://realpython.com/prevent-python-sql-injection/
cursor.execute('SELECT name, email FROM users WHERE name = %s', ('Margo',))
row = cursor.fetchone()
print(f'name={row[0]}, email={row[1]}')
cursor.close()
connection.close()