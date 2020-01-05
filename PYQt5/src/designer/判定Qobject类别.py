#--Time : 2020/1/5 13:18
#--Author : Zhang
#--File : 判定Qobject类别.py

from PyQt5.Qt import *
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
        #判定Qobject类别
    def Qobj():
        ojb = QObject()
        w = QWidget()
        btn = QPushButton()
        lab = QLabel()
        obs = [ojb,w,btn,lab]
        for i in obs:
            # 判定Qwidget类别
            print(i.isWidgetType())
            # 判定是否继承自某一个父类
            print(i.inherits("QWidget"))
    Qobj()

    #

    win = QWidget()
    win.show()
    sys.exit(app.exec_())
