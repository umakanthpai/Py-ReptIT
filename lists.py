class Lists:
    def sliceList(self):
        print("------------------------")
        print("Slicing list will create a new list")
        new_list = ['a', 'b', 'c']
        print(new_list[1])
        print(new_list[-2])
        print(new_list[1:3])
        new_list[0] = 'z'
        print(new_list)

    def manipulateList(self):
        print("------------------------")
        my_list = [1, 2, 3]
        bonus = my_list + [5]
        my_list[0] = 'z'
        print(my_list)
        print(bonus)

    def copyList(self):
      cart = ['Laptop', 'Mouse', 'Keyboard']
      cart_copy = cart[:]
      print(cart)
      print(cart_copy)

      # Change cart_copy with out affecting cart 
      cart_copy[0] = 'PC'

      print("------------------")
      print(cart)
      print(cart_copy)

    def methods(self):
      print("------------------")
      alist = ['a', 'b', 'c',4,6,8,4]
      alist.append(100)
      alist.insert(8,33)
      alist.extend(['qq','rr'])
      alist.remove
      print(alist)
      #Using list comprehension remove all 4's
      newlist = [i for i in alist if i != 4]
      print(newlist)

      #Make an unique list using set
      #Observe 4 is occuring only once
      print(list(set(alist)))
      print("------------------")

    def unpacking(self):
      print("------------------")
      a,b,c,*other,d = [1,3,4,5,6,7,8,9]
      print(a)
      print(b)
      print(c)
      print(other)
      print(d)
      print("------------------")



