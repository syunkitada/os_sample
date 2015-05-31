# coding: utf-8


def pipeline_factory(loader, global_conf, **local_conf):
    """A paste pipeline replica that keys off of auth_strategy."""
    auth_strategy = 'keystone'
    pipeline = local_conf[auth_strategy]

    # space-separated list of filter and app names:
    pipeline = pipeline.split()

    filters = [loader.get_filter(n) for n in pipeline[:-1]]
    app = loader.get_app(pipeline[-1])
    filters.reverse()
    for filter in filters:
        app = filter(app)
    return app


def auth_filter_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    conf['auth'] = True

    def filter(app):
        return AuthFilter(app, conf)

    return filter


def noauth_filter_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    conf['auth'] = False

    def filter(app):
        return AuthFilter(app, conf)

    return filter


class AuthFilter(object):
    def __init__(self, app, conf):
        self.app = app
        self.conf = conf

    def __call__(self, env, start_response):
        if self.conf['auth']:
            print 'AuthFilter AUTH'
        else:
            print 'AuthFilter NOAUTH'

        print '\nDEBUG env'
        print env
        print '\nDEBUG start_response'
        print start_response

        return self.app(env, start_response)
