import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        self.kwargs = kwargs

    def get(self):
        self.write('Server is running.')

