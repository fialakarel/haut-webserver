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
    def temp(self):
        # zjistime teplotu a vratime ji
        # ajax ji nahradi
        data = dict()
        data["key"] = "get"
        data["value"] = "dev.haut.local_28-000005e6d5be"
        
        self.net.send(data, "main.haut.local", 5556)
        temp = self.net.recv()
        
        # should be recv
        return temp
    
    @cherrypy.expose
    def off(self):
        # vypnout ledky
        data = dict()
        data["key"] = "set"
        data["value"] = "gpio-17-off"
        
        self.net.send(data, "main.haut.local", 5556)
        
        return self.index()
    
    @cherrypy.expose
    def on(self):
        # spustit ledky
        data = dict()
        data["key"] = "set"
        data["value"] = "gpio-17-on"
        
        self.net.send(data, "main.haut.local", 5556)
        
        return self.index()
    
    @cherrypy.expose
    def index(self):
        # exposed metoda -- zavolali jsme /
        obsah = '<div><a href="/on">ON</a><br><a href="/off">OFF</a><br><a href="/temp">temp</a><br>'
        obsah = obsah + 'temp: <div id="teplota">00</div><br></div>'

        return base.render(content=obsah)



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
    cherrypy.server.socket_port = 8888
 
    base = Template(filename='./static/base.html')
   
    cherrypy.quickstart(Webserver(), '/', conf)
