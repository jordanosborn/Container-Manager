import tornado.ioloop
import tornado.web
import asyncio
from inflection import titleize

class HelpHandler(tornado.web.RequestHandler):
    def initialize(self, help_json):
        self.help_dict = help_json

    def get(self, help_page):
        help_page = help_page if help_page != '' else 'all'
        self.write(f'{titleize(help_page)}<br><br>{self.help_dict[help_page]}')

