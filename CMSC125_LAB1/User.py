from Resource import Resource
class User:
    def __init__(self,i):
        self.resource = []
        self.user_id = i

    def __repr__(self):
        return str(self.user_id)

    def setRes(self,r):
        self.resource.append(r)

    def getRes(self):
        return self.resource

    def getId(self):
        return self.user_id

    # def __str__(self):
    #     return ("user " + str(self.user_id)  + " resources: " + str(self.resource))

    def __str__(self):
        return ("user " + str(self.user_id))