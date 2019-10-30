from fileserver import  *
import Pyro4
import sys

namainstance = sys.argv[1]

def start_with_ns(hostname="localhost", port=50001):
    #name server harus di start dulu dengan  pyro4-ns -n localhost -p 7777
    #gunakan URI untuk referensi name server yang akan digunakan
    #untuk mengetahui instance apa saja yang aktif gunakan pyro4-nsc -n localhost -p 7777 list

    daemon = Pyro4.Daemon(host=hostname)
    ns = Pyro4.locateNS(hostname,port)
    x_FileServer = Pyro4.expose(FileServer)
    uri_fileserver = daemon.register(x_FileServer)
    ns.register("{}" . format(namainstance), uri_fileserver)
    Pyro4.Proxy("PYRONAME:{}@localhost:{}" . format(namainstance, str(port))).set_identifier(namainstance)
    print("PYRONAME:{}@localhost:{}" . format(namainstance, str(port)))
    daemon.requestLoop()


if __name__ == '__main__':
    start_with_ns()
