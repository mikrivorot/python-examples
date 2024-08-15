import tornado.web
import tornado.ioloop
import psycopg2
import json
import os

# we expect connection to be defined, but we handle errors in classes
connection = None

class connectHandler(tornado.web.RequestHandler):
    def post(self):
        # Normally, when you create a variable inside a function, that variable is local, 
        # and can only be used inside that function.
        # If you create a variable with the same name inside a function, this variable will be local.
        # The global variable with the same name will remain as it was, global and with the original value.
        # use the global keyword if you want to change a global variable inside a function.
        global connection
        connection = psycopg2.connect(
            host = os.getenv('DB_HOST'), 
            user = os.getenv('DB_USERNAME'), 
            password = os.getenv('DB_PASSWORD'), 
            database = os.getenv('DB_NAME'),
            port = os.getenv('DB_PORT')
            );
        #  'json.dumps()' is a method in the json module that converts a Python object (like a dictionary) into a JSON formatted string
        self.set_header("content-type", "application/json")
        self.write(json.dumps({"success": "true"}))
        
class getHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("stateful.html")

class readHandler(tornado.web.RequestHandler):
    def post(self):
        global connection
        try:
            cursor = connection.cursor()
            #execute query
            cursor.execute("select id, name from users where name = 'Margo'")
            
            # Array of tuples
            # rows = cursor.fetchall() 
            # rows = cursor.fetchmany(50)
            
            # A tuple
            row = cursor.fetchone()

            #close the cursor
            cursor.close()
            
            #close the connection
            self.set_header("content-type", "application/json")
            self.write(json.dumps(row)) # convert tuple into json (array)
        except: 
            self.write(json.dumps({"success": False, "error": "Failed read the database."}))

    def get(self):
        self.render("stateless.html")

class closeHandler(tornado.web.RequestHandler):
    def post(self):
        global connection

        self.set_header("content-type", "application/json")
        try:
            #close the connection
            connection.close()
            self.write(json.dumps({"success": True}))
        except: 
            self.write(json.dumps({"success": False, "error": "Failed to close database."}))
