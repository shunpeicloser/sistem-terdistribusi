from datetime import datetime
import time
import Pyro4
import threading

class Service1:
    def ping(self):
        return 'ACK'