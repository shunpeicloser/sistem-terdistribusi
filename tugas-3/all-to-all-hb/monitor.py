import Pyro4
import time
from datetime import datetime
class Monitor:
    def get_service_proxy(self, ns='localhost:50001'):
        ret = []
        for i in range(1, 3):
            uri = "PYRONAME:service"+str(i)+"@"+ns
            proxy = Pyro4.Proxy(uri)
            ret.append(proxy)
        return ret

    def monitor(self):
        cmd = input('start services? (y/n): ')
        if cmd != 'y':
            return
        proxs = self.get_service_proxy()
        for prox in proxs:
            print(prox.get_id())
            prox.start_service()

        try:
            while True:
                print('###')
                for prox in proxs:
                    print(prox.get_id(), prox.get_connected_service())
                time.sleep(6)
                

        except KeyboardInterrupt:
            return

mon = Monitor()
mon.monitor()