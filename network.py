#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.2.0

"""
Pouziti:

from network import Network

chceme jen posilat:
    client = Network()

chceme posilat i prijimat (sednout si na port):
    server = Network("0.0.0.0", 8888)

vstupy a vystupy jsou pole (prevod z/do JSONu je automaticky)
"""

import socket
import json

# asi staci kdyz MTU pro 1 paket je max 1500
BUFF_SIZE = 1024

class Network(object):

    def __init__(self, ip = "", port = 0):

        self.server = False;
        self.addr = False;
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if ip != "":
            self.sock.bind((ip, port)) # jen server
            self.server = True;
        pass

    def send(self, message, ip, port):
        try:
            self.sock.sendto(bytes(json.dumps(message), "utf-8"), (ip , port))
        except ValueError:
            print("ValueError happen -- continuing")
            pass        # chyba JSONu
        # TODO -- doplnit osetreni chyb socketu?

    def recv(self):
        if self.server:
            data, self.addr = self.sock.recvfrom(BUFF_SIZE)
            try:
                return json.loads(data.decode("utf-8"))
            except ValueError:
                return False    # neprisel nam JSON (vracime False)
        else:
            return False

    def recv_from(self):
        # return last ip
        return self.addr
