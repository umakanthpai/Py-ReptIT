class Basics:
  
  def ternary(self, expand_value):
    print("------------------------")
    is_expand = expand_value
    status = "Processing" if is_expand else "Stopped"

    print(status)
    print("------------------------")

  def iterable(self):
    print("------------------------")
    user = {
      'name' : "Pai",
      'age' : 50,
      'can_code' : True
    }

    for aKey in user:
      print(aKey)
    print(" ")  

    for aValue in user.values():
      print(aValue)
    print(" ")  

    for anItem in user.items():
      print(str(anItem[0]) + "->" + str(anItem[1]))
    
    print(" ")

    print("Better way to do this:")
    for anItem in user.items():
      key,value = anItem
      print(str(key) + "->" + str(value))      
    print(" ")          

    print("Best way to do this:")
    for key,value in user.items():
      print(str(key) + "->" + str(value))      
    print(" ")          

    print("------------------------")

  def listUsingRange(self):
    print("------------------------")
    for _ in range(2):
      print(list(range(10)))    
    print("------------------------")  

  def doEnumerate(self):
    print("------------------------")
    for index,value in enumerate("Umakanth Pai"):
      print (index, value)
    print("------------------------")
    for index,value in enumerate([11,22,33,44,55]):
      print (index, value)
    print("------------------------")

  def whileElse(self):
    print("------------------------")
    i = 0
    while i < 10:
      print(i)
      i += 1
    else:
      print("Wrong condition")
    print("------------------------")

  def whileBreak(self):
    print("------------------------")
    while True:
      response = input("Say Something: ")
      if(response == 'bye'):
        break
    print("------------------------")        

  def usePassPlaceholder(self):
    print("------------------------")
    for i in range(6):
      # Pass is just a place holder with out it error will come 
      # Main idea is you can write a loop and you can code later but
      # need to write pass, so that you do not get any error

      pass

    print("Used Pass in a loop")
    print("------------------------")

  def basicsExercise(self):
    print("------------------------")
    picture = [
      [0,0,0,1,0,0,0],
      [0,0,1,1,1,0,0],
      [0,1,1,1,1,1,0],
      [1,1,1,1,1,1,1],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0]
    ] 

    for aList in picture:
      for anItem in aList:        
        if(anItem == 0):
          print(" ", end="")
        else:
          print("*", end="")  
      print("")
      
    print("------------------------")

  # Determine duplicates and put it in a list
  def basicsExerciseDuplicates(self):
    duplicates = []
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n','c']
    for item in some_list:
      if(some_list.count(item) > 1):
        if(item not in duplicates):
          duplicates.append(item)
    print(duplicates)
