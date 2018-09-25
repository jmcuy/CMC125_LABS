import queue as q
import collections
import time
import sys
class Resource:
    def __init__(self,i):

        self.queue = q.Queue()
        self.available = True
        self.res_id = i
        self.time = 0

    def __repr__(self):
        return str(self.res_id) + " total time:" + str(self.time) + " "

    def printdis(self,s):
        t = time.time()
        print("%s  %s" % (t, s))

    def getTotalTime(self):
        return self.time

    def setTotalTime(self,t):
        self.time = t

    def setQueue(self,item):
        self.queue.put(item,block=True,timeout=item.getTime())

    def getQueue(self):
        l = []
        for i in range(self.queue.qsize()):
            l.append(self.queue.get(i))
        return l.copy()

    # def top(self):
    #     temp_Q = self.getQueue()
    #     return collections.deque(temp_Q).popleft()

    def getId(self):
        return self.res_id

    def setAvailability(self, t):
        self.available = t

    def getStatus(self):
        return self.available

    def __str__(self):
        return ("resource " + str(self.res_id))
