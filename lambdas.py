from functools import reduce
class Lambdas:

  def doX2Map(self, itemList=[3,4,6,8]):
    print(f"Map input {itemList}")

    # Lambda to multiply be 2
    return list(map(lambda x : x*2,itemList))
    
  def doFilter(self,itemList=[3,4,6,8,9,11]):
    print(f"\n\nFilter input {itemList}")
    
    return list(filter(lambda x : x%2 != 0, itemList))

  def doReduce(self,itemList=[1,3,5,6,7,8]):

    return reduce(lambda acc,item : acc+item ,itemList,10)

  def doExercises(self):
    print("\n\n")
    print(list(map(lambda num: num**2, [1,2,3])))

    a = [(0, 2), (5, 2), (9, 9), (10, -1)]
    a.sort(key=lambda x: x[1])    
    print(a)  