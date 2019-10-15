from service1 import  *
from service2 import  *
from service3 import  *
import Pyro4

def start_server(host='localhost', port=50001):
    #name server harus di start dulu dengan  pyro4-ns -n [host] -p [port]
    #gunakan URI untuk referensi name server yang akan digunakan
    #untuk mengecek service apa yang ada di ns, gunakan pyro4-nsc -n [host] -p [port] list
    daemon = Pyro4.Daemon(host=host)
    ns = Pyro4.locateNS(host, port)

    service1 = Pyro4.expose(Service1)
    service2 = Pyro4.expose(Service2)
    service3 = Pyro4.expose(Service3)
    
    uri_s1 = daemon.register(service1)
    uri_s2 = daemon.register(service2)
    uri_s3 = daemon.register(service3)

    # print("URI FileManager : ", uri)
    ns.register("service1", uri_s1)
    ns.register("service2", uri_s2)
    ns.register("service3", uri_s3)
    
    daemon.requestLoop()

if __name__ == '__main__':
    start_server()
