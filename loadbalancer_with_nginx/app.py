import tornado.web # import request handlers
import tornado.ioloop # import a thread which will continuously listen to port
import os
import sys

class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(f'Server from {os.getpid()}')
        
        
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/healthcheck", BasicRequestHandler)
    ])
    port = 8882
    if sys.argv.__len__() > 1:
        port = sys.argv[1]
    app.listen(port)
    print(f"I'm listening on port {port}")
    tornado.ioloop.IOLoop.current().start()