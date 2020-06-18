from guizero import App, Box, PushButton, TextBox, Text, CheckBox
# Lists (arrays), Queue, Stacks, Dictionary, Tuple

def insertText():
    global qText
    t = txtInput.value
    qText.insert(0,t)
    stackInput.height +=1
    stackInput.value = ""
    for each in qText:
        stackInput.value += each
    txtInput.value = ""
    queueInput.width +=len(t)
    queueInput.value =  queueInput.value + t + ", "

def deleteText():
    global qText
    qText.pop(0)
    stackInput.value = ""
    stackInput.height -=1
    for each in qText:
        stackInput.value += each
    q = queueInput.value
    stopQ = q.find(",")
    stopQ +=1
    newValues = q[stopQ:]
    queueInput.width -= stopQ
    queueInput.value = newValues
    print(q)

dsApp = App(title="Data Structures",width=650, height=800, layout='grid')
#Main Box
inputBox = Box(dsApp,layout='grid',grid=[0,0])
txtInput = TextBox(inputBox,text="",width=38, height=1 ,grid=[1,0])
txtInput.text_size = 15
PushButton(inputBox,insertText,text="Add Data",grid=[0,0])
PushButton(inputBox,deleteText,text="Remove Data",grid=[2,0])

#STACK Box
stackBox = Box(dsApp, layout='grid',grid=[0,2])
stackBox.bg = "limegreen"
Text(stackBox,text='Stack',grid=[0,0])
stackInput = TextBox(stackBox,text="",width=20, height=1 ,grid=[0,1], multiline=True)
#QUEUE Box
queueBox = Box(dsApp, layout='grid',grid=[0,3])
queueBox.bg = "cyan"
Text(queueBox,text='Queue',grid=[1,0])
Text(queueBox,text='Back',grid=[2,1])
queueInput = TextBox(queueBox,text="",width=20, height=1 ,grid=[1,1], multiline=False, enabled=False)
Text(queueBox,text='Front',grid=[0,1])

# Stores Queue data
qText = []
dsApp.display()