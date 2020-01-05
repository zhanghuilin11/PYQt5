#--Time : 2020/1/5 19:44
#--Author : Zhang
#--File : qobj定时器.py
import sys
from PyQt5.Qt import *

class Mylab(QLabel):
    def timerEvent(self, *args,**kwargs):
        print('xx')
        self.setText(str(int(self.text())+1))

app = QApplication(sys.argv)




wind = QWidget()
wind.resize(500,500)
bnt = QPushButton(wind)
bnt.setText('按钮')

lab1 = Mylab(wind)
lab1.startTimer(1000)
lab1.setText('1   ')
lab1.setStyleSheet('')
lab1.move(100,100)

print(wind.size().width())


wind.show()
sys.exit(app.exec_())