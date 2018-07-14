import tornado.ioloop
import threading
import tornado.web
import json
import sys
import docker

import handlers

def build_config():
    config = {}
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            config = json.loads(f.read())
    else:
        with open('config.json', 'r') as f:
            config = json.loads(f.read())

    help_json = {}
    with open('help.json', 'r') as f:
        help_json = json.loads(f.read())
    return (config, help_json)

# if already in list switch to management request!
def make_app(config, help_json):
    docker_env = docker.APIClient()
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
import sys
if __name__ == "__main__":
    config, help_json = build_config()
    app = make_app(config, help_json)
    app.listen(config['port'])
    print(f'Server running on 127.0.0.1:{config["port"]}')
    t = threading.Thread(target=tornado.ioloop.IOLoop.current().start, daemon=True)
    t.start()
    while True:
        cmd = input('cmd> ')
        if cmd == 'quit':
            print('Server stopping')
            sys.exit()
