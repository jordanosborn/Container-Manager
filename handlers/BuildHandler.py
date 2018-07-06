import tornado.ioloop
import tornado.web

class BuildHandler(tornado.web.RequestHandler):
    def initialize(self, docker_env):
        self.docker_env = docker_env

    def post(self):
        #if not pull if whitelisted fetch localhost:.../pull/image
        docker_files = {key: value[0]['body'] for key, value in self.request.files.items()}
        print(docker_files)
        self.write('Built')

