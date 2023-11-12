from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import sys
import subprocess

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.myListWidget1 = QListWidget()
        self.myListWidget2 = QListWidget()

        run_button = QPushButton(QIcon("images/run.png"), "Run")
        str_button = QPushButton(QIcon("images/string.png"), "String")
        int_button = QPushButton(QIcon("images/int.png"), "Integer")
        var_button = QPushButton("Var")

        #self.myListWidget2.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setAcceptDrops(False)
        self.myListWidget1.setDragEnabled(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)

        self.myListWidget2.setDropIndicatorShown(True)  # Show drop indicator when reordering
        self.myListWidget2.setDefaultDropAction(Qt.MoveAction)  # Allow moving items
        self.myListWidget2.setSelectionMode(QAbstractItemView.SingleSelection)  # Single item selection

        gbuttons = [
            ("Game Init", "images/game.png", self.game_add)
        ]

        self.setGeometry(300, 350, 500, 300)
        self.hboxlayout = QHBoxLayout()
        self.gbutton_layout = QVBoxLayout()

        for label, icon_path, action in gbuttons:
            button = QPushButton(QIcon(icon_path), label)
            button.clicked.connect(action)
            self.gbutton_layout.addWidget(button)\
        
        self.hboxlayout.addLayout(self.gbutton_layout)
        self.hboxlayout.addWidget(self.myListWidget1)
        self.hboxlayout.addWidget(self.myListWidget2)
        
        

        self.button_layout1 = QVBoxLayout()
        buttons1 = [
            ("Run", "images/run.png", self.run_action),
            ("String", "images/string.png", self.str_add),
            ("Integer", "images/int.png", self.int_add),
            ("Variable", "images/var.png", self.var_add),
            ("Input", "images/terminal.png", self.input_add),
            ("Function", "images/func.png", self.func_add),
            ("Comment", "images/sticky.png", self.comment_add)
        ]

        for label, icon_path, action in buttons1:
            button = QPushButton(QIcon(icon_path), label)
            button.clicked.connect(action)
            self.button_layout1.addWidget(button)
    
            
        self.hboxlayout.addLayout(self.button_layout1)

        l1 = QListWidgetItem(QIcon("images/terminal.png"), 'Print')
        l2 = QListWidgetItem(QIcon("images/loop.png"), 'For Loop')
        l3 = QListWidgetItem(QIcon("images/loop.png"), 'End Loop')
        l13 = QListWidgetItem(QIcon("images/loop.png"), 'Forever')
        l9 = QListWidgetItem(QIcon("images/branch.png"), 'If')
        l10 = QListWidgetItem(QIcon("images/branch.png"), 'End If')
        l11 = QListWidgetItem(QIcon("images/func.png"), 'End Func')
        l4 = QListWidgetItem(QIcon("images/wait.png"), 'Wait')
        l5 = QListWidgetItem(QIcon("images/clock.png"), 'Current Time')
        l6 = QListWidgetItem(QIcon("images/clock.png"), 'Current Date')
        l7 = QListWidgetItem(QIcon("images/questionmark.png"), '<opx> Equal To')
        l8 = QListWidgetItem(QIcon("images/questionmark.png"), '<opx> Not Equal To')
        l14 = QListWidgetItem(QIcon("images/game.png"), '<game> update')
        l15 = QListWidgetItem(QIcon("images/game.png"), '<game> event loop')

        l0 = QListWidgetItem(QIcon("images/run.png"), 'On Run:')

        self.myListWidget1.insertItem(999, l1)
        self.myListWidget1.insertItem(999, l2)
        self.myListWidget1.insertItem(999, l3)
        self.myListWidget1.insertItem(999, l13)
        self.myListWidget1.insertItem(999, l9)
        self.myListWidget1.insertItem(999, l10)
        self.myListWidget1.insertItem(999, l11)
        self.myListWidget1.insertItem(999, l4)
        self.myListWidget1.insertItem(999, l5)
        self.myListWidget1.insertItem(999, l6)
        self.myListWidget1.insertItem(999, l7)
        self.myListWidget1.insertItem(999, l8)
        self.myListWidget1.insertItem(999, l14)
        self.myListWidget1.insertItem(999, l15)

            
        self.myListWidget2.insertItem(1, l0)

        self.setWindowTitle("Block Python")
        self.setWindowIcon(QtGui.QIcon('images/owo.png'))
        self.setLayout(self.hboxlayout)
        self.show()

    def run_action(self):
        u = []
        for index in range(self.myListWidget2.count()):
            item = self.myListWidget2.item(index)
            u.append(item.text())
        lines = []
        rargs = 0
        parg = ""
        vargs = 0
        oargs = 0
        xargs = 0
        indent = 0
        erag = False
        time = False
        game = False
        for prompt in u:
            if xargs != 0:
                if prompt.startswith("<str>"):
                    prompt = prompt.replace("<str> ", "")
                    if xargs == 1:
                        parg = f"{parg}'{prompt}'"
                        xargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<input>"):
                    prompt = prompt.replace("<input> ", "")
                    if xargs == 1:
                        parg = f"{parg}input('{prompt}')"
                        xargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("Current Date"):
                    if vargs == 1:
                        xarg = f"{parg}datetime.date.today()"
                        time = True
                        xargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("Current Time"):
                    if xargs == 1:
                        parg = f"{parg}datetime.datetime.now().strftime('%H:%M:%S')"
                        time = True
                        xargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<int>"):
                    try:
                        prompt = int(prompt.replace("<int> ", ""))
                    except ValueError:
                        return print("Non Int value in <int> tag")
                    except Exception as e:
                        return print(e)
                    if xargs == 1:
                        parg = f"{parg}{prompt}"
                        xargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<var>"):
                    prompt = prompt.replace("<var> ", "")
                    if xargs == 1:
                        parg = f"{parg}{prompt}"
                        xargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
            elif oargs != 0:
                if prompt.startswith("<opx> Equal To"):
                    if oargs == 1:
                        parg = f"{parg} == "
                        oargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<opx> Not Equal To"):
                    if oargs == 1:
                        parg = f"{parg} != "
                        oargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
            elif vargs != 0:
                if prompt.startswith("<str>"):
                    prompt = prompt.replace("<str> ", "")
                    if vargs == 1:
                        parg = f"{parg}'{prompt}'"
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                        vargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<input>"):
                    prompt = prompt.replace("<input> ", "")
                    if vargs == 1:
                        parg = f"{parg}input('{prompt}')"
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                        vargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("Current Date"):
                    if vargs == 1:
                        parg = f"{parg}datetime.date.today()"
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                        time = True
                        vargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("Current Time"):
                    if vargs == 1:
                        parg = f"{parg}datetime.datetime.now().strftime('%H:%M:%S')"
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                        time = True
                        vargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<var>"):
                    prompt = prompt.replace("<var> ", "")
                    if vargs == 1:
                        parg = f"{parg}{prompt}"
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                        vargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<int>"):
                    try:
                        prompt = int(prompt.replace("<int> ", ""))
                    except ValueError:
                        return print("Non Int value in <int> tag")
                    except Exception as e:
                        return print(e)
                    if vargs == 1:
                        parg = f"{parg}{prompt}"
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                        vargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
            elif rargs != 0:
                if prompt.startswith("<str>"):
                    prompt = prompt.replace("<str> ", "")
                    if rargs == 1:
                        parg = f"{parg}'{prompt}')"
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                        rargs = 0
                    elif rargs >1:
                        parg = f"{parg}'{prompt}', "
                        rargs -= 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<int>"):
                    try:
                        prompt = int(prompt.replace("<int> ", ""))
                    except ValueError:
                        return print("Non Int value in <int> tag")
                    except Exception as e:
                        return print(e)
                    if rargs == 1:
                        parg = f"{parg}{prompt})"
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                        rargs = 0
                    elif rargs >1:
                        parg = f"{parg}{prompt}, "
                        rargs -= 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<var>"):
                    prompt = prompt.replace("<var> ", "")
                    if rargs == 1:
                        parg = f"{parg}{prompt})"
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                        rargs = 0
                    elif rargs >1:
                        parg = f"{parg}{prompt}, "
                        rargs -= 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<input>"):
                    prompt = prompt.replace("<input> ", "")
                    if rargs == 1:
                        parg = f"{parg}input('{prompt}'))"
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                        rargs = 0
                    elif rargs >1:
                        parg = f"{parg}input('{prompt}'), "
                        rargs -= 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("Current Date"):
                    if rargs == 1:
                        parg = f"{parg}datetime.date.today())"
                        lines.append(parg)
                        time = True
                        rargs = 0
                    elif rargs >1:
                        parg = f"{parg}datetime.date.today() , "
                        rargs -= 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("Current Time"):
                    if rargs == 1:
                        parg = f"{parg}datetime.datetime.now().strftime('%H:%M:%S'))"
                        lines.append(parg)
                        time = True
                        rargs = 0
                    elif rargs >1:
                        parg = f"{parg}datetime.datetime.now().strftime('%H:%M:%S') , "
                        rargs -= 0
                    else: 
                        return print("Invalid Prompt(s)")
            else:
                parg = ""
                if indent != 0:
                    for f in range(indent):
                        parg = f"{parg}\t"
                if prompt == "On Run:":
                    pass
                elif prompt == "Print":
                    rargs = 1
                    parg = f"{parg}print("
                elif prompt == "For Loop":
                    rargs = 1
                    parg = f"{parg}for item in range("
                    erag = True
                    indent += 1
                elif prompt == "End Loop":
                    indent -= 1
                    pass
                elif prompt == "End If":
                    indent -= 1
                    pass
                elif prompt == "End Func":
                    indent -= 1
                    pass
                elif prompt == "Wait":
                    rargs = 1
                    parg = f"{parg}time.sleep("
                    time = True
                elif prompt == "If":
                    erag = True
                    xargs = 1
                    vargs = 1
                    oargs = 1
                    parg = f"{parg}if "
                    indent += 1
                elif prompt == "Forever":
                    parg = f"{parg}while True:"
                    indent += 1
                    lines.append(parg)
                elif prompt.startswith("<var> "):
                    vargs = 1
                    prompt = prompt.replace("<var> ", "")
                    parg = f"{parg}{prompt} = "
                elif prompt.startswith("<comment> "):
                    prompt = prompt.replace("<comment> ", "")
                    parg = f"{parg}# {prompt}"
                    lines.append(parg)
                elif prompt.startswith("<createfunc> "):
                    prompt = prompt.replace("<createfunc> ", "")
                    parg = f"{parg}def {prompt}():"
                    lines.append(parg)
                    indent += 1
                elif prompt.startswith("<func> "):
                    prompt = prompt.replace("<func> ", "")
                    parg = f"{parg}{prompt}()"
                    lines.append(parg)
                elif prompt.startswith("<game> "):
                    prompt = prompt.replace("<game> ", "")
                    if prompt.startswith("init "):
                        prompt = prompt.replace("init ", "")
                        garg = f"{parg}pygame.init()"
                        lines.append(garg)
                        prompt = prompt.replace("l=", "")
                        prompt = prompt.replace("h=", "")
                        prompt = prompt.replace("c=", "")
                        owo = prompt.split()
                        garg = f"{parg}screen = pygame.display.set_mode(({owo[0]},{owo[1]}))\nclock = pygame.time.Clock()\nframerate = {owo[2]}"
                        lines.append(garg)
                        game = True
                    elif prompt.startswith("update"):
                        marg = f"{parg}pygame.display.update()"
                        lines.append(marg)
                        marg = f"{parg}clock.tick(framerate)"
                        lines.append(marg)
                        game = True
                    elif prompt.startswith("event loop"):
                        indent += 1
                        marg = f"{parg}for event in pygame.event.get():"
                        lines.append(marg)
                        parg = f"{parg}\t"
                        marg = f"{parg}if event.type == pygame.QUIT:"
                        lines.append(marg)
                        parg = f"{parg}\t"
                        marg = f"{parg}pygame.quit()"
                        lines.append(marg)
                        marg = f"{parg}sys.exit()"
                        lines.append(marg)
                        game = True
                else:
                    return print("Invalid prompt(s)")
                
        output = ""
        for line in lines:
            if time == True:
                output = f"{output}import time\nimport datetime\n"
                time = False
            if game == True:
                output = f"{output}import pygame\nimport sys\n"
                game = False
            output = f"{output}{line}\n"                    
        with open("output.py", "w") as file:
            file.write(output)
        
        subprocess.Popen(['python', 'output.py'])
    
    def str_add(self):
        text, ok = QInputDialog.getText(self, 'Create String', 'Enter the string value:')
        s1 = QListWidgetItem(QIcon("images/string.png"), f'<str> {text}')
        self.myListWidget2.insertItem(1000, s1)
    
    def int_add(self):
        text, ok = QInputDialog.getText(self, 'Create Integer', 'Enter the value:')
        s1 = QListWidgetItem(QIcon("images/int.png"), f'<int> {text}')
        self.myListWidget2.insertItem(1000, s1)

    def var_add(self):
        text, ok = QInputDialog.getText(self, 'Create Variable', 'Enter the name:')
        s1 = QListWidgetItem(QIcon("images/var.png"), f'<var> {text}')
        self.myListWidget1.insertItem(1000, s1)
    
    def func_add(self):
        text, ok = QInputDialog.getText(self, 'Create Function', "Enter the function's name:")
        s1 = QListWidgetItem(QIcon("images/func.png"), f'<func> {text}')
        self.myListWidget1.insertItem(1000, s1)
        s2 = QListWidgetItem(QIcon("images/func.png"), f'<createfunc> {text}')
        self.myListWidget2.insertItem(1000, s2)

    def input_add(self):
        text, ok = QInputDialog.getText(self, 'Create An Input', 'Enter the input prompt:')
        s1 = QListWidgetItem(QIcon("images/terminal.png"), f'<input> {text}')
        self.myListWidget2.insertItem(1000, s1)
    
    def comment_add(self):
        text, ok = QInputDialog.getText(self, 'Create a Comment', 'Enter the comment')
        s1 = QListWidgetItem(QIcon("images/sticky.png"), f'<comment> {text}')
        self.myListWidget2.insertItem(1000, s1)

    def game_add(self): 
        length, ok = QInputDialog.getText(self, 'Create a game', 'Enter the screen length:')
        height, ok = QInputDialog.getText(self, 'Create a game', 'Enter the screen height:')
        clock, ok = QInputDialog.getText(self, 'Create a game', 'Enter the FrameRate (60 is suggested):')

        s1 = QListWidgetItem(QIcon("images/game.png"), f'<game> init l={length} h={height} c={clock}')
        self.myListWidget2.insertItem(1000, s1)

    def other_action(self):
        print("Other button clicked")

app = QApplication(sys.argv)

window = Window()

app.exec_()
