import random
import re
import os

class FileManager(object):
    def __init__(self):
        pass

    def send(self, filename, data):
        if os.path.isfile('./files/'+filename):
            return filename+' has been exist!'
        try:
            f = open('./files/'+filename, mode='w')
            if data != None:
                f.write(data)
            return filename+' has been send'
        except IOError:
            return 'Fail to send '+filename

    def delete(self, filename):
        try:
            os.remove('./files/'+filename)
            return filename+' has been deleted'
        except OSError:
            return filename+' not exist'
    
    def read(self, filename):
        ret = ''
        f = open('./files/'+filename)
        for i in f:
            ret += i
        return ret
    
    def edit(self, filename, data):
        ret = ''
        if not os.path.isfile('./files/'+filename):
            ret += filename+' does not exist. Creating file'
        try:
            f = open('./files/'+filename, mode='w')
            if data != None:
                f.write(data)
            if ret != '':
                return ret
            else:
                return filename+' has been editted'
        except IOError:
            return 'Fail to send '+filename
    
    def lists(self):
        ret = '=============\nList of Files:\n'
        files = os.listdir('./files')
        for i in files:
            ret = ret + '- ' + i + '\n'
        ret = ret + '=============\n'
        return ret

    def runCommand(self, command='', data=None):
        # command = self.parseCommand(command)
        if command == None:
            return
        if command[0] == 'Error':
            print(command[0]+': '+command[1])
            return
        if command[0] == 'SEND':
            return self.send(command[1], data)
        if command[0] == 'DEL':
            return self.delete(command[1])
        if command[0] == 'READ':
            return self.read(command[1])
        if command[0] == 'EDIT':
            return self.edit(command[1], data)
        if command[0] == 'LIST':
            return self.lists()
