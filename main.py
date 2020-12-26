from lists import Lists
from matrix import Matrix
from dictionaries import Dictry
from basics import Basics
from myFunctions import MyFunctions
from special import Special
from oops import Part

str = "Umakanth Pai"

# Reverse the string
#print(str[::-1])

l1 = Lists()
#l1.sliceList()
#l1.manipulateList()
#l1.copyList()
#l1.methods()
#l1.unpacking()

m1 = Matrix()
#m1.accessElement()

d1 = Dictry()
#d1.access()
#d1.methods()

b1 = Basics()
#b1.ternary(True)
#b1.ternary(False)
#b1.iterable()
#b1.listUsingRange()
#b1.doEnumerate()
#b1.whileElse()
#b1.whileBreak()
#b1.usePassPlaceholder()
#b1.basicsExercise()
#b1.basicsExerciseDuplicates()

# Adding custom class documentaion
# exec(open("myFunctions.py").read())
# print(globals())

f1=MyFunctions()
#f1.callHello()
#print(help(MyFunctions.sayHello))

s1=Special()
#s1.callMutipleArgFunction()

gear = Part("A12345","Gear")
engine = Part("A12346","Engine")
gear.showPartInfo()
engine.showPartInfo()






