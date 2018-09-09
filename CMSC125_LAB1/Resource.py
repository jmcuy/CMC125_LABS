import queue as q
# import threading
import time
import sys
class Resource:
    def __init__(self,i):

        self.queue = q.Queue()
        self.available = True
        self.res_id = i

    def __repr__(self):
        return str(self.res_id)

    def printdis(self,s):
        t = time.time()
        print("%s  %s" % (t, s))

    def setQueue(self,item):
        if not self.queue.full() or self.queue.empty():
            try:
                o = self.queue.put(item,block=True, timeout=item.getTime())

            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise

        # self.queue.put(item,block=True,timeout=item.getTime())

    def getQueue(self):
        l = []
        for i in range(self.queue.qsize()):
            l.append(self.queue.get(i))
        return l

    def getId(self):
        return self.res_id

    def setAvailability(self, t):
        self.available = t

    def getStatus(self):
        return self.available

    def __str__(self):
        return ("resource " + str(self.res_id))
