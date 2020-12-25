class Dictry:
# Key needs to be unique,immutable, and hashable
# hence a list can not be used as a key but a tuple can.
  def access(self):
    print("------------------------")
    d1 = {
      'a':1, 
      'b':2,
      'c':[66,77,88],
      'd':True
      }

    print(d1['a'])
    print(d1['c'][1])
    print(d1['d'])
    print(d1.get("b"))
    print(d1.get("z"))
    print(d1.get("z","default"))

    print("------------------------")

  def methods(self):
    print("------------------------")
    d1 = {
      'a':1, 
      'b':2,
      'c':[66,77,88],
      'd':True,
      'age':33
      }
    print("a" in d1.keys())
    print(2 in d1.values())
    print([66,77,88] in d1.values())
    print(d1.items())
    d1.update({'age':44})
    print(d1)
    #copy 
    #clear 
    #pop  
    #popitem 
    #
    print("------------------------")