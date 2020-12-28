class Dunder:

  def __init__(self,name,age):
    
    self.name=name
    self.age=age
    self.map = {"name":name,"age":age}

  def __str__(self):
    print("Override __str__ like toString in Java")
    return f'name is {self.name} and age is {self.age}'

  def __call__(self):
    print("\n__call__ invoked. Object used like a function call\n")

  def __getitem__(self, key):
    print("accessing fields like list or dictionaries")
    return self.map[key]