from PyQt5 import QtCore, QtGui, QtWidgets
import random, fcfs, sjfpre, sjfnonpre, prioritypre, prioritynonpre

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelpno = QtWidgets.QLabel(self.centralwidget)
        self.labelpno.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.labelpno.setObjectName("labelpno")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 101, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 101, 19))
        self.label_2.setObjectName("label_2")
        self.addp = QtWidgets.QPushButton(self.centralwidget)
        self.addp.setGeometry(QtCore.QRect(150, 90, 131, 41))
        self.addp.setObjectName("addp")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 20, 20, 221))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ptable = QtWidgets.QTableWidget(self.centralwidget)
        self.ptable.setGeometry(QtCore.QRect(300, 21, 401, 221))
        self.ptable.setAutoScroll(False)
        self.ptable.setObjectName("ptable")
        self.ptable.setColumnCount(4)
        self.ptable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.ptable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ptable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ptable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ptable.setHorizontalHeaderItem(3, item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.algoselect = QtWidgets.QComboBox(self.centralwidget)
        self.algoselect.setGeometry(QtCore.QRect(180, 270, 321, 41))
        self.algoselect.setObjectName("algoselect")
        self.algoselect.addItem("")
        self.algoselect.addItem("")
        self.algoselect.addItem("")
        self.algoselect.addItem("")
        self.algoselect.addItem("")
        self.algoselect.addItem("")
        self.calcubutton = QtWidgets.QPushButton(self.centralwidget)
        self.calcubutton.setGeometry(QtCore.QRect(520, 270, 131, 41))
        self.calcubutton.setStyleSheet("font: 75 14pt \"Waree\";")
        self.calcubutton.setObjectName("calcubutton")
        self.arrtime = QtWidgets.QLineEdit(self.centralwidget)
        self.arrtime.setGeometry(QtCore.QRect(20, 100, 113, 27))
        self.arrtime.setObjectName("arrtime")
        self.burtime = QtWidgets.QLineEdit(self.centralwidget)
        self.burtime.setGeometry(QtCore.QRect(20, 170, 113, 27))
        self.burtime.setObjectName("burtime")
        self.pnolabel = QtWidgets.QLabel(self.centralwidget)
        self.pnolabel.setGeometry(QtCore.QRect(110, 30, 31, 21))
        self.pnolabel.setStyleSheet("font: 75 14pt \"DejaVu Sans\";")
        self.pnolabel.setObjectName("pnolabel")
        self.clrbutton = QtWidgets.QPushButton(self.centralwidget)
        self.clrbutton.setGeometry(QtCore.QRect(600, 220, 81, 21))
        self.clrbutton.setObjectName("clrbutton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(170, 370, 120, 80))
        self.widget.setObjectName("widget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 320, 711, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.qtext = QtWidgets.QTextBrowser(self.centralwidget)
        self.qtext.setGeometry(QtCore.QRect(90, 330, 491, 192))
        self.qtext.setObjectName("qtext")
        self.priovalue = QtWidgets.QLineEdit(self.centralwidget)
        self.priovalue.setGeometry(QtCore.QRect(20, 240, 113, 27))
        self.priovalue.setObjectName("priovalue")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 191, 19))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
       # Custom code
        self.addp.clicked.connect(self.addprocess)
        self.clrbutton.clicked.connect(self.cleartable)
        self.calcubutton.clicked.connect(self.calculate)



    def addprocess(self):
        # print(self.ptable.rowCount(), self.pnolabel.text(),self.arrtime.text(),self.burtime.text())  
        if self.arrtime.text().isnumeric():
            arrivaltime = self.arrtime.text()
        else:
            arrivaltime = str(random.randint(1,15))

        if self.burtime.text().isnumeric():
            burstime = self.burtime.text()
        else:
            burstime = str(random.randint(1,15))

        if self.priovalue.text().isnumeric():
            prioval = self.priovalue.text()
        else:
            prioval = str(random.randint(1,15))


        self.ptable.setRowCount(self.ptable.rowCount()+1)

        self.ptable.setItem(self.ptable.rowCount()-1, 0, QtWidgets.QTableWidgetItem( self.pnolabel.text() ))
        self.ptable.setItem(self.ptable.rowCount()-1, 1, QtWidgets.QTableWidgetItem( arrivaltime ))
        self.ptable.setItem(self.ptable.rowCount()-1, 2, QtWidgets.QTableWidgetItem( burstime ))
        self.ptable.setItem(self.ptable.rowCount()-1, 3, QtWidgets.QTableWidgetItem( prioval ))

        self.pnolabel.setText(str(int(self.pnolabel.text())+1))
        self.arrtime.clear()
        self.burtime.clear()

    def cleartable(self):
        self.ptable.clearContents()
        self.ptable.setRowCount(0)
        self.pnolabel.setText("1")

    def calculate(self):
        pd = dict()
        r= self.ptable.rowCount()
        for i in range(r):    # getting all the data from the table in a dictoinary-list.
            pd[str(i+1)]=[int(self.ptable.item(i,1).text()), int(self.ptable.item(i,2).text()),\
                                    int(self.ptable.item(i,3).text())]
        print(pd)
        # calling the corresponding function:
        selected = self.algoselect.currentText()
        if selected == "First Come First Served":
            fcfsdict,pLine,avgwait,avgturntime = fcfs.fcfs(pd)
            print("in design: ",fcfsdict)
            self.printData(pd,fcfsdict,pLine,avgwait,avgturntime,'First Come First Serve')
        
        elif selected == "Shortest Job First: Preemptive":
            sjfpredict,pLine,avgwait,avgturntime = sjfpre.sjfpre(pd)
            self.printData(pd,sjfpredict,pLine,avgwait,avgturntime,'Shortest Job First: Preemptive')
        
        elif selected == "Shortest Job First: Non-Preemptive":
            sjfnonpredict,pLine,avgwait,avgturntime = sjfnonpre.sjfnonpre(pd)
            self.printData(pd,sjfnonpredict,pLine,avgwait,avgturntime,'Shortest Job First: Non-Preemptive')
        
        elif selected == "Priority Scheduling: Preemptive":
            priopredict,pLine,avgwait,avgturntime = prioritypre.priopre(pd)
            self.printData(pd,priopredict,pLine,avgwait,avgturntime,'Priority Scheduling: Preemptive')
        
        elif selected == "Priority Scheduling: Non-Preemptive":
            priononpredict,pLine,avgwait,avgturntime = prioritynonpre.priononpre(pd)
            self.printData(pd,priononpredict,pLine,avgwait,avgturntime,'Priority Scheduling: Non-Preemptive')
        
        elif selected == "All":
            returndict,pLine,avgwait,avgturntime=[1 for i in range(5)],\
                    [1 for i in range(5)],[1 for i in range(5)],[1 for i in range(5)]
            returndict[0],pLine[0],avgwait[0],avgturntime[0] = fcfs.fcfs(pd)
            returndict[1],pLine[1],avgwait[1],avgturntime[1] = sjfpre.sjfpre(pd)
            returndict[2],pLine[2],avgwait[2],avgturntime[2] = sjfnonpre.sjfnonpre(pd)
            returndict[3],pLine[3],avgwait[3],avgturntime[3] = prioritypre.priopre(pd)
            returndict[4],pLine[4],avgwait[4],avgturntime[4] = prioritynonpre.priononpre(pd)

            # print("returned values:",returndict,'\n',pLine,'\n',avgturntime,'\n',avgwait)
            print('average turns: ',avgturntime)
            minturnindx = avgturntime.index(min(avgturntime))
            self.printData(pd,returndict[minturnindx],pLine[minturnindx],avgwait[minturnindx],\
                avgturntime[minturnindx], self.algoselect.itemText(minturnindx+1))

    def printData(self, gData, cData, pLine, avgwait, avgturntime, Name): #(self,pd,turnaroundtimes,wallclock,'fcfs')
        # print("inside printdata: ",pLine)
        plinestr= "{} -> ".format(pLine[0][0])
        del pLine[0]
        a = "  "*20 + str(Name.upper())+"\n"

        a = a+ '\n' +str('| Pno. | ARRIVAL | BURST | WAIT | TURNAROUND |')

        for key,value in sorted(cData.items()):
            a = a+ '\n' +str('{:>4}{:>16}{:>18}{:>14}{:>15}'.format(key,gData[key][0],gData[key][1],value[0],value[1]))
            
        # print(avgwait,avgturntime)
        a = a+ '\n' +str('Average Wait Time = {}  \
          Average Turnaround Time = {}\n'.format(round(avgwait,2),round(avgturntime,2)))

        for x in pLine:
            plinestr += ('P{} -> {} -> '.format(x[0],x[1]))
        a = a+ '\n' +str('{}\n'.format(plinestr[:-3]))

        self.qtext.setText(a)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelpno.setText(_translate("MainWindow", "Process No."))
        self.label.setText(_translate("MainWindow", "Arrival time:"))
        self.label_2.setText(_translate("MainWindow", "Burst time:"))
        self.addp.setText(_translate("MainWindow", "Add process ➜"))
        item = self.ptable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Process No."))
        item = self.ptable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Arrival time"))
        item = self.ptable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Burst time"))
        item = self.ptable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Priority"))
        self.label_3.setText(_translate("MainWindow", "Select Algorithm:"))
        self.algoselect.setItemText(0, _translate("MainWindow", "All"))
        self.algoselect.setItemText(1, _translate("MainWindow", "First Come First Served"))
        self.algoselect.setItemText(2, _translate("MainWindow", "Shortest Job First: Preemptive"))
        self.algoselect.setItemText(3, _translate("MainWindow", "Shortest Job First: Non-Preemptive"))
        self.algoselect.setItemText(4, _translate("MainWindow", "Priority Scheduling: Preemptive"))
        self.algoselect.setItemText(5, _translate("MainWindow", "Priority Scheduling: Non-Preemptive"))
        self.calcubutton.setText(_translate("MainWindow", "Calculate"))
        self.pnolabel.setText(_translate("MainWindow", "1"))
        self.clrbutton.setText(_translate("MainWindow", "Clear"))
        self.label_4.setText(_translate("MainWindow", "Priority(lower is higher):"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
