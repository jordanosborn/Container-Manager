import tornado.web
import docker
import json

class VolumeHandler(tornado.web.RequestHandler):
    def initialize(self, whitelist, docker_env):
        self.whitelist = whitelist
        self.docker_env = docker_env

    def post(self, image, tag=None):
        query_args = self.request.query_arguments
        if image in self.whitelist:
            output = ''
            for line in self.docker_env.pull(image, tag, stream=True):
                output += line.decode('utf-8') + '\n'
            self.write(output)
        else:
            self.write('403 Image blacklisted.')
