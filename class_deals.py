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


# Create a class that captures planets. Each planet has a name, 
# a distance from the sun, and its gravity relative to Earth’s gravity. 
# For distance and gravity, use the type double which captures real numbers. 
# Make objects for Earth and your favorite non-earth planet.

class planets:

  def __init__(self, name, distance, gravity):
    self.name = name
    self.distance = distance
    self.gravity = gravity

  def planet_details(self):
    print('{}  is  {}  relative distance from the SUN'.format(self.name, self.distance))

planet1 = planets('Mercury', 0.3, 0.5)
planet2 = planets('Venus', 0.6, 0.7)
planet3 = planets('Earth', 1, 1)
planet5 = planets('Jupiter', 2, 9)

planet3.planet_details()
planet5.planet_details()

# Create classes that capture bank customers and bank accounts. A customer has a first and last name. 
# An account has a customer and a balance. Make objects for two accounts held by the same customer.

class customer:
  def __init__(self, name):
    self.name = name

class account:
  def __init__(self, customer.name, balance):
    self.name = customer.name
    self.balance = balance

  def acc_details(self):
    print('balance of {} is {}'.format(self.name, self.balance))


  customer1 = customer('Chandler')
  account1 = account(customer1.name, 1000)
  account.acc_details()

