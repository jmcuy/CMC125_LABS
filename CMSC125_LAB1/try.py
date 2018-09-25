import random
import queue as q
from User import User
from Resource import Resource
from Item import Item
import time
import sys
from appJar import gui
from copy import deepcopy
#===================SET UP WINDOW=====================
app = gui("","900x500")
app.startFrame("LEFT", row=0, column=0)
app.setBg("#031e03")
app.setSticky("NEW")
app.setStretch("COLUMN")

app.addLabel("L1", "CMSC125 LAB1",colspan=2)
app.setLabelBg("L1","#00a800")

#==================Generate Random Resources============
prev_resources = []
prev_user = []
res_to_users = []
def rand(n):
    return random.randint(1, n)

num_resources = rand(10)
num_user = rand(10)
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
# counter = 5
# def countdown(n):
#     global counter
#     if counter > 0:
#         app.setLabel("counter", str(counter))
#         counter -= 1

prev_list = q.Queue()
new = []
somelist = []

def assign_resUser():
    userList = prev_user.copy()
    resList = prev_resources.copy()
    temp_res = resList.copy()
    for user in range(len(userList)):
        random.shuffle(temp_res)
        reserves = rand(len(resList))
        for res in range(reserves):
            t = rand(5)
            item = Item(temp_res[res], t, userList[user])
            temp_res[res].setQueue(item)
            userList[user].setRes(temp_res[res]) #put str
    #======prev_resources is where all resources are stored===========
    all_queues = []
    name_resource = []

    for res in prev_resources:
        # print("Resource: " + str(res.getId()))
        if res.getId() not in name_resource:
            name_resource.append(str(res.getId()))
        try:
            all_queues.append(res.getQueue().copy())
        except Exception as e:
            print(str(e))
    # all_queues = [x for x in all_queues if x != []]
    print("Length: " + str(len(all_queues)))
    return all_queues


def next():
    original_list = assign_resUser().copy()
    temp_q = []
    for i in original_list:
        temp_q.append(i.copy())

    print("ORIGINAL LIST: " + str(original_list))


   #======================LOGIC AREA========================
    queue = [[] for x in range(len(temp_q))]
    print("Resource Lsit:  " + str(prev_resources))
    print("User Lsit:  " + str(prev_user))
    while temp_q:
        delete_list = []
        for qi in range(len(temp_q)):
            temp = temp_q[qi]
            if temp:
                res = temp[0].getRes()
                add_queue = False
                min_time = temp[0].getUser().getTotalTime()
                for i in temp:
                    user = i.getUser()
                    min_time = user.getTotalTime() if min_time > user.getTotalTime() else min_time
                    if res.getTotalTime() >= user.getTotalTime():
                        i.setWaitingTime(res.getTotalTime())
                        res.setTotalTime(i.getTime() + res.getTotalTime())
                        user.setTotalTime(i.getWaitingTime() + i.getTime())
                        queue[res.getId() - 1].append(i)
                        temp.remove(i)
                        add_queue = True
                        break
                if not add_queue:
                    res.setTotalTime(min_time)
            else:
                delete_list.append(temp)
        for n in delete_list:
            temp_q.remove(n)

    print("Resource List:  " + str(prev_resources))
    print("User List:  " + str(prev_user))
    print("SCHEDULE LIST: ")
    for t in queue:
        print(str(t))
    olist = original_list.copy()
    return queue

def countdown():
    queue = next()
    print("sdasda" + str(olist))
    #================DISPLAY GENERATED RESOURCES==============
    app.addLabel("L2","Generated Resources  " + "( " + str(num_resources) + " )",colspan=2)
    app.setLabelBg("L2","light blue")

    app.setSticky("NEW")
    app.setStretch("COLUMN")
    # ==============countdown ===============
    cond = [[] for l in range(len(queue))]
    toPrint = []
    data = ""
    # app.startScrollPane("Pane",colspan=2)
    # app.setScrollPaneHeight("Pane",470)
    # app.setScrollPaneBg("Pane", "black")
    # app.setPadX(10)
    # app.setPadY(20)

    col = 0
    row = 2
    count = 0
    x=0


    # for res in range(len(original_list)):
    #     if original_list[res] == []:
    #         app.addScrolledTextArea("res" + str(res+1), text=None, row=row, column=col, colspan=1)
    #         app.setTextArea("res" + str(res +1), "Resource  " + str(res+1) +"\n")
    #         app.setTextArea("res" + str(res+1), "FREE")
    #     else:
    #         item =original_list[res][0]
    #         if count % 4 == 0:
    #             row += 1
    #             col = 0
    #         else:
    #             col += 1
    #         app.addScrolledTextArea("res" + str(item.getRes().getId()), text=None, row=row, column=col, colspan=1)
    #         app.setTextArea("res" + str(item.getRes().getId()), "Resource  " + str(item.getRes().getId()))
    #
    #
    #     count += 1
    #     x += 1


    # app.setAllTextAreaWidths(20)
    # app.setAllTextAreaHeights(5)
    # while queue != cond:
    #     for qi in range(len(queue)):
    #         curr = queue[qi].copy()
    #         toPrint.append(str(curr))
    #         print("CURRENT LIST:  " + str(curr))
    #
    #         data += str(curr) + "\n"
    #         while curr:
    #
    #             # app.setPollTime(10)
    #             app.clearTextArea("res"+ str(curr[0].getRes().getId()))
    #             app.setTextArea("res" + str(curr[0].getRes().getId()), "Resource  " + str(curr[0].getRes().getId()) + "\n")
    #             app.setTextArea("res" + str(curr[0].getRes().getId()), "Total Time: " + str(curr[0].getRes().getTotalTime()) + "\n")
    #             for item in curr:
    #                 if item.getWaitingTime() > 0:
    #                     item.setWaitingTime(item.getWaitingTime() - 1)
    #
    #                 else:
    #                     print(curr[0].getRes().getTotalTime())
    #                     item.setTime(item.getTime() - 1)
    #
    #                 if item.getTime() == 0:
    #                     data +="REMOVED..... " + str(item) + "\n"
    #                     # print("CURRENT LIST:  " + str(curr))
    #                     print("REMOVED..." + str(item))
    #                     curr.remove(item)
    #                     queue[item.getRes().getId() - 1].remove(item)
    #                     # print(queue2)
    #
    #             break
    #     data += "====================\n\n\n"
    # app.stopScrollPane()
app.stopFrame()
#main
add_res_vector(num_resources)
add_user_vector(num_user)
# assign_resUser()
countdown()
# assign_resUser(prev_user,prev_resources)
# app.registerEvent(assign_resUser())
app.go()
