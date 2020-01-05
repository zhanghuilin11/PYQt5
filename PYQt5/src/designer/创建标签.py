#--Time : 2020/1/5 13:32
#--Author : Zhang
#--File : 创建标签.py

from PyQt5.Qt import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建一个窗口
    win = QWidget()
    win.resize(500,500)

    labl1 = QLabel(win)
    labl2 = QLabel(win)
    labl1.setText('宝贝与描述相符')
    labl2.setText('卖家的服务态度')
    labl2.move(0,20)
    labl3 = QLabel(win)
    labl3.setText('等待删除')
    labl3.move(50,50)
    btn = QPushButton(win)
    btn.setText('下移')
    btn.resize(120,80)
    btn.move(100,200)
    for widget in win.findChildren(QLabel):
        if widget.inherits('QLabel'):
            widget.setStyleSheet('background-color:cyan;')
    btn2 = QPushButton(win)
    btn2.setText('删除标签')
    btn2.move(80,80)
    btn2.clicked.connect(lambda : labl3.deleteLater())
    labl3.destroyed.connect(lambda : print('label3 destory!'))
    win.show()

    sys.exit(app.exec_())
