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

        run_button = QPushButton(QIcon("run.png"), "Run")
        str_button = QPushButton(QIcon("string.png"), "String")
        int_button = QPushButton(QIcon("int.png"), "Integer")
        var_button = QPushButton("Var")

        #self.myListWidget2.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setAcceptDrops(False)
        self.myListWidget1.setDragEnabled(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)

        self.myListWidget2.setDropIndicatorShown(True)  # Show drop indicator when reordering
        self.myListWidget2.setDefaultDropAction(Qt.MoveAction)  # Allow moving items
        self.myListWidget2.setSelectionMode(QAbstractItemView.SingleSelection)  # Single item selection

        self.setGeometry(300, 350, 500, 300)
        self.hboxlayout = QHBoxLayout()
        self.hboxlayout.addWidget(self.myListWidget1)
        self.hboxlayout.addWidget(self.myListWidget2)
        
        self.button_layout1 = QVBoxLayout()
        buttons1 = [
            ("Run", "run.png", self.run_action),
            ("String", "string.png", self.str_add),
            ("Integer", "int.png", self.int_add),
            ("Variable", "var.png", self.var_add),
            ("Input", "terminal.png", self.input_add),
            ("Function", "func.png", self.other_action)
        ]
        for label, icon_path, action in buttons1:
            button = QPushButton(QIcon(icon_path), label)
            button.clicked.connect(action)
            self.button_layout1.addWidget(button)
            
        self.hboxlayout.addLayout(self.button_layout1)

        l1 = QListWidgetItem(QIcon("terminal.png"), 'Print')
        l2 = QListWidgetItem(QIcon("loop.png"), 'For Loop')
        l3 = QListWidgetItem(QIcon("loop.png"), 'End Loop')
        l4 = QListWidgetItem(QIcon("wait.png"), 'Wait')

        l0 = QListWidgetItem(QIcon("run.png"), 'On Run:')

        self.myListWidget1.insertItem(1, l1)
        self.myListWidget1.insertItem(2, l2)
        self.myListWidget1.insertItem(3, l3)
        self.myListWidget1.insertItem(4, l4)

        self.myListWidget2.insertItem(1, l0)

        self.setWindowTitle("Block Python")
        self.setWindowIcon(QtGui.QIcon('owo.png'))
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
        indent = False
        erag = False
        time = False
        for prompt in u:
            if vargs != 0:
                if prompt.startswith("<str>"):
                    prompt = prompt.replace("<str> ", "")
                    if vargs == 1:
                        parg = f"{parg}'{prompt}'"
                        lines.append(parg)
                        vargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                if prompt.startswith("<input>"):
                    prompt = prompt.replace("<input> ", "")
                    if vargs == 1:
                        parg = f"{parg}input('{prompt}')"
                        lines.append(parg)
                        vargs = 0
                    else: 
                        return print("Invalid Prompt(s)")
                if prompt.startswith("<int>"):
                    try:
                        prompt = int(prompt.replace("<int> ", ""))
                    except:
                        return print("Non Int value in <int> tag")
                    if vargs == 1:
                        parg = f"{parg}{prompt}"
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
                    except:
                        return print("Non Int value in <int> tag")
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
            else:
                parg = ""
                if indent == True:
                    parg = "\t"
                if prompt == "On Run:":
                    pass
                elif prompt == "Print":
                    rargs = 1
                    parg = f"{parg}print("
                elif prompt == "For Loop":
                    rargs = 1
                    parg = f"{parg}for item in range("
                    erag = True
                    indent = True
                elif prompt == "End Loop":
                    indent = False
                    pass
                elif prompt == "Wait":
                    rargs = 1
                    parg = f"{parg}time.sleep("
                    time = True
                elif prompt.startswith("<var> "):
                    vargs = 1
                    prompt = prompt.replace("<var> ", "")
                    parg = f"{parg}{prompt} = "
                else:
                    return print("Invalid prompt(s)")
                
        output = ""
        for line in lines:
            if time == True:
                output = f"{output}import time\n"
                time = False
            output = f"{output}{line}\n"                    
        with open("output.py", "w") as file:
            file.write(output)
        
        subprocess.Popen(['python', 'output.py'])
    
    def str_add(self):
        text, ok = QInputDialog.getText(self, 'Create String', 'Enter the string value:')
        s1 = QListWidgetItem(QIcon("string.png"), f'<str> {text}')
        self.myListWidget2.insertItem(1000, s1)
    
    def int_add(self):
        text, ok = QInputDialog.getText(self, 'Create Integer', 'Enter the value:')
        s1 = QListWidgetItem(QIcon("int.png"), f'<int> {text}')
        self.myListWidget2.insertItem(1000, s1)

    def var_add(self):
        text, ok = QInputDialog.getText(self, 'Create Variable', 'Enter the name:')
        s1 = QListWidgetItem(QIcon("var.png"), f'<var> {text}')
        self.myListWidget1.insertItem(1000, s1)

    def input_add(self):
        text, ok = QInputDialog.getText(self, 'Create An Input', 'Enter the input prompt:')
        s1 = QListWidgetItem(QIcon("terminal.png"), f'<input> {text}')
        self.myListWidget2.insertItem(1000, s1)

    def other_action(self):
        print("Other button clicked")

app = QApplication(sys.argv)

window = Window()

app.exec_()
