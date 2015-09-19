#!/usr/bin/python3

import os
import cherrypy
from mako.template import Template
from network import Network
from config import *

class Webserver(object):

    def __init__(self):
        cherrypy.engine.subscribe('stop', self.stop)
        self.net = Network(WEBSERVER_IP, WEBSERVER_PORT)
        # spusti se pri zapinani


    def stop(self):
        # spusti se pri vypinani
        pass

    @cherrypy.expose
    def index(self):
        # exposed metoda -- zavolali jsme /
        return base.render()

    def doit(self, action, value):
        # spustit ledky
        data = dict()
        data["key"] = action
        data["value"] = value
        self.net.send(data, SERVER_IP, SERVER_PORT)

    @cherrypy.expose
    def set(self, value):
        self.doit("set", value)
        return self.index()

    @cherrypy.expose
    def get(self, value):
        self.doit("get", value)
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
    cherrypy.server.socket_host = "0.0.0.0"
    cherrypy.server.socket_port = 80

    base = Template(filename='./static/base.html')

    cherrypy.quickstart(Webserver(), '/', conf)
