from lists import Lists
from matrix import Matrix
from dictionaries import Dictry
from basics import Basics
from myFunctions import MyFunctions
from special import Special
from oops import Part,MBPart, FLPart
from dunderMethods import Dunder

#str = "Umakanth Pai"

# Reverse the string
#print(str[::-1])

def aboutLists():
  l1 = Lists()
  l1.sliceList()
  l1.manipulateList()
  l1.copyList()
  l1.methods()
  l1.unpacking()
  l1.listComprehension()

def aboutMatrix():
  m1 = Matrix()
  m1.accessElement()

def aboutDictionary():
  d1 = Dictry()
  d1.access()
  d1.methods()

def aboutBasics():
  b1 = Basics()
  b1.ternary(True)
  b1.ternary(False)
  b1.iterable()
  b1.listUsingRange()
  b1.doEnumerate()
  b1.whileElse()
  b1.whileBreak()
  b1.usePassPlaceholder()
  b1.basicsExercise()
  b1.basicsExerciseDuplicates()

def aboutQuirks():
# Adding custom class documentaion
 #exec(open("myFunctions.py").read())
 #print(globals())

 s1=Special()
 s1.callMutipleArgFunction()
 
 #Function Argument Unpacking
 foo_list = (3, 4) 
 bar_dict = {'y': 3, 'x': 2}  
 s1.point(*foo_list) # Unpacking Lists 
 s1.point(**bar_dict) # Unpacking Dictionaries  

 #Index inside a for loop
 print("\nUsage of enumerate")
 s1.indexInsideForLoop()

def aboutFunctions():
  f1=MyFunctions()
  f1.callHello()
  print(help(MyFunctions.sayHello))
  

def oops():
  #gear = Part("A12345","Gear")
  #engine = Part("A12346","Engine")
  #gear.showPartInfo()
  #engine.showPartInfo()

  gear = Part.createPart("Gear")
  gear.showPartInfo()
  print(" ")
  engine = Part.createPart("Engine")
  engine.showPartInfo()
  print(" ")
  print(Part.generateDisplayPartNumber(gear.partNumber))
  print(" ")
  mbPart = MBPart("889","Wheel")
  #mbPart.showPartInfo()
  print(" ")
  print(isinstance(mbPart,Part))
  print(" ")
  flPart = FLPart("889","Cam")
  #flPart.showPartInfo()
  print("Polymorphism ")
  for part in [mbPart,flPart]:
    part.showPartInfo()
  print(" ")

  print(dir(part))

def aboutDunder():
  d1=Dunder("Mat","44")
  print(str(d1))
  print(d1.__str__())
  d1()
  print(d1["name"])



# Call function about which you want to revise
#aboutQuirks()
#aboutLists()
aboutDunder()

