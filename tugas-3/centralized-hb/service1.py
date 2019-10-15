from datetime import datetime
import time
import Pyro4
import threading
class Service1:
    id = 1
    service_list = {}

    def get_id(self):
        return Service1.id

    def get_connected_service(self):
        ret = []
        for k in Service1.service_list.keys():
            ret.append([k, Service1.service_list[k][1], Service1.service_list[k][2]])
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

    # check beat, run as thread per connected service
    def recv_beat(self, src_id):
        if self.get_id() == src_id:
            return
        
        try:
            while True:
                self.service_list[src_id][2] = datetime.utcnow()
                if abs((self.service_list[src_id][2] - self.service_list[src_id][1]).total_seconds()) > 15:
                    print('Server '+str(src_id)+' fail. Deleting from service_list')
                    self.service_list.__delitem__(src_id)
                    return
                # print(self.service_list[src_id][1:], abs((self.service_list[src_id][2] - self.service_list[src_id][1]).total_seconds))
                time.sleep(5)
        except:
            print('ada error 1')
            return

    def get_service_proxy(self, ns='localhost:50001'):
        ret = []
        for i in range(2, 3):
            if i == self.get_id():
                continue
            uri = "PYRONAME:service"+str(i)+"@"+ns
            proxy = Pyro4.Proxy(uri)
            ret.append(proxy)
        return ret
 
    def act(self):
        return "service " + str(self.get_id())
    
    def watch(self):
        try:
            while True:
                print(self.get_connected_service())
                time.sleep(5)
        except:
            return
        

    @Pyro4.oneway
    def start_service(self):
        # tsend = []
        trecv = []
        w = threading.Thread(target=self.watch)
        self.add_services()
        for i in range(2, 3):
            # tsend.append(threading.Thread(target=self.send_beat, args=(i,)))
            trecv.append(threading.Thread(target=self.recv_beat, args=(i,)))
        for r in trecv:
            # s.start()
            r.start()
        w.start()
        for r in trecv:
            # s.join()
            r.join()
        w.join()
        return