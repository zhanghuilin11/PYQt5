# --Time : 2020/1/4 15:23
# --Author : Zhang
# --File : classTest.py
class dog():
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def setdog(self, na, co):
        self.name = na
        self.color = co

    def seedog(self):
        print('dogs color is ', self.color)
        print('dogs name is ', self.name)


dog1 = dog('as', 'sdf')

dog1.seedog()
dog1.setdog('jack', 'green')

print('+++++++++++++++++++++++++++++++++++')

dog1.seedog()
