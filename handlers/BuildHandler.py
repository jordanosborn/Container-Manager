import tornado.ioloop
import tornado.web

class BuildHandler(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        self.kwargs = kwargs

    def get(self):
        self.write()

