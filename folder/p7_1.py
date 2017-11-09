from Rectangle import Rectangle

def main():
    rec1=Rectangle(4,40)
    rec2=Rectangle(3.5,35.7)
    print('The area of the rectangle with width {} units and height {} units is {:.2f} square units.'.format(rec1.width, rec1.height, rec1.getArea()))
    print('The perimeter of the rectangle with width {} units and height {} units is {:.2f} square units.'.format(rec1.width, rec1.height, rec1.getPerimeter()))
    print('The area of the rectangle with width {} units and height {} units is {:.2f} square units.'.format(rec2.width, rec2.height, rec2.getArea()))
    print('The perimeter of the rectangle with width {} units and height {} units is {:.2f} square units.'.format(rec2.width, rec2.height, rec2.getPerimeter()))

main()
