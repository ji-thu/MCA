class Rectangle:
    def __init__(self, length, breadth):
       
        self.length = length
        self.breadth = breadth

    def area(self):
        
        return self.length * self.breadth

    def perimeter(self):
       
        return 2 * (self.length + self.breadth)

    def compare_area(self, other):
        
        if self.area() > other.area():
            return "First rectangle has a larger area."
        elif self.area() < other.area():
            return "Second rectangle has a larger area."
        else:
            return "Both rectangles have the same area."



rect1 = Rectangle(4, 5)  
rect2 = Rectangle(6, 3) 

print(rect1.compare_area(rect2)) 
