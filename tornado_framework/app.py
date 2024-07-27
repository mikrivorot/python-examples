
import tornado.web # import request handlers
import tornado.ioloop # import a thread which will continiously listen to port
from handlers import BasicRequestHandler, ListRequestHandler, QueryParamRequestHandler, ResourceParamRequestHandler, LisArrayRequestHandler, MainRequestHandler, UploadImgHandler, \
    ImageHandler
from helpers import PathHandler

    
# In Python, __name__ is a special variable assigned to the name of the Python module by the interpreter.
# If your module is invoked as a script, then the string ‘__main__’ will automatically be assigned to the special variable __name__. 
# But if you import your module into another module, the string ‘my_module’ will be assigned to __name__
if __name__ == "__main__":
    app = tornado.web.Application([
        # raw string '/', an actual backslash and not part of an escape code
        (r"/main", MainRequestHandler),
        (r"/", BasicRequestHandler),
        (r"/animal", ListRequestHandler),
        (r"/list", LisArrayRequestHandler),
        (r"/isEven", QueryParamRequestHandler),
        (r"/students/([A-Za-z]+)/([0-9]+)", ResourceParamRequestHandler),
        (r"/upload", UploadImgHandler),
        # Note: path depends on root path defined by Vscode, so we use helper
        (r"/img/(.*)", ImageHandler, {'path': PathHandler.get_folder_path('upload')}), 
    ])
    
    port = 8882 # Everything lower 1000 reserved for the system
    app.listen(port)
    print(f"Application is ready and listening on port {port}") # The f means Formatted string literals, see https://docs.python.org/3.6/reference/lexical_analysis.html#formatted-string-literals
    tornado.ioloop.IOLoop.current().start() # Starts the I/O loop to listen