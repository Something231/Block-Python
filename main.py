from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import sys
import subprocess

print('Block Python - Copyright (c) 2023 Hamish Briggs')

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
            ("Game Init", "images/game.png", self.game_add),
            ("Game Title", "images/game.png", self.game_title),
            ("Game bg colour", "images/game.png", self.game_bgcolour),
            ("Game New Rect", "images/game.png", self.game_rect),
            ("Check Collisions", "images/game.png", self.game_cls),
            ("Get Dict Item", "images/json.png", self.getitem),
            ("Save Program", "images/save.png", self.save),
            ("Load Program", "images/load.png", self.load)
        ]

        self.setGeometry(300, 350, 500, 300)
        self.hboxlayout = QHBoxLayout()
        self.gbutton_layout = QVBoxLayout()

        for label, icon_path, action in gbuttons:
            button = QPushButton(QIcon(icon_path), label)
            button.clicked.connect(action)
            self.gbutton_layout.addWidget(button)
        
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
        l16 = QListWidgetItem(QIcon("images/math.png"), '<math> Add')
        l17 = QListWidgetItem(QIcon("images/math.png"), '<math> Subtract')
        l7 = QListWidgetItem(QIcon("images/questionmark.png"), '<opx> Equal To')
        l8 = QListWidgetItem(QIcon("images/questionmark.png"), '<opx> Not Equal To')
        l18 = QListWidgetItem(QIcon("images/questionmark.png"), '<opx> Is Larger Than')
        l19 = QListWidgetItem(QIcon("images/questionmark.png"), '<opx> Is Smaller Than')
        l14 = QListWidgetItem(QIcon("images/game.png"), '<game> update')
        l15 = QListWidgetItem(QIcon("images/game.png"), '<game> event loop')
        l22 = QListWidgetItem(QIcon("images/game.png"), '<game> event type')
        l23 = QListWidgetItem(QIcon("images/game.png"), '<game> event keypress')
        l28 = QListWidgetItem(QIcon("images/game.png"), '<game> keytype')
        l24 = QListWidgetItem(QIcon("images/game.png"), '<game> key up')
        l25 = QListWidgetItem(QIcon("images/game.png"), '<game> key down')
        l26 = QListWidgetItem(QIcon("images/game.png"), '<game> key left')
        l27 = QListWidgetItem(QIcon("images/game.png"), '<game> key right')
        l31 = QListWidgetItem(QIcon("images/game.png"), '<game> key W')
        l32 = QListWidgetItem(QIcon("images/game.png"), '<game> key S')
        l20 = QListWidgetItem(QIcon("images/request.png"), 'HTTP Request')
        l21 = QListWidgetItem(QIcon("images/json.png"), 'Convert From JSON')
        l29 = QListWidgetItem(QIcon("images/true.png"), 'TRUE')
        l30 = QListWidgetItem(QIcon("images/false.png"), 'FALSE')
        

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
        self.myListWidget1.insertItem(999, l16)
        self.myListWidget1.insertItem(999, l17)
        self.myListWidget1.insertItem(999, l7)
        self.myListWidget1.insertItem(999, l8)
        self.myListWidget1.insertItem(999, l18)
        self.myListWidget1.insertItem(999, l19)
        self.myListWidget1.insertItem(999, l14)
        self.myListWidget1.insertItem(999, l15)
        self.myListWidget1.insertItem(999, l22)
        self.myListWidget1.insertItem(999, l23)
        self.myListWidget1.insertItem(999, l28)
        self.myListWidget1.insertItem(999, l24)
        self.myListWidget1.insertItem(999, l25)
        self.myListWidget1.insertItem(999, l26)
        self.myListWidget1.insertItem(999, l27)
        self.myListWidget1.insertItem(999, l31)
        self.myListWidget1.insertItem(999, l32)
        self.myListWidget1.insertItem(999, l20)
        self.myListWidget1.insertItem(999, l21)
        self.myListWidget1.insertItem(999, l29)
        self.myListWidget1.insertItem(999, l30)

            
        self.myListWidget2.insertItem(1, l0)
        
        self.myListWidget2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.myListWidget2.customContextMenuRequested.connect(self.show_context_menu)

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
        jargs = 0
        indent = 0
        erag = False
        time = False
        game = False
        rand = False
        requests = False
        njson = False
        for prompt in u:
            if jargs != 0:
                if prompt.startswith("<math>"):
                    prompt = prompt.replace("<math> ", "")
                    if jargs == 1:
                        jargs = 0
                        if prompt.startswith("Add"):
                            parg = f"{parg} + "
                            vargs += 1
                        elif prompt.startswith("Subtract"):
                            parg = f"{parg} - "
                            vargs += 1
                    else: 
                        return print("Invalid Prompt(s)")
                else:
                    jargs = 0
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
                elif prompt.startswith("<game> event type"):
                    if xargs == 1:
                        parg = f"{parg}event.type"
                        xargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<game> keytype"):
                    if xargs == 1:
                        parg = f"{parg}event.key"
                        xargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("TRUE"):
                    if xargs == 1:
                        parg = f"{parg}True"
                        xargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("FALSE"):
                    if xargs == 1:
                        parg = f"{parg}False"
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
                elif prompt.startswith("<opx> Is Larger Than"):
                    if oargs == 1:
                        parg = f"{parg} > "
                        oargs = 0
                elif prompt.startswith("<opx> Is Smaller Than"):
                    if oargs == 1:
                        parg = f"{parg} < "
                        oargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
            elif vargs != 0:
                jargs += 1
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
                elif prompt.startswith("<game> rect "):
                    prompt = prompt.replace("<game> rect ", "")
                    prompt = prompt.replace("c=", "")
                    prompt = prompt.replace("x=", "")
                    prompt = prompt.replace("y=", "")
                    prompt = prompt.replace("w=", "")
                    prompt = prompt.replace("h=", "")
                    owo = prompt.split()
                    parg = f"{parg}pygame.draw.rect(screen, pygame.Color('{owo[0]}'), ({owo[1]}, {owo[2]}, {owo[3]}, {owo[4]}))"
                    lines.append(parg)
                    vargs = 0
                    game = True
                elif prompt == "HTTP Request":
                    requests = True
                    parg = f"{parg}requests.get("
                    vargs = 0
                    rargs += 1
                elif prompt == "Convert From JSON":
                    njson = True
                    oo = parg.split()
                    zz = oo[0]
                    parg = f"{parg}{zz}.json()"
                    vargs = 0
                    lines.append(parg)
                elif prompt.startswith("<dict> item "):
                    if vargs == 1:
                        prompt = prompt.replace("<dict> item ", "")
                        oo = parg.split()
                        zz = oo[0]
                        parg = f"{parg}{zz}['{prompt}']"
                        lines.append(parg)
                        vargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<game> event type"):
                    if vargs == 1:
                        parg = f"{parg}event.type"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<game> event keypress"):
                    if vargs == 1:
                        parg = f"{parg}pygame.KEYDOWN"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<game> keytype"):
                    if vargs == 1:
                        parg = f"{parg}event.key"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<game> key up"):
                    if vargs == 1:
                        parg = f"{parg}pygame.K_UP"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<game> key down"):
                    if vargs == 1:
                        parg = f"{parg}pygame.K_DOWN"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<game> key left"):
                    if vargs == 1:
                        parg = f"{parg}pygame.K_LEFT"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<game> key right"):
                    if vargs == 1:
                        parg = f"{parg}pygame.K_RIGHT"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<game> key W"):
                    if vargs == 1:
                        parg = f"{parg}pygame.K_w"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<game> key S"):
                    if vargs == 1:
                        parg = f"{parg}pygame.K_s"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("<game> c-check if "):
                    if vargs == 1:
                        prompt = prompt.replace("<game> c-check if ", "")
                        prompt = prompt.replace(" is colliding", "")
                        prompt = prompt.split()
                        parg = f"{parg}{prompt[0]}.colliderect({prompt[1]})"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("TRUE"):
                    if vargs == 1:
                        parg = f"{parg}True"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
                    else: 
                        return print("Invalid Prompt(s)")
                elif prompt.startswith("FALSE"):
                    if vargs == 1:
                        parg = f"{parg}False"
                        vargs = 0
                        if erag == True:
                            erag = False
                            parg = f"{parg}:"
                        lines.append(parg)
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
                elif prompt.startswith("random"):
                    parg = f"{parg}time.sleep("
                    rand = True
                    lines.append(parg)
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
                    elif prompt.startswith("title"):
                        prompt = prompt.replace("title ", "")
                        parg = f"{parg}pygame.display.set_caption('{prompt}')"
                        lines.append(parg)
                        game = True
                    elif prompt.startswith("bg colour"):
                        prompt = prompt.replace("bg colour ", "")
                        parg = f"{parg}screen.fill(pygame.Color('{prompt}'))"
                        lines.append(parg)
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
            if requests == True:
                output = f"{output}import requests\n"
                requests = False
            if njson == True:
                output = f"{output}import json\n"
                njson = False
            if rand == True:
                output = f"{output}import random\n"
                rand = False
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

    def game_title(self):
        text, ok = QInputDialog.getText(self, 'Enter the title for your game', 'Enter the title:')
        s1 = QListWidgetItem(QIcon("images/game.png"), f'<game> title {text}')
        self.myListWidget2.insertItem(1000, s1)
        
    def game_bgcolour(self):
        text, ok = QInputDialog.getText(self, 'Background Colour', 'Enter the background colour:')
        s1 = QListWidgetItem(QIcon("images/game.png"), f'<game> bg colour {text}')
        self.myListWidget2.insertItem(1000, s1)
    
    def getitem(self):
        text, ok = QInputDialog.getText(self, 'Dict Item', 'Enter item you want to get from a dict')
        s1 = QListWidgetItem(QIcon("images/json.png"), f'<dict> item {text}')
        self.myListWidget2.insertItem(1000, s1)

    def game_add(self): 
        length, ok = QInputDialog.getText(self, 'Create a game', 'Enter the screen length:')
        height, ok = QInputDialog.getText(self, 'Create a game', 'Enter the screen height:')
        clock, ok = QInputDialog.getText(self, 'Create a game', 'Enter the FrameRate (60 is suggested):')

        s1 = QListWidgetItem(QIcon("images/game.png"), f'<game> init l={length} h={height} c={clock}')
        self.myListWidget2.insertItem(1000, s1)

    def game_rect(self): 
        colour, ok = QInputDialog.getText(self, 'Create a rectangle', 'Enter the colour:')
        xpos, ok = QInputDialog.getText(self, 'Create a rectangle', 'Enter x position:')
        ypos, ok = QInputDialog.getText(self, 'Create a rectangle', 'Enter y position:')
        width, ok = QInputDialog.getText(self, 'Create a rectangle', 'Enter rectangle width:')
        height, ok = QInputDialog.getText(self, 'Create a rectangle', 'Enter rectangle height:')

        s1 = QListWidgetItem(QIcon("images/game.png"), f'<game> rect c={colour} x={xpos} y={ypos} w={width} h={height}')
        self.myListWidget2.insertItem(1000, s1)
    
    def game_cls(self): 
        item1, ok = QInputDialog.getText(self, 'Checking Collision (game)', 'What item are you checking?')
        item2, ok = QInputDialog.getText(self, 'Checking Collision (game)', 'What item are you checking to collide?')
        s1 = QListWidgetItem(QIcon("images/game.png"), f'<game> c-check if {item2} is colliding {item1}')
        self.myListWidget2.insertItem(1000, s1)

    def other_action(self):
        print("Other button clicked")
    
    def save(self):
        s = []
        for index in range(self.myListWidget2.count()):
            item = self.myListWidget2.item(index)
            s.append(item.text())
        output = ""
        for line in s:
            output = f"{output}{line}\n"
        with open("saved.bloc", "w") as f:
            f.write(output)
        print("File Saved!")
    
    def load(self):
        with open("saved.bloc", "r") as f:
            data = f.read()
        self.myListWidget2.clear()
        mexico = []
        for line in data.split("\n"):
            if line != "":               
                mexico.append(line)
        for item in mexico:
            p1 = QListWidgetItem(QIcon("images/cpp.png"), item)
            self.myListWidget2.insertItem(1000, p1)
    
    def show_context_menu(self, position):
        # Create a context menu
        context_menu = QMenu(self)
        delete_action = QAction('Delete', self)
        delete_action.triggered.connect(self.delete_item)
        context_menu.addAction(delete_action)

        # Show the context menu at the cursor position
        context_menu.exec_(self.myListWidget2.mapToGlobal(position))

    def delete_item(self):
        selected_item = self.myListWidget2.currentItem()
        if selected_item:
            # Display a confirmation dialog
            reply = QMessageBox.question(self, 'Delete Item', 'Are you sure you want to delete this item?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Remove the selected item from myListWidget2
                self.myListWidget2.takeItem(self.myListWidget2.row(selected_item))
        else:
            QMessageBox.warning(self, 'Warning', 'No item selected for deletion.', QMessageBox.Ok)

app = QApplication(sys.argv)

window = Window()

app.exec_()
