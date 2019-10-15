import Pyro4
import time
from threading import Thread
class Monitor:
    def get_service_proxy(self, ns='localhost:50001'):
        uri = "PYRONAME:service1@"+ns
        proxy = Pyro4.Proxy(uri)
        return proxy

    def ping(self, proxy):
        count = 0
        while True:
            if count >= 2:
                print('Ping fail')
                return
            try:
                proxy.ping()
                time.sleep(2)
                count = 0
            except:
                count += 1
                time.sleep(2)

    def monitor(self):
        proxy = self.get_service_proxy()
        tping = Thread(target=self.ping, args=(proxy,))
        tping.start()
        tping.join()
        return

mon = Monitor()
mon.monitor()