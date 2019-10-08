from filemanager import  *
import Pyro4

def start_server(host='localhost', port=50001):
    #name server harus di start dulu dengan  pyro4-ns -n [host] -p [port]
    #gunakan URI untuk referensi name server yang akan digunakan
    #untuk mengecek service apa yang ada di ns, gunakan pyro4-nsc -n [host] -p [port] list
    daemon = Pyro4.Daemon(host=host)
    ns = Pyro4.locateNS(host, port)
    expose_server = Pyro4.expose(FileManager)
    uri = daemon.register(expose_server)
    print("URI FileManager : ", uri)
    ns.register("filemanager", uri)
    daemon.requestLoop()

if __name__ == '__main__':
    start_server('10.151.253.159', 8081)
