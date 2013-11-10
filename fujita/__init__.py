from tornado import ioloop, web

from .handlers import LogHandler, IndexHandler
from .runner import DjangoRunner

def main():
    print "Django Fujita - Starting up"

    handlers = [
        (r"/log", LogHandler),
        (r"/", IndexHandler),
    ]
    settings = dict(
        debug=True,
        template_path="fujita/templates/", # XXX TODO fix me - http://stackoverflow.com/a/50905
    )

    print "Application listening on 5665"
    application = web.Application(handlers, **settings)
    application.listen(5665)

    # XXX TODO fix me
    application.django = DjangoRunner([
            "/home/evan/python-envs/fujita/bin/python",
            "/home/evan/projects/django-fujita/testproject/manage.py",
            "runserver",
            "0:5666"
        ])

    print "Starting main IO loop..."
    ioloop.IOLoop.instance().start()
