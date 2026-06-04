import math

# Graphics
Rect(75,20,250,365,fill=None,border="black",borderWidth=4)
for i in range(3):
    Rect(85,30+35*i,230,30,fill=rgb(210,210,210))
Rect(85,140,230,30,fill=rgb(180,180,180))

# Buttons
buttons = [[0 for _ in range(5)] for _ in range(5)]
labels = [['C',' ',' ',' ',' '],
          ['1','2','3','+',' '],
          ['4','5','6','-',' '],
          ['7','8','9','*',' '],
          ['0','.',' ','/',' ']]
for row in range(5):
    for col in range(5):
        buttons[row][col] = Rect(100+col*40,180+row*40,35,35,fill="lightgrey")
        labels[row][col] = Label(labels[row][col],117.5+col*40,192.5+row*40,size=18)

clearAll = buttons[0][2]
clearAll.width = 75
# clearAll.fill = "yellow"
buttons[0][3].fill = None
labels[0][1] = Label("AC",217,193,size=18)

enter = buttons[2][4]
enter.height = 115
buttons[3][4].fill = None
buttons[4][4].fill = None
labels[2][4] = Group(Label("E",278,282,size=18),
                     Label("n",278,297,size=18),
                     Label("t",278,312,size=18),
                     Label("e",278,327,size=18),
                     Label("r",278,342,size=18))

swap = buttons[0][4]
swap.height = 75
buttons[1][4].fill = None
labels[2][4] = Group(Label("S",278,191,size=18),
                     Label("w",278,206,size=18),
                     Label("a",278,220,size=18),
                     Label("p",278,234,size=18))

back = buttons[0][1]
labels[0][1] = Line(150,193,170,193,arrowStart=True)

clear = buttons[0][0]
plus = buttons[0][0]
minus = buttons[0][0]
times = buttons[0][0]
divide = buttons[0][0]
decimal = buttons[0][0]

digits = [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    digits[i] = buttons[1+math.floor(i/3)][i%3]

# Stack
stack = [0]
isDecimal = False
stackLabels = []
stackLabels.append(Label("0",303,155,size=18))
for i in range(3):
    stackLabels.append(Label("0",303,115-i*35,size=18))

def getNum(index):
    if (len(stack) > index):
        return stack[index]
    else:
        pass # TODO: error message
        
def pop():
    if (len(stack) > 0):
        return stack.pop()
    else:
        pass # TODO: error message
        
def enter():
    stack.insert(0, 0)
    
def swap():
    if (len(stack) > 1):
        temp = stack[0]
        stack[0] = stack[1]
        stack[1] = temp
    else:
        pass # TODO: error message

def setNum(num):
    if (len(stack) > 0):
        stack[0] = num
    else:
        stack.push(num)
        
def clear():
    if (len(stack) > 0):
        setNum(0)
    else:
        pass # TODO: error message
