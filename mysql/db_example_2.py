from mysql.connector import connect, Error
# Load environment variables
# https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv
load_dotenv()

import os

CONFIG = {
    'host': os.getenv('DB_HOST'), 
    'user': os.getenv('DB_USERNAME'), 
    'password': os.getenv('DB_PASSWORD'), 
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT'),
    'autocommit': False
}

try:
    with connect(**CONFIG) as conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute('select * from users')
                rows = cursor.fetchall()
                for item in rows:
                    print(f"name={item[0]}, email={item[1]}")
        finally:
            cursor.close()
except Error as e:
    print(e)