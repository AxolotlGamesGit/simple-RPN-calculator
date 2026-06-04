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
          ['.','0',' ','/','e']]
keys =   [['c','C','backspace','s','p'],
          ['1','2','3',        '+',' '],
          ['4','5','6',        '-','enter'],
          ['7','8','9',        '*',' '],
          ['.','0','enter',    '/',' ']]
for row in range(5):
    for col in range(5):
        buttons[row][col] = Rect(100+col*40,180+row*40,35,35,fill="lightgrey")
        labels[row][col] = Label(labels[row][col],117.5+col*40,197.5+row*40,size=18)

# Custom labels
labels[0][1] = Label("AC",158,198,size=14)
labels[0][2] = Line(190,198,210,198,arrowStart=True)
labels[0][3] = Label("swap",238,198,size=13)
labels[0][4] = Label("pop",278,198,size=13)
labels[1][4] = Label("sqrt",278,238,size=13)
labels[2][4] = Label("log",278,278,size=13)
labels[3][4] = Group(Line(270,310,286,310),
                     Line(274,310,274,326),
                     Line(282,310,282,326))
labels[4][2] = Label("enter",198,358,size=12)

# Stack
stack = []
current = None
isDecimal = False
decimalLength = 0
currentlabel = Label("",303,155,size=18)
stackLabels = []
for i in range(3):
    stackLabels.append(Label("",303,115-i*35,size=18))

# Misc stack stuff
def clear():
    global current, isDecimal, decimalLength
    current = None
    isDecimal = False
    decimalLength = 0
    
def clearAll():
    global stack
    clear()
    stack = []

def enter():
    if (current != None):
        stack.insert(0,current)
        clear()

def getNum(index):
    if (len(stack) > index):
        return stack[index]
    else:
        print("TODO: error message")
        
def pop():
    enter()
    if (len(stack) > 0):
        return stack.pop(0)
    else:
        print("TODO: error message")
    
def swap():
    enter()
    if (len(stack) > 1):
        temp = stack[0]
        stack[0] = stack[1]
        stack[1] = temp
    else:
        print("TODO: error message")

# Current number stuff
def typeDigit(digit):
    global current, decimalLength
    if (isDecimal):
        decimalLength += 1
        current += digit / (math.pow(10,decimalLength))
    else:
        if (current == None):
            current = digit
        else:
            current = current*10 + digit
            
def decimal():
    global isDecimal
    isDecimal = True
            
def backspace():
    global current, isDecimal, decimalLength
    if (isDecimal):
        if (decimalLength == 0):
            isDecimal = False
        else:
            decimalLength -= 1
            current = pythonRound(current, decimalLength)
    else:
        if (current != None):
            current = (current - current%10)/10
        if (current == 0):
            current = None
            
# Operations
def plus():
    enter()
    if (len(stack)<2):
        print("TODO: error message")
        return
    stack.insert(0,pop() + pop())

def minus():
    enter()
    if (len(stack)<2):
        print("TODO: error message")
        return
    stack.insert(0,-pop() + pop())
    
def times():
    enter()
    if (len(stack)<2):
        print("TODO: error message")
        return
    stack.insert(0,pop() * pop())
    
def divide():
    enter()
    if (len(stack)<2):
        print("TODO: error message")
        return
    temp = pop()
    stack.insert(0,pop() / temp)

# Called after input handling
def updateStackLabels():
    for i in range(3):
        if (len(stack) > i):
            stackLabels[i].value = f"{stack[i]:.8g}"
            stackLabels[i].right = 305
        else:
            stackLabels[i].value = ""
    
def updateCurrentLabel():
    global isDecimal, decimalLength
    if (current != None):
        if (isDecimal  and  decimalLength == 0):
            currentlabel.value = f"{current:.0f}" + "."
        else:
            currentlabel.value = f"{current:.{decimalLength}f}"
        currentlabel.right = 305
    else:
        currentlabel.value = ""
    
def onKeyPress(key):
    global current
    # print(key)
    match key:
        case "c":
            clear()
        case "C":
            clearAll()
        case "backspace":
            backspace()
        case "enter":
            enter()
        case "s":
            swap()
        case "p":
            pop()
        case ".":
            decimal()
        case "+":
            plus()
        case "-":
            minus()
        case "*":
            times()
        case "/":
            divide()
            
    if (key.isdigit()):
        typeDigit(int(key))
            
    updateStackLabels()
    updateCurrentLabel()
        
def onMousePress(mouseX, mouseY):
    for row in range(5):
        for col in range(5):
            if (buttons[row][col].hits(mouseX,mouseY)):
                onKeyPress(keys[row][col])
