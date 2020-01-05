
'''object的父子关系'''

from PyQt5.Qt import QObject
from PyQt5.Qt import *
object0 = QObject()
object1 = QObject()
object2 = QObject()
object3 = QObject()
object4 = QObject()
object5 = QObject()

object1.setParent(object0) # setParent设置对象的父类
object2.setParent(object0)
object3.setParent(object1)
object4.setParent(object1)
object5.setParent(object2)

print('objext0',object0)
print('objext1',object1)
print('objext2',object2)
print('objext3',object3)
print('objext4',object4)
print('objext5',object5)

print('objext1 parent ',object1.parent()) # object1.parent()返回object1的父类
print('objext5 parent ',object5.parent())

print(object0.findChild(object)) #返回一个子类

object2.setObjectName('b')
print(object0.findChild(object,'b')) #返回一个ObjectName为b的子类

object3.setObjectName('n')
print(object0.findChild(object,'n'))

print(object0.findChild(object,'n', Qt.FindDirectChildrenOnly)) #只查找直接继承的子类

print(object0.findChildren(object))#返回所有子类

#当父类删除时，其子类也被删除，释放内存

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win1 = QWidget()
    win1.resize(500,500)
    win1.show()

    win2 = QWidget()
    win2.resize(200,200)
    win2.setStyleSheet("background-color : cyan;")
    win2.setParent(win1)
    win2.move(100,100)
    win2.show()

    but1 = QPushButton()
    but1.setParent(win1)
    but1.setText('sdsadsdasdsaasddas')
    but1.move(150,150)
    but1.show()

    #信号与槽
    def cao():
        print('xxxxxxxxxxxx')
    but1.clicked.connect(cao)

    def color():

        win2.setStyleSheet("background-color : red;")

    but1.clicked.connect(color)

def odj():
    obj1 = QObject
    obj2 = QObject
    obj3 = QObject
    obj4 = QObject
    obj2.setParent(obj1)
    obj3.setParent(obj2)
    obj4.setParent(obj3)

    def destory(name):
        print(name,' was destiryed!')
    obj1.destroyed.connect(destory)
    obj2.destroyed.connect(destory)
    obj3.destroyed.connect(destory)
    obj4.destroyed.connect(destory)
    



    # def but1_cl(name):
    #     print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqq',name)
    # # object信号的操作
    #
    # obj = QObject()
    #
    # def destory_obj(obj):
    #     print('bei shi fang ')
    #
    # # obj.destroyed.connect(destory_obj())
    # obj.objectNameChanged.connect(but1_cl())
    # obj.setObjectName('sdf')
    # del obj
    # but1.clicked().connect(but1_cl())
    sys.exit(app.exec_())



