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
