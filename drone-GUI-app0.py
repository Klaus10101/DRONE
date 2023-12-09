
import PyQt5.QtWidgets as q
import PyQt5.QtGui as qt
# from PyQt5.QtWidgets import QWidget
class MainWindow(q.QWidget):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("APPLICATION") #for adding a title
        self.setLayout(q.QVBoxLayout())#for a vertical layout
        l = q.QLabel("GUI OF DRONE APPLICATION .0\n") #label hai ye apne app ka
        self.layout().addWidget(l)
        l.setFont(qt.QFont('helvetics',18))# font size change karne ke liye label ka .
        
        # entry box ka code yaha par shuru👇👇 abhi comment kiya hai jab jarurat hogi tab uncomment karlenge
        # me = q.QLineEdit()
        # me.setObjectName("name")
        # me.setText("")
        # self.layout().addWidget(me)
        # likne wale mtlb entry  box ka code yaha par 
         
         #list wale box ka code👇👇👇
        mc = q.QComboBox(self,editable=True,insertPolicy=q.QComboBox.InsertAtBottom)
        mc.addItem("S formation")
        mc.addItem("l formation", "h formation")
        # mc.addItem("👾")
        mc.addItems(['Y formation','T formation','Z formation'])
        self.layout().addWidget(mc)


        
        mb = q.QPushButton("ENTER !!",clicked = lambda:daba_de()) #ye tera button hogaya

        self.layout().addWidget(mb)

        self.show()
        def daba_de(): #ye function type kiye huye text ko fstring mein likhe gaye word ke saath jod sakta haiand
            # curly brakets mein jo value hai data ko show karne ke liye hai.
            # l.setText(f'DRONE{me.text()}')
            # me.setText("")
            l.setText(f'SELECTED Formation\n: {mc.currentText()}')
            


app = q.QApplication([])
mw = MainWindow()#ye samajh le (ye main window ke liye)
app.exec_() #application ko execute karne ke liye