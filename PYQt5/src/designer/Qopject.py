
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
