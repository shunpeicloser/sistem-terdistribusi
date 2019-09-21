import Pyro4
import sys
import socket

def createProxy(ns='localhost:50001'):
    uri = "PYRONAME:filemanager@"+ns
    proxy = Pyro4.Proxy(uri)
    return proxy

def command(proxy=None):
    if proxy == None:
        sys.exit('Proxy not created!')
    try:
        print("Available command:\n\
                SEND [filename]\t=> Send file \"filename\" to server\n\
                DEL [filename]\t=> Delete file \"filename\" from server\n\
                READ [filename]\t=> Read file \"filename\" from server\n\
                EDIT [filename]\t=> Edit file \"filename\" from server\n\
                LIST\t\t=> List files in server\n")

        cmd = input(">> ")
        response = proxy.runCommand(cmd)
        print(response)
    except KeyboardInterrupt:
        print('\nClient closed.')

if __name__=='__main__':
    command(createProxy())