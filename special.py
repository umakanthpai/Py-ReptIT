class Special:

  def funcWithAllTypesOfArgs(self,normal_parm,*args,deflt_params=10,**kwargs):
    print("-------------------------")
    print(normal_parm)
    print(args)
    print(deflt_params)
    print(kwargs)
    print("-------------------------")

  def sum_func(self,*args):
    print("-------------------------")
    print("See all the arguments")
    print(*args)
    print(f"Use only args to get tuple {args}")
    print(f"Sum of all arguments {sum(args)}")
    print("-------------------------")

  def sum_func_kwargs(self,**kwargs):
    print("-------------------------")
    print(kwargs)
    total = 0
    for value in kwargs.values():
      total += value 

    print(f'Total from kwargs is {total}')
    print("-------------------------")

  def callMutipleArgFunction(self):
    self.sum_func(2,3,4,5)
    self.sum_func_kwargs(n1=10,n2=20)
    self.funcWithAllTypesOfArgs("normal",[3,4,5],[3,4,5],name1="aaa", name2="bbb")

  def point(self,x, y): 
    print(x,y) 
  
  def indexInsideForLoop(self):
    vowels=['a','e','i','o','u'] 
    for i, letter in enumerate(vowels): 
      print (i, letter)    
