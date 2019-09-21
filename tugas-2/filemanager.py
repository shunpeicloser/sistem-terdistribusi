import random
import re
import os

class FileManager(object):
    def __init__(self):
        pass

    def parseCommand(self, cmd):
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

    def send(self, filename):
        return

    def delete(self, filename):
        return
    
    def read(self, filename):
        return
    
    def edit(self, filename):
        return
    
    def lists(self):
        ret = '=============\nList of Files:\n'
        files = os.listdir('./files')
        for i in files:
            ret = ret + '- ' + i + '\n'
        ret = ret + '=============\n'
        return ret

    def runCommand(self, command=''):
        command = self.parseCommand(command)
        if command == None:
            return
        if command[0] == 'Error':
            print(command[0]+': '+command[1])
            return
        if command[0] == 'SEND':
            return self.send(command[1])
        if command[0] == 'DEL':
            return self.delete(command[1])
        if command[0] == 'READ':
            return self.read(command[1])
        if command[0] == 'EDIT':
            return self.edit(command[1])
        if command[0] == 'LIST':
            return self.lists()
