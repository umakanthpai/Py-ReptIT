class MyFunctions:

  
  def sayHello(self,name,emoji):
    '''
    Prints hello string using the provided arguments
    '''
    print(f'Hello {name}  {emoji}')

  # Method with default arguments
  def sayHello2(self,name="Billu",emoji=":("):
    print(f'Hello {name}  {emoji}')
  

  def callHello(self):
    help(self.sayHello)
    '''
    Call hello in different ways
    '''

    # Postional arguments
    print("Called with positional arguments")
    self.sayHello("Pai", ":)")
    print(" ")

    # keyword arguments
    print("Called with keyword arguments")
    self.sayHello(name="Neel Pai", emoji=":)")
    self.sayHello( emoji=":)", name="Anita Pai")
    print(" ")

    # Default arguments
    print("Called with default arguments")
    self.sayHello2()
    print(" ")
