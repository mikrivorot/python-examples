import tornado.web
import json
import os

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World this is a python command executed from the backend.")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}") # res.send() in JS
        else:
            self.set_status(400)
            self.write(f"{num} is not a valid integer.")   
            
            
class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self,studentName, courseId):
        self.write(f"Welcome {studentName} you are viewing course {courseId}")

class lisArrayRequestHandler(tornado.web.RequestHandler):
    def get(self):
        my_local_file = self.__get_file_path("list.txt")
        fh = open(my_local_file, 'r')
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))
    def post(self):
        my_local_file = self.__get_file_path("list.txt")
        fruit = self.get_argument("fruit")
        fh = open(my_local_file, "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully."}))
    def __get_file_path(self, file_name):
        return os.path.join(os.path.dirname(__file__), file_name)