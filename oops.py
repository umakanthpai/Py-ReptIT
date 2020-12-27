class Part:

  lastNumber = 0

  @staticmethod
  def generatePartNumber(basenumber="A9000100200"):
    Part.lastNumber = Part.lastNumber + 1;
    return basenumber+str(Part.lastNumber)

  def __init__(self, partNumber, nomenclature):
    self.partNumber = partNumber
    self.nomenclature = nomenclature

  def showPartInfo(self):
    print(self.partNumber + " " + self.nomenclature, end="")

  @classmethod
  def createPart(cls,nomenclature):
    return cls(cls.generatePartNumber(),nomenclature)

  @staticmethod
  def generateDisplayPartNumber(partNumber):
    displayPart = []
    counter = 0
    for ch in partNumber:
      counter += 1
      if(counter % 4 == 0):
        displayPart.append(ch)
        displayPart.append(" ")
      else:
        displayPart.append(ch)
    return "".join(displayPart)

class MBPart(Part):
  
  def __init__(self,endNumber,nomenclature):
    partNr = Part.generatePartNumber()
    super().__init__(partNr,nomenclature)
    self.endNumber = endNumber    

  def showPartInfo(self):
    super().showPartInfo()
    print(" MB End Number:" + self.endNumber)

class FLPart(Part):
  def __init__(self,endNumber,nomenclature):
    partNr = Part.generatePartNumber()
    super().__init__(partNr,nomenclature)
    self.endNumber = endNumber    

  def showPartInfo(self):
    super().showPartInfo()
    print(" Freight Liner End Number:" + self.endNumber)
  