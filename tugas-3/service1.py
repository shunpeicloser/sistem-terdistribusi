from datetime import datetime
import time
import _thread
import Pyro4

class Service1:
    # @Pyro4.expose
    # id = 1

    # @Pyro4.expose
    service_list = {}

    def get_id(self):
        return 1

    def add_services(self):
        services = self.get_service_proxy()
        if services == None:
            return "no services exist"

        # add services
        for service in services:
            if service.get_id() == self.get_id():
                continue
            t = datetime.utcnow()
            self.service_list[service.id] = [service, t, t]
    
        return "services has been added"

    # check beat, run as thread per connected service
    @Pyro4.oneway
    def recv_beat(self, src_id):
        if self.get_id() == src_id:
            return
        
        while True:
            try:
                now = datetime.utcnow()
                self.service_list[src_id][2] = now
                if abs((now - self.service_list[src_id][1]).total_seconds) > 6:
                    print('Server '+str(src_id)+' fail. Deleting from service_list')
                    self.service_list.__delitem__(src_id)
                    return
                time.sleep(2)
            except KeyboardInterrupt:
                return

    # send
    @Pyro4.oneway
    def send_beat(self, dest_id):
        if dest_id == self.get_id():
            return

        while True:
            try:
                self.service_list[dest_id][1] = datetime.utcnow()
                time.sleep(2)
            except KeyboardInterrupt:
                return

    def get_service_proxy(self, ns='localhost:50001'):
        ret = []
        for i in range(1, 4):
            if i == self.get_id():
                continue
            if i == 2:
                continue
            uri = "PYRONAME:service"+str(i)+"@"+ns
            proxy = Pyro4.Proxy(uri)
            ret.append(proxy)
        return ret
 
    def act(self):
        return "service " + str(self.get_id())
    
    def start_service(self):
        self.add_services()
        for i in range(1, 4):
            if i == 2:
                continue
            self.send_beat(i)
            self.recv_beat(i)
        return