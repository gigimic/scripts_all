# This class finds the perimeter of the triangle
class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2 
        self.s3 = s3 
    
    def perimeter(self):
        p1 = self.s1 + self.s2+ self.s3
        area = self.s1 * self.s2 /2
        return p1, area

t1 = Triangle(3, 4, 5)
[t, a]=t1.perimeter()
print('perimeter is ', t)
print('area is ', a)
