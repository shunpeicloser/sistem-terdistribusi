import os
import base64

class FileServer(object):
    def __init__(self):
        pass

    def set_identifier(self, id):
        self.id = id
        self.basedir = id

    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def list(self):
        print("list ops")
        try:
            daftarfile = []
            prefix = "{}-".format(self.id)
            for x in os.listdir("./{}".format(self.basedir)):
                if x[0:self.id.__len__()] == prefix:
                    daftarfile.append(x[self.id.__len__():])
            return self.create_return_message('200',daftarfile)
        except:
            return self.create_return_message('500','Error')

    def create(self, name='filename000'):
        nama='{}-{}' . format(self.id, name)
        print("create ops {}" . format(nama))
        try:
            if os.path.exists("./{}/{}".format(self.basedir, name)):
                return self.create_return_message('102', 'OK','File Exists')
            f = open("./{}/{}".format(self.basedir, name),'wb',buffering=0)
            f.close()
            return self.create_return_message('100','OK')
        except:
            return self.create_return_message('500','Error')
    def read(self,name='filename000'):
        nama='{}-{}' . format(self.id, name)
        print("read ops {}" . format(nama))
        try:
            f = open("./{}/{}".format(self.basedir, name),'r+b')
            contents = f.read().decode()
            f.close()
            return self.create_return_message('101','OK',contents)
        except:
            return self.create_return_message('500','Error')
            
    def update(self,name='filename000',content=''):
        nama='{}-{}' . format(self.id, name)
        print("update ops {}" . format(nama))

        if (str(type(content))=="<class 'dict'>"):
            content = content['data']
        try:
            f = open("./{}/{}".format(self.basedir, name),'w+b')
            f.write(content.encode())
            f.close()
            return self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

    def delete(self,name='filename000'):
        nama='{}-{}' . format(self.id, name)
        print("delete ops {}" . format(nama))

        try:
            os.remove("./{}/{}".format(self.basedir, name))
            return self.create_return_message('101','OK')
        except:
            return self.create_return_message('500','Error')
