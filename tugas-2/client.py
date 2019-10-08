import Pyro4
import sys
import re

def createProxy(ns='localhost:50001'):
    uri = "PYRONAME:filemanager@"+ns
    proxy = Pyro4.Proxy(uri)
    return proxy

def parseCommand(cmd):
    if cmd == None or cmd == '':
        return None
    parse = re.sub(r'\n', '', cmd)
    parse = parse.split(' ')
    if parse[0] == 'LIST':
        return ['LIST', None]
    elif parse.__len__() != 2:
        return ['Error', 'Filename doesn\'t exist / incorrect parameter']
    elif parse[0] == 'SEND' or parse[0] == 'DEL' or parse[0] == 'READ' or parse[0] == 'EDIT':
        return parse
    else:
        return ['Error', 'Incorrect command']

def command(proxy=None):
    if proxy == None:
        sys.exit('Proxy not created!')
    try:
        while True:
            print("Available command:\n\
                    SEND [filename]\t=> Send file \"filename\" to server\n\
                    DEL [filename]\t=> Delete file \"filename\" from server\n\
                    READ [filename]\t=> Read file \"filename\" from server\n\
                    EDIT [filename]\t=> Edit file \"filename\" from server\n\
                    LIST\t\t=> List files in server\n")

            cmd = input(">> ")
            cmd = parseCommand(cmd)
            if cmd[0] == 'SEND' or cmd[0] == 'EDIT':
                f = open(cmd[1])
                buf = f.read()
                f.close()
                response = proxy.runCommand(cmd, buf)
            elif cmd[0] != 'ERROR':
                response = proxy.runCommand(cmd)
            else:
                print(cmd[0]+cmd[1])
                continue

            print(response)
    except KeyboardInterrupt:
        print('\nClient closed.')

if __name__=='__main__':
    command(createProxy('10.151.62.66:6969'))