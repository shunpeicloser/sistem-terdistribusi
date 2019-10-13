from datetime import datetime

class Service2:
    id = 2
    def act(self):
        return "service " + str(self.id)

class Pinger2:
    id = 2
    status = True
    service_list = {}
    # base_time = datetime(2019, 10, 9)

    def __init__(self, id=2, services=None):
        if service_list == None:
            return "no services exist"
        
        self.id = id

        # add services
        for service in services:
            if service.id == self.id:
                continue
            t = datetime.utcnow()
            self.service_list[service.id] = [service, t]
        
        return "success"

    # send
    def recv_beat(self, src_id):
        if self.id == src_id:
            return
        
        while True:
            try:
                now = datetime.utcnow()
                if (now - self.service_list[src_id][1]).total_seconds > 6:
                    print('Server '+str(dest_id)+' fail. Deleting from service_list')
                    self.service_list.__delitem__(dest_id)
                    return
            except KeyboardInterrupt:
                return

    # recv
    @Pyro4.oneway
    def send_beat(self, dest_id):
        self.service_list[dest_id][1] = datetime.utcnow()