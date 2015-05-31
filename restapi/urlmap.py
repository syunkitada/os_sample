# coding: utf-8

import paste.urlmap


# nova.api.openstack.urlmap:urlmap_factory もこれ
# ちなみに、paste.urlmap.urlmap_factoryも同じ実装でnovaでもそれをパクってる
def urlmap_factory(loader, global_conf, **local_conf):
    if 'not_found_app' in local_conf:
        not_found_app = local_conf.pop('not_found_app')
    else:
        not_found_app = global_conf.get('not_found_app')
    if not_found_app:
        not_found_app = loader.get_app(not_found_app, global_conf=global_conf)
    urlmap = URLMap(not_found_app=not_found_app)
    for path, app_name in local_conf.items():
        # path = parse_path_expression(path)
        path = paste.urlmap.parse_path_expression(path)
        app = loader.get_app(app_name, global_conf=global_conf)
        urlmap[path] = app
    return urlmap


# novaでは、この部分を少しいじってる
class URLMap(paste.urlmap.URLMap):
    pass
