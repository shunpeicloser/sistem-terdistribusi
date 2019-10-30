import Pyro4
import base64
import json
import sys
import re

namainstance = sys.argv[1] or "fs1"

def get_fileserver_object(port=50001):
    uri = "PYRONAME:{}@localhost:{}" . format(namainstance, str(port))
    fserver = Pyro4.Proxy(uri)
    return fserver

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

if __name__=='__main__':
    proxy = get_fileserver_object()
    print(proxy)
    try:
        while True:
            response = ''
            print("Available command:\n\
                    SEND [filename]\t=> Send file \"filename\" to server\n\
                    DEL [filename]\t=> Delete file \"filename\" from server\n\
                    READ [filename]\t=> Read file \"filename\" from server\n\
                    EDIT [filename]\t=> Edit file \"filename\" from server\n\
                    LIST\t\t=> List files in server\n")

            cmd = input(">> ")
            cmd = parseCommand(cmd)
            print(cmd)
            if cmd[0] == 'SEND':
                response += proxy.create(cmd[1])
                response += proxy.update(cmd[1], content = open(cmd[1],'rb+').read())
            elif cmd[0] == 'EDIT':
                response += proxy.update(cmd[1], content = open(cmd[1],'rb+').read())
            elif cmd[0] == 'READ':
                response += proxy.read(cmd[1])
            elif cmd[0] == 'DEL':
                response += proxy.delete(cmd[1])
            elif cmd[0] == 'LIST':
                response += proxy.list()
            else:
                print(cmd[0]+cmd[1])
                continue

            print(response)
    except KeyboardInterrupt:
        sys.exit("Client Closed.")


    # f.create('slide1.pdf')
    # f.update('slide1.pdf', content = open('slide1.pdf','rb+').read() )

    # f.create('slide2.pptx')
    # f.update('slide2.pptx', content = open('slide2.pptx','rb+').read())

    # print(f.list())
    # d = f.read('slide1.pdf')
    # #kembalikan ke bentuk semula ke dalam file name slide1-kembali.pdf
    # open('slide1-kembali.pdf','w+b').write(base64.b64decode(d['data']))

    # k = f.read('slide2.pptx')
    # #kembalikan ke bentuk semula ke dalam file name slide2-kembali.pptx
    # open('slide2-kembali.pptx','w+b').write(base64.b64decode(k['data']))


