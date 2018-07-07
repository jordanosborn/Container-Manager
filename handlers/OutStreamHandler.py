import tornado.websocket

class OutStreamHandler(tornado.websocket.WebSocketHandler):
    def initialize(self):
        self.message_queue = []

    def add_to_queue(self, message):
        

    def check_origin(self, origin):
        return True
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")