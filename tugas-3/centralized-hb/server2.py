from service2 import  *
import Pyro4

def start_server(host='localhost', port=50001):
    #name server harus di start dulu dengan  pyro4-ns -n [host] -p [port]
    #gunakan URI untuk referensi name server yang akan digunakan
    #untuk mengecek service apa yang ada di ns, gunakan pyro4-nsc -n [host] -p [port] list
    daemon = Pyro4.Daemon(host=host)
    ns = Pyro4.locateNS(host, port)

    service2 = Pyro4.expose(Service2)
    uri_s2 = daemon.register(service2)
    ns.register("service2", uri_s2)
    
    daemon.requestLoop()

if __name__ == '__main__':
    start_server()
