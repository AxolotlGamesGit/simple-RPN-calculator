Rect(75,20,250,360,fill=None,border="black",borderWidth=4)
Rect(85,30,230,30,fill="lightgrey")
Rect(85,65,230,30,fill="lightgrey")
Rect(85,100,230,30,fill="lightgrey")
Rect(85,135,230,30,fill="lightgrey")

buttons = [[0 for _ in range(5)] for _ in range(5)]
labels = [['C',' ',' ',' ',' '],
          ['1','2','3','+',' '],
          ['4','5','6','-',' '],
          ['7','8','9','*',' '],
          ['0','.',' ','/',' ']]
for row in range(5):
    for col in range(5):
        buttons[row][col] = Rect(100+col*40,175+row*40,35,35,fill="lightgrey")
        labels[row][col] = Label(labels[row][col],117.5+col*40,192.5+row*40,size=18)

clearAll = buttons[0][2]
clearAll.width = 75
clearAll.fill = "yellow"
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
