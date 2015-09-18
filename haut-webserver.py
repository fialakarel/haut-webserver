#!/usr/bin/python3

import os
import cherrypy
from mako.template import Template
from network import Network

class Webserver(object):

    def __init__(self):
        cherrypy.engine.subscribe('stop', self.stop)
        self.net = Network("127.0.0.1", 5557)
        # spusti se pri zapinani


    def stop(self):
        # spusti se pri vypinani
        pass

    def pomocna(self, do):
        # pomocna metoda
        pass

    @cherrypy.expose
    def index(self):
        # exposed metoda -- zavolali jsme /
        return base.render()

    @cherrypy.expose
    def set(self, value):
        # spustit ledky
        data = dict()
        data["key"] = "set"
        data["value"] = value

        self.net.send(data, "main.haut.local", 5556)

        return self.index()

    @cherrypy.expose
    def get(self, value):
        # spustit ledky
        data = dict()
        data["key"] = "get"
        data["value"] = value

        self.net.send(data, "main.haut.local", 5556)

        tmp = self.net.recv()

        # should be recv
        return tmp



if __name__ == '__main__':
    conf = {
         '/': {
             #'tools.sessions.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd()),
         },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './static'
         },
         '/css': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './static/css'
         },
         '/js': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './static/js'
         }
     }
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.socket_port = 80

    base = Template(filename='./static/base.html')

    cherrypy.quickstart(Webserver(), '/', conf)
