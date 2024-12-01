import Graphics.rectangle
import Graphics.circle
import Graphics.three_Graphics.cuboid
import Graphics.three_Graphics.sphere

# for circle
print "----------Circle Operations----------"
radius=int(raw_input("Enter the radius:"))
print "Area of a circle:",Graphics.circle.findArea(radius)


#for rectangle
print "---------Rectangle Operations---------------"
length=int(raw_input("Enter the length :"))
breadth=int(raw_input("Enter the breadth:"))
print "Rectangle area :",Graphics.rectangle.findArea(length,breadth)
print "Rectangle Perimeter :",Graphics.rectangle.findPerimeter(length,breadth)


#for cuboid
print "---------Cuboid-------"
length=int(raw_input("Enter the length:"))
breadth=int(raw_input("Enter the breadth:"))
height=int(raw_input("Enter the height:"))
print "Area of the cuboid:",Graphics.three_Graphics.cuboid.area(length,breadth,height)
print "Perimeter of the cuboid:",Graphics.three_Graphics.cuboid.perimeter(length,breadth,height)


#for sphere
print "--------Sphere-------"
radius=int(raw_input("Enter the radius:"))
print "Area of a sphere :",Graphics.three_Graphics.sphere.area(radius)
print "Perimeter of a sphere :",Graphics.three_Graphics.sphere.perimeter(radius)


