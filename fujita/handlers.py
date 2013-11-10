from tornado import web, websocket

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

class LogHandler(websocket.WebSocketHandler):
    def open(self):
        print "Opened new socket"
        self.application.django.add_waiter(self.new_line)

    def on_close(self):
        print "Closed socket"
        self.application.django.remove_waiter(self.new_line)

    def new_line(self, id, fd, line):
        self.write_message({
            'id': id,
            'fd': fd,
            'line': line
        })
