import tornado.web
import os
import dockerfile_parse
from io import BytesIO
import json

class BuildHandler(tornado.web.RequestHandler):
    def initialize(self, docker_env, whitelisted_base_images):
        self.docker_env = docker_env
        self.whitelisted_base_images = whitelisted_base_images

    def post(self, tag):
        query_args = self.request.query_arguments
        #if not pull if whitelisted fetch localhost:.../pull/image
        name, body = None, None
        for key, value in self.request.files.items():
            name = key
            body = value[0]['body']
        if name and body:
            dfp = dockerfile_parse.DockerfileParser()
            dfp.content = body
            if dfp.baseimage.split(':')[0] in self.whitelisted_base_images:
                output = ''
                f = BytesIO(body)
                for line in self.docker_env.build(fileobj=f, rm=True, tag=tag):
                    output += line.decode('utf-8') + '\n'
                self.write(output)
            else:
                self.write('Can\'t build')
        else:
            self.write('Can\'t build')

