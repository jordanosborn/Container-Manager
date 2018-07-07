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

import handlers

docker_env = docker.APIClient()

# if already in list switch to management request!

def make_app():
    return tornado.web.Application([
        (r"/", handlers.MainHandler, {'docker_env': docker_env}),
        (r"/images", handlers.ImagesHandler, {'docker_env': docker_env}),
        (r"/build/(.*)", handlers.BuildHandler, {'docker_env': docker_env, 'whitelisted_base_images': config['image_whitelist']}),
        (r"/pull/(.*)/(.*)", handlers.PullHandler, {'whitelist': config['image_whitelist'], 'docker_env': docker_env}),
        (r"/pull/(.*)", handlers.PullHandler, {'whitelist': config['image_whitelist'], 'docker_env': docker_env}),
        (r"/volume/(.*)", handlers.VolumeHandler, {'docker_env': docker_env}),
        (r"/help", handlers.HelpHandler, {"help_json": help_json}),
        #(r"/help", tornado.web.RedirectHandler, dict(url=r"/help/all")),
        (r"/outstream", handlers.OutStreamHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(config['port'])
    tornado.ioloop.IOLoop.current().start()
