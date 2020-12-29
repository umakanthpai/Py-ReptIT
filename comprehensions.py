class Comprehensions:

  #list, set, dictionary
  #quick way to create list, set etc.
  def doCreateList(self):
    lst = [aChar for aChar in "hello"]
    print(lst)

    numLst = [aNr for aNr in range(1,30)]
    print(numLst)

    # Using expression
    numLst = [aNr**2 for aNr in range(1,30)]
    print(numLst)

    # Using condition
    numLst = [aNr**2 for aNr in range(1,30) if aNr % 2 == 0]
    print(numLst)

  def doCreateSet(self):
    print("\n\n----------------------------------\n")
    set1 = {aChar for aChar in "hello"}
    print(set1)

    set2 = {aNr for aNr in range(1,30)}
    print(set2)

    # Using expression
    set3 = {aNr**2 for aNr in range(1,30)}
    print(set3)

    # Using condition
    set4 = {aNr**2 for aNr in range(1,30) if aNr % 2 == 0}
    print(set4)

  def doCreateDictionary(self):
    print("\n\n----------------------------------\n")
    
    di = {'a':1,'b':2,'c':3}
    dctry1={key:value**2 for key,value in di.items()}
    print(dctry1)

    di = {'a':1,'b':2,'c':3}
    dctry1={key:value**2 for key,value in di.items() if value %2 == 0}
    print(dctry1)

    dctry1={num:num*2 for num in [1,2,4,6,7]}
    print(dctry1)

  def doExercises(self):
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

    duplicates = list(set([char for char in some_list if(some_list.count(char) > 1)]))
    print(duplicates)
