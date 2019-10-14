import Pyro4

class Monitor:
    def get_service_proxy(self, ns='localhost:50001'):
        ret = []
        for i in range(1, 4):
            if i == 2:
                continue
            uri = "PYRONAME:service"+str(i)+"@"+ns
            proxy = Pyro4.Proxy(uri)
            ret.append(proxy)
        return ret

    def monitor(self):
        try:
            cmd = input('start services? (y/n)')
            if cmd == 'n':
                return
            proxs = self.get_service_proxy()
            for prox in proxs:
                prox.start_service()
            return
        except KeyboardInterrupt:
            return

mon = Monitor()
mon.monitor()