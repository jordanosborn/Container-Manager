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
        if 'name' in query_args.keys():
            filter_name = query_args['name'][0].decode('utf-8')
            images = list(filter(lambda x: x['RepoTags'][0].split(':')[0] == filter_name, images))
        self.write(pprint.pformat(images))
