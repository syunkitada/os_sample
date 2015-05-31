#!/usr/bin/env python
# coding: utf-8

"""
PasteDeployは、iniファイルでWSGIアプリケーションやミドルウェア、サーバーの設定や構成を管理するものです。
で、そのiniファイルを paster serveに渡せば WSGIアプリケーションが実行されるわけですね。
"""

import os
import sys

from paste.deploy import loadapp
import eventlet
import eventlet.wsgi


if __name__ == '__main__':
    argv = sys.argv
    app_name = 'helloapi'
    if len(argv) > 0:
        app_name = argv[0]

    conf_name = 'api-paste.ini'
    conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             conf_name)
    wsgi_app = loadapp('config:{0}'.format(conf_path), name='helloapi')

    server_sock = eventlet.listen(('localhost', 8080))
    eventlet.wsgi.server(server_sock, wsgi_app)
