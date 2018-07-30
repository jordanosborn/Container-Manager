import tornado.ioloop
import tornado.web
import asyncio
from inflection import titleize

class HelpHandler(tornado.web.RequestHandler):
    def initialize(self, help_json):
        self.help_dict = help_json

    def get(self):
        query_args = self.request.query_arguments
        keys = []
        if 'command' in query_args.keys() and query_args['command'] != 'all':
            required_help = ''
            for q in query_args['command']:
                print(q)
                qd = q.decode('utf-8')
                if qd in self.help_dict:
                    required_help += f'{titleize(qd)}<br><br>{self.help_dict[qd]}<br><br>'
        else:
            required_help = '<br><br>'.join([f'{titleize(key)}<br><br>{self.help_dict[key]}' for key in self.help_dict])

        self.write(required_help)

