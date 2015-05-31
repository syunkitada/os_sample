#!/usr/bin/env python
# coding: utf-8

"""
PasteDeployは、iniファイルでWSGIのアプリケーションやサーバーの設定や構成を管理するものです。
で、そのiniファイルを paster serveに渡せば WSGIアプリケーションが実行されるわけですね。
loadapp関数により、confファイルからWSGIアプリケーションをロードする。
"""

import os
import sys

from paste.deploy import loadapp
import eventlet
import eventlet.wsgi


if __name__ == '__main__':
    argv = sys.argv
    app_name = None
    if len(argv) > 1:
        app_name = argv[1]

    conf_name = 'api-paste.ini'
    conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             conf_name)
    wsgi_app = loadapp('config:{0}'.format(conf_path), name=app_name)

    server_sock = eventlet.listen(('localhost', 8080))
    eventlet.wsgi.server(server_sock, wsgi_app)
