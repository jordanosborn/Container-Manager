import tornado.web
import docker
import json
import pprint

class ImagesHandler(tornado.web.RequestHandler):
    def initialize(self, docker_env):
        self.docker_env = docker_env

    def post(self):
        query_args = self.request.query_arguments
        images = self.docker_env.images()
        self.write(pprint.pformat(images))
