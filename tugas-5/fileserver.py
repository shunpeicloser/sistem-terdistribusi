import os
import base64

class FileServer(object):
    def __init__(self):
        pass

    def report(self, client_id):
        print(str(client_id) + ' has been connected')

    def set_identifier(self, id):
        FileServer.id = id
        FileServer.basedir = id

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
            return self.create_return_message('100','OK')
        except:
            return self.create_return_message('500','Error')
    def read(self,name='filename000'):
        name='{}-{}' . format(FileServer.id, name)
        print("read ops {}" . format(name))
        try:
            f = open("{}/{}".format(FileServer.basedir, name),'r+b')
            contents = f.read().decode()
            f.close()
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
            return self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

    def delete(self,name='filename000'):
        name='{}-{}' . format(FileServer.id, name)
        print("delete ops {}" . format(name))

        try:
            os.remove("{}/{}".format(FileServer.basedir, name))
            return self.create_return_message('101','OK')
        except:
            return self.create_return_message('500','Error')
