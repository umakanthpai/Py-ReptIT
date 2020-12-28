from functools import reduce

class PureFunctions:
  '''
  Maps by multiplying by 2 and returns the list
  '''
  def doX2Map(self, itemList=[3,4,6,8]):
    print(f"Map input {itemList}")
    def multipy_by_two(item):
      return item*2

    return list(map(multipy_by_two,itemList))
    
  def doFilter(self,itemList=[3,4,6,8,9,11]):
    print(f"\n\nFilter input {itemList}")
    def onlyOdd(item):
      return item % 2 != 0
    
    return list(filter(onlyOdd,itemList))

  def doZip(self,itemList1=[1,2,3,4,5],itemList2=[10,20,30,40]):
    print(f"\n\nzip input {itemList1} {itemList2}")
    
    return list(zip(itemList1,itemList2))

  def doReduce(self,itemList=[1,3,5,6,7,8]):
    def accumulator(acc,item):
      print(f'{acc} {item}')
      return acc+item

    return reduce(accumulator,itemList,10)

  def doExercises(self):
    print("\n\n Exercises")

    #1 Capitalize all of the pet names and print the list
    my_pets = ['sisi', 'bibi', 'titi', 'carla']

    def capitalize(string):
        return string.upper()

    print(list(map(capitalize, my_pets)))
    #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
    my_strings = ['a', 'b', 'c', 'd', 'e']
    my_numbers = [5,4,3,2,1]

    print(list(zip(my_strings, sorted(my_numbers))))


    #3 Filter the scores that pass over 50%
    scores = [73, 20, 65, 19, 76, 100, 88]

    def is_smart_student(score):
        return score > 50

    print(list(filter(is_smart_student, scores)))


    #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
    def accumulator(acc, item):
        return acc + item

    #print(type([4] + my_numbers + scores))
    print(reduce(accumulator, (my_numbers + scores)))


