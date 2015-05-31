# coding: utf-8


class Hello(object):

    def __init__(self, global_conf, **local_conf):
        self.name = local_conf['user']

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return ['Hello, World!! by %s' % (self.name)]
