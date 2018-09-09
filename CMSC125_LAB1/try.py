import random
from multiprocessing import Process

from User import User
from Resource import Resource
from Item import Item
import time, sys


prev_resources = []
prev_user = []
res_to_users = []
def rand(n):
    return random.randint(1, n)

num_resources = rand(5)
num_user = rand(5)
# print("Resources:  "+ str(num_resources))
# print("Users:  " + str(num_user))


def add_res_vector(n):
    for i in range(1, n +1):
        new_res = Resource(i)
        prev_resources.append(new_res)
    print("\n")


def add_user_vector(n):
    for i in range(1,n + 1):
        new_user = User(i)
        prev_user.append(new_user)

def countdown(n):
    for i in range(n, 0, -1):
        sys.stdout.write('\r' + str(i) + ' ')
        sys.stdout.flush()
        time.sleep(1)
        n -= 1
    if n ==0:
        sys.stdout.write('\rDone')


def assign_resUser(userList, resList):
    temp_res = resList.copy()
    for user in range(len(userList)):
        random.shuffle(temp_res)
        reserves = rand(len(resList))
        for res in range(reserves):
            item = Item(temp_res[res], rand(10), userList[user])
            temp_res[res].setQueue(item)
            userList[user].setRes(temp_res[res]) #put str



    for res in prev_resources:
        # print("Resource: " + str(res.getId()))
        for item in res.getQueue():
            current = item
            # print(current)
            if __name__ == '__main__':
                p1 = Process(target=countdown,args=(item.getTime(),))
                p1.start()
                p1.join()




    # index = 0
    # while(index < len(res_to_users)):
    #     for res in res_to_users[index].getRes():
    #         print(str(res_to_users[index]) + str(res))
    #     index += 1








#main
add_res_vector(num_resources)
add_user_vector(num_user)
assign_resUser(prev_user,prev_resources)
