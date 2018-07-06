import tornado.ioloop
import tornado.web
import docker
import json

class PullHandler(tornado.web.RequestHandler):
    def initialize(self, whitelist, docker_env):
        self.whitelist = whitelist
        self.docker_env = docker_env

    def post(self, image, tag=None):
        if image in self.whitelist:
            self.docker_env.images.pull(image, tag)
            self.write('success')
        else:
            self.write('403 Image blacklisted.')

