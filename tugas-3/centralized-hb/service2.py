from datetime import datetime
import time
import Pyro4
import threading
class Service2:
    id = 2
    service_list = {}

    def get_id(self):
        return Service2.id

    def get_connected_service(self):
        ret = []
        for k in Service2.service_list.keys():
            ret.append([k, Service2.service_list[k][1], Service2.service_list[k][2]])
        return ret

    def add_services(self):
        services = self.get_service_proxy()
        # print(self.get_id())
        # for service in services:
        #     print('connect to: ' + str(service.get_id()))
        if services == None:
            return "no services exist"

        # add services
        for service in services:
            t = datetime.utcnow()
            self.service_list[service.get_id()] = [service, t, t]
    
        return "services has been added"

    # send
    def send_beat(self, dest_id):
        if dest_id == self.get_id():
            return

        while True:
            try:
                self.service_list[dest_id][0].act()
                self.service_list[dest_id][1] = datetime.utcnow()
                time.sleep(5)
            except:
                return

    def get_service_proxy(self, ns='localhost:50001'):
        ret = []
        uri = "PYRONAME:service1@"+ns
        proxy = Pyro4.Proxy(uri)
        ret.append(proxy)
        return ret
 
    def act(self):
        return "service " + str(self.get_id())
    
    def watch(self):
        try:
            while True:
                print(self.get_connected_service())
                time.sleep(15)
        except KeyboardInterrupt:
            return
        

    @Pyro4.oneway
    def start_service(self):
        # trecv = []
        w = threading.Thread(target=self.watch)
        self.add_services()
        tsend = threading.Thread(target=self.send_beat, args=(1,))
        tsend.start()
        w.start()
        tsend.join()
        w.join()
        return