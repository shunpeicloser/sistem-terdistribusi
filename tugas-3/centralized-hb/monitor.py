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
            prox.start_service()


mon = Monitor()
mon.monitor()