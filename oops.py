class Part:

  def __init__(self, partNumber, nomenclature):
    self.partNumber = partNumber
    self.nomenclature = nomenclature

  def showPartInfo(self):
    print(self.partNumber + " " + self.nomenclature)

