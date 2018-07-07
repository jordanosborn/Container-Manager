import tornado.web
import os

class BuildHandler(tornado.web.RequestHandler):
    def initialize(self, docker_env):
        self.docker_env = docker_env

    def post(self):
        #if not pull if whitelisted fetch localhost:.../pull/image
        for key, value in self.request.files.items():
            name = key
            body = value['body']

        if name and body:
            os.mkdir(name)
            with open(name + '/Dockerfile', 'w') as f:
                f.write(body)
            self.docker_env.images.build()

        self.write('Built')

