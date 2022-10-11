class Resource:

    def __init__(self, id, name, abbreviation, metricName, type, numericalValue, quantity):
        self.id = id
        self.name = name
        self.abbreviation = abbreviation
        self.metricName = metricName
        self.type = type
        self.numericalValue = numericalValue
        self.quantity = quantity

    #Methods get

    def getId(self):
        return self.id

    def getName(self):
        return self.name
    
    def getAbbreviation(self):
        return self.abbreviation

    def getMetricName(self):
        return self.metricName

    def getType(self):
        return self.type

    def getNumericalValue(self):
        return self.numericalValue

    def getQuantity(self):
        return self.quantity

    #Methods set

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name
    
    def setAbbreviation(self, abbreviation):
        self.abbreviation = abbreviation

    def setMetricName(self, metricName):
        self.metricName = metricName

    def setType(self, type):
        self.type = type

    def setNumericalValue(self, numericalValue):
        self.numericalValue = numericalValue

    def setQuantity(self, quantity):
        self.quantity = quantity