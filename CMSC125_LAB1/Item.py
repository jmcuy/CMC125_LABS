class Item:
    def __init__(self,r,t,u):
        self.resource = r
        self.time = t
        self.user = u

    # def __repr__(self):
    #     return str(self.resource) + " Time: " +  str(self.time) + " " + str(self.user)+"\n"

    def __repr__(self):
        return  str(self.user) + " Time: " +  str(self.time)

    def getId(self):
        return self.resource

    def setId(self,r):
        self.resource.append(r)

    def getTime(self):
        return self.time

    def setTime(self,t):
        self.time = t

    def getUser(self):
        return self.user

    def setUser(self,u):
        self.user = u