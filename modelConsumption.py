from numpy import nested_iters


class Consumption:

    def __init__(self, nit, idInstance, time, date):
        self.nit = nit
        self.idInstance = idInstance
        self.time = time
        self.date = date

    #Methods get
    def getNit(self):
        return self.nit
    
    def getIdInstance(self):
        return self.idInstance

    def getTime(self):
        return self.time
    
    def getDate(self):
        return self.date

    #Methods getl
    def setNit(self, nit):
        self.nit = nit
    
    def setIdInstance(self, idInstance):
        self.idInstance = idInstance

    def setTime(self, time):
        self.time = time
    
    def setDate(self, date):
        self.date = date