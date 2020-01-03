from PyQt5.Qt import *

import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('就不给你充电宝')
    window.resize(120,100)
    #window.move(400,400)
    label = QLabel(window)
    label.setText('fgjhdfgjkdfhhdfjhdfhjdfhjdhd')
    label.move(50,50)
    # label.show()
    window.show()
    sys.exit(app.exec_())
    # while True:
    #     pass