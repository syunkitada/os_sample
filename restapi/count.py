def create_app(global_conf, **local_conf):
    return application


def application(environ, start_response):
    session = environ.get('beaker.session')
    session['counter'] = session.get('counter', 0) + 1
    session.save()
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return 'counter: %d' % session['counter']
