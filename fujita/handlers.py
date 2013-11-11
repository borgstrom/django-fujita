import logging

from tornado import web, websocket

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

class LogHandler(websocket.WebSocketHandler):
    def open(self):
        self.application.django.add_line_waiter(self.new_line)

    def on_close(self):
        self.application.django.remove_line_waiter(self.new_line)

    def new_line(self, id, fd, line):
        self.write_message({
            'id': id,
            'fd': fd,
            'line': line
        })

class StatusHandler(websocket.WebSocketHandler):
    def open(self):
        self.application.django.add_status_waiter(self.new_status)

    def on_close(self):
        self.application.django.remove_status_waiter(self.new_status)

    def new_status(self, code, status):
        self.write_message({
            'code': code,
            'status': status
        })

class StartHandler(web.RequestHandler):
    def post(self):
        self.application.django.start()
        self.write("ok")

class StopHandler(web.RequestHandler):
    def post(self):
        self.application.django.stop()
        self.write("ok")
