import tornado.web
import json
import os
from helpers import PathHandler

class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World this is a python command executed from the backend.")

class ListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class QueryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}") # res.send() in JS
        else:
            self.set_status(400)
            self.write(f"{num} is not a valid integer.")   
            
            
class ResourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self,studentName, courseId):
        self.write(f"Welcome {studentName} you are viewing course {courseId}")

class LisArrayRequestHandler(tornado.web.RequestHandler):
    def get(self):
        my_local_file = PathHandler.get_file_path("list.txt")
        fh = open(my_local_file, 'r')
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))
    def post(self):
        my_local_file = PathHandler.get_file_path("list.txt")
        fruit = self.get_argument("fruit")
        fh = open(my_local_file, "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully."}))
    
    
class UploadFileHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files["file"]
        for f in files:
            folder_path = PathHandler.get_folder_path('upload')
            fh = open(f"{folder_path}/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        self.redirect(f"/img/{f.filename}")
    def get(self):
        folder = PathHandler.get_folder_path("static")
        file = PathHandler.get_file_path(f'{folder}/fileUploader.html')
        self.render(file)
        
class RenderHandler(tornado.web.StaticFileHandler):
    async def get(self, path: str, include_body: bool = True) -> None:
        # for demo/test purposes
        return await super(RenderHandler, self).get(path, include_body)