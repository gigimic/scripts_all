class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()

# Create a class that captures students. Each student has a first name, 
# last name, class year, and major. Create two examples of students.

class students:

  def __init__(self, first, last, year, major):
    self.first = first
    self.last = last
    self.year = year
    self.major = major

  def print_details(self):
    print("student name  :", self.first, self.last)
    print("student year  :", self.year)
    print("student major  :", self.major)

student1 = students('Monica', 'Geller', 1994, "Cooking")
student2 = students('Rachel', 'Green', 1995, "Fashion")

student1.print_details()
student2.print_details()
    
