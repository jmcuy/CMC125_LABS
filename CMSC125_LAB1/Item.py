class Item:
    def __init__(self,r,t,u):
        self.resource = r
        self.time = t
        self.user = u
        self.wait_time = 0

    # def __repr__(self):
    #     return str(self.resource) + " Time: " +  str(self.time) + " " + str(self.user)+"\n"

    def __repr__(self):
        # return  str(self.resource) + " " + str(self.user) + " Time: " +  str(self.time) + " HOLD:  " +  str(self.wait_time)
        return str(self.user) + " Time: " +  str(self.time) + " WTime: " + str(self.wait_time)

    def getRes(self):
        return self.resource

    def setRes(self,r):
        self.resource.append(r)

    def setWaitingTime(self,w):
        self.wait_time = w

    def getWaitingTime(self):
        return self.wait_time

    def getTime(self):
        return self.time

    def setTime(self,t):
        self.time = t

    def getUser(self):
        return self.user

    def setUser(self,u):
        self.user = u

    def __eq__(self, other):
        return self.user == other