class Student:

  def __init__(self, roll, name):
    if roll > 0:
        self.__roll=roll
    else:
        self.__roll=None
        print("enter correct roll no")
    self.__name=name

  @property
  def roll(self):
    return self.__roll

  @property
  def name(self):
    return self.__name 

  @roll.setter
  def roll(self,roll):
    self.__roll=roll

  @name.setter
  def name(self,name):
    self.__name=name

s1 = Student(11, "sreekar")
print(s1.roll)
print(s1.name)

s1.roll=12
s1.name="Sanju"

print(s1.roll)
print(s1.name)
