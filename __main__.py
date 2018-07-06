import tornado.ioloop

import tornado.web
import json
import sys
import docker
import re

config = {}

if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        config = json.loads(f.read())

help_json = {}
with open('help.json', 'r') as f:
    help_json = json.loads(f.read())

all_string = ''
for key, value in help_json.items():
    all_string += f'{key}<br>{value}<br>'
help_json['all'] = all_string

import handlers

docker_env = docker.from_env()

def make_app():
    return tornado.web.Application([
        (r"/", handlers.MainHandler, {}),
        (r"/build", handlers.BuildHandler, {'docker_env': docker_env}),
        (r"/pull/(.*)/(.*)", handlers.PullHandler, {'whitelist': config['image_whitelist'], 'docker_env': docker_env}),
        (r"/pull/(.*)", handlers.PullHandler, {'whitelist': config['image_whitelist'], 'docker_env': docker_env}),
        (r"/help/(.*)", handlers.HelpHandler, {"help_json" : help_json}),
        (r"/help", tornado.web.RedirectHandler, dict(url=r"/help/all"))
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(config['port'])
    tornado.ioloop.IOLoop.current().start()
