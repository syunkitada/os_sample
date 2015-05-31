from beaker.middleware import SessionMiddleware


def create_filter(global_conf, **local_conf):

    def _filter(app):
        session_opts = {'session.type': 'file',
                        'session.data_dir': './data',
                        'session.cookie_expires': True,
                        'session.auto': True
                        }
        return SessionMiddleware(app, config=session_opts)
    return _filter
