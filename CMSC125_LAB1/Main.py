from appJar import gui
app = gui("","500x500")


# app.setLabelBg("CENTER title", "red")
app.setSticky("NEW")
app.setExpand("both")
app.addLabel("L1", "CMSC125 LAB1",0,1)
app.setLabelBg("L1","red")
app.addMessage("mess", "")
app.go()