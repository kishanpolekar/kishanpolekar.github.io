import abc,math,os

class Shape:

    @abc.abstractmethod
    def getArea(self):
        return NotImplementedError('Method getArea not implemented!!\n')

    @abc.abstractmethod
    def getPerimeter(self):
        return NotImplementedError('Method getPerimeter not implemented!!\n')

class Triangle(Shape):
    def __init__(self):
        print('TRIANGLE\n')
        self.s=float(input('Enter the side length of the triangle: '))

    def getArea(self):
        return ('\nThe area of the triangle with side length {} units is {:.2f} square units.\n'.format(self.s, (math.sqrt(3)/4)*(self.s**2)))

    def getPerimeter(self):
        return ('The perimeter of the triangle with side length {} units is {:.2f} units.\n'.format(self.s, self.s*3))

class Square(Shape):
    def __init__(self):
        print('SQUARE\n')
        self.s=float(input('Enter the side length of the square: '))

    def getArea(self):
        return ('\nThe area of the square with side length {} units is {:.2f} square units.\n'.format(self.s, self.s**2))

    def getPerimeter(self):
        return ('The perimeter of the square with side length {} units is {:.2f} units.\n'.format(self.s, self.s*4))

class Rectangle(Shape):
    def __init__(self):
        print('RECTANGLE\n')
        self.l=float(input('Enter the length of the rectangle: '))
        self.b=float(input('Enter the breadth of the rectangle: '))

    def getArea(self):
        return ('\nThe area of the rectangle with length {} units and breadth {} units is {:.2f} square units.\n'.format(self.l, self.b, self.l*self.b))

    def getPerimeter(self):
        return ('The perimeter of the rectangle with length {} units and breadth {} units is {:.2f} units.\n'.format(self.l, self.b, 2*(self.l+self.b)))

class Circle(Shape):
    def __init__(self):
        print('CIRCLE\n')
        self.r=float(input('Enter the radius of the circle: '))

    def getArea(self):
        return ('\nThe area of the circle with radius {} units is {:.2f} square units.\n'.format(self.r, math.pi*(self.r**2)))

    def getPerimeter(self):
        return ('The perimeter (circumference) of the circle with radius {} units is {:.2f} units.\n'.format(self.r, math.pi*self.r*2))

class Polygon(Shape):
    def __init__(self):
        print(('POLYGON\n'))
        self.n=int(input('Enter the number of sides in the regular polygon: '))
        self.s=float(input('Enter the side length: '))

    def getArea(self):
        a=self.s/(2*math.tan(math.radians(180/self.n)))
        return ('\nThe area of the regular polygon with side length {} units having {} sides is {:.2f} square units.\n'.format(self.s, self.n, (a*self.s*self.n)/2))

    def getPerimeter(self):
        return ('The perimeter of the regular polygon with side length {} units having {} sides is {:.2f} units.\n'.format(self.s, self.n, self.s*self.n))

def main():
    choice='Y'
    while choice.lower()=='y':
        os.system('clear')
        print('SHAPES!\n\n1-Triangle\n2-Square\n3-Rectangle\n4-Circle\n5-Any regular polygon with \'n\' sides\n')
        ch=int(input('Enter your choice: '))
        os.system('clear')
        if ch==1:
            t=Triangle()
            print(t.getArea(),t.getPerimeter(),sep='')
        elif ch==2:
            s=Square()
            print(s.getArea(),s.getPerimeter(),sep='')
        elif ch==3:
            r=Rectangle()
            print(r.getArea(),r.getPerimeter(),sep='')
        elif ch==4:
            c=Circle()
            print(c.getArea(),c.getPerimeter(),sep='')
        elif ch==5:
            p=Polygon()
            print(p.getArea(),p.getPerimeter(),sep='')
        else:
            print('\nWrong Choice!!\n')
        choice=input('\nDo you want to make another calculation? (y/n): ')
main()
