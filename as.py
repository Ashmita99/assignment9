class Circle:

    def __init__(self):
        self.radius=3

    def getArea(self):
        area= 3.14*self.radius*self.radius
        print('the area is ',area)
    def getCircumfrence(self):
        cicum=2*3.14*self.radius
        print('the circumfrence is ',cicum)
C=Circle()
C.getArea()
C.getCircumfrence()
