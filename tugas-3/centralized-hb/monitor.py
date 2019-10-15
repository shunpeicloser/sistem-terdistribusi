import Pyro4
import time
from datetime import datetime
class Monitor:
    def get_service_proxy(self, ns='localhost:50001'):
        ret = []
        for i in range(1, 4):
            uri = "PYRONAME:service"+str(i)+"@"+ns
            proxy = Pyro4.Proxy(uri)
            ret.append(proxy)
        return ret

    def monitor(self):
        d1 = datetime.utcnow()
        time.sleep(2)
        d2 = datetime.utcnow()
        print(abs((d1 - d2).total_seconds()) < 5)
        cmd = input('start services? (y/n)')
        if cmd == 'n':
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