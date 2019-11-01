import os
import base64
from collections import defaultdict
class FileServer(object):
    peer = []

    def __init__(self):
        pass

    def report(self, client_id):
        print(str(client_id) + ' has been connected')

    def init_filestate(self):
        FileServer.filestate = defaultdict(lambda: '', FileServer.filestate)
        for x in os.listdir("{}".format(FileServer.basedir)):
            FileServer.filestate[x[FileServer.id.__len__()+1:]] = 'unlock'

    def get_filestate(self, filename):
        return FileServer.filestate[filename]

    def set_identifier(self, id):
        FileServer.id = id
        FileServer.basedir = id
        FileServer.init_filestate()

    def add_peer(self, peer_proxy):
        FileServer.peer.append(peer_proxy)
    
    def is_unlocked_peer(self, filename, peer_proxy):
        return (peer_proxy.get_filestate(filename) == 'unlock')

    def propagate(self, cmd, filename=None):
        flag = False
        for peer_proxy in FileServer:
            if not FileServer.is_unlocked_peer(filename, peer_proxy):
                flag = True
                break

        if flag:
            return self.create_return_message('9999','File still in use by another user')

        FileServer.filestate[filename] = 'lock'
        ret = None

        if cmd == 'create':
            for peer_proxy in FileServer:
                peer_proxy.create(filename)
            ret = self.create_return_message('100','OK')
        elif cmd == 'update':
            for peer_proxy in FileServer:
                peer_proxy.update(filename, content = open(str(FileServer.basedir)+'/'+filename,'r+b').read())
            ret = self.create_return_message('101','OK')
        elif cmd == 'delete':
            for peer_proxy in FileServer:
                peer_proxy.delete(filename)
            ret = self.create_return_message('101','OK')
        else:
            pass

        FileServer.filestate[filename] = 'unlock'
        return ret

    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def list(self):
        print("list ops")
        print("{}".format(FileServer.basedir))
        try:
            daftarfile = []
            prefix = "{}-".format(FileServer.id)
            for x in os.listdir("{}".format(FileServer.basedir)):
                print(x[0:FileServer.id.__len__()])
                if x[0:FileServer.id.__len__()+1] == prefix:
                    daftarfile.append(x[FileServer.id.__len__()+1:])
            return self.create_return_message('200',daftarfile)
        except:
            return self.create_return_message('500','Error')

    def create(self, name='filename000'):
        name='{}-{}' . format(FileServer.id, name)
        print("create ops {}" . format(name))
        try:
            if os.path.exists("{}/{}".format(FileServer.basedir, name)):
                return self.create_return_message('102', 'OK','File Exists')
            f = open("{}/{}".format(FileServer.basedir, name),'wb',buffering=0)
            f.close()
            return FileServer.propagate('create', name) #self.create_return_message('100','OK')
        except:
            return self.create_return_message('500','Error')
    def read(self,name='filename000'):
        name='{}-{}' . format(FileServer.id, name)
        print("read ops {}" . format(name))
        try:
            f = open("{}/{}".format(FileServer.basedir, name),'r+b')
            contents = f.read().decode()
            f.close()
            tmp = FileServer.propagate('read', name)
            if tmp['kode'] == '9999':
                return tmp
            return self.create_return_message('101','OK',contents)
        except:
            return self.create_return_message('500','Error')
            
    def update(self,name='filename000',content=''):
        print(content)
        name='{}-{}' . format(FileServer.id, name)
        print("update ops {}" . format(name))

        if (str(type(content))=="<class 'dict'>"):
            content = content['data']
        try:
            f = open("{}/{}".format(FileServer.basedir, name),'w+b')
            f.write( base64.b64decode( content ) )
            f.close()
            return FileServer.propagate('update', name) #self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

    def delete(self,name='filename000'):
        name='{}-{}' . format(FileServer.id, name)
        print("delete ops {}" . format(name))

        try:
            os.remove("{}/{}".format(FileServer.basedir, name))
            return FileServer.propagate('delete', name) #self.create_return_message('101','OK')
        except:
            return self.create_return_message('500','Error')
