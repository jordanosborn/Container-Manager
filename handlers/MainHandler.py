import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, docker_env):
        self.docker_env = docker_env

    def get(self):
        self.write(self.docker_env.version())

    def post(self):
            self.write(f'{{"Status": {str(self.docker_env.ping()).lower()}}}')

