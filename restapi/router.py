# coding: utf-8

import webob.dec
import webob.exc
import routes
import routes.middleware


class Router(object):

    def __init__(self, global_conf, **local_conf):
        mapper = routes.Mapper()
        self._setup_routes(mapper)
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,
                                                          mapper)

    @webob.dec.wsgify(RequestClass=webob.Request)
    def __call__(self, req):
        """Route the incoming request to a controller based on self.map.

        If no match, return a 404.

        """
        # return 'Hello, World!!'
        return self._router

    @staticmethod
    @webob.dec.wsgify(RequestClass=webob.Request)
    def _dispatch(req):
        """Dispatch the request to the appropriate controller.

        Called by self._router after matching the incoming request to a route
        and putting the information into req.environ.  Either returns 404
        or the routed WSGI app's response.

        """
        # RoutesMiddlewareを使うと、environに結果が保存される
        # この内容を元に処理をディスパッチすれば良い
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            return webob.exc.HTTPNotFound()

        app = match['controller']
        return 'Hello {0}'.format(app)

    def _setup_routes(self, mapper):
        mapper.connect('get_rout', '/',
                       controller='root', action='list',
                       conditions={'method': 'GET'},
                       requirements={'format': R'json|xml'})
