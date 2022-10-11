class Instance:

    def __init__(self, id, idConfiguration, name, dateStart, state, dateEnd):
        self.id = id 
        self.idConfiguration = idConfiguration
        self.name = name
        self.dateStart = dateStart
        self.state = state
        self.dateEnd = dateEnd

    #Methods get
    def getId(self):
        return self.id

    def getIdConfiguration(self):
        return self.idConfiguration

    def getName(self):
        return self.name

    def getDateStart(self):
        return self.dateStart

    def getState(self):
        return self.state
    
    def getDateEnd(self):
        return self.dateEnd

    #Methods set
    def setId(self, id):
        self.id = id

    def setIdConfiguration(self, idConfiguration):
        self.idConfiguration = idConfiguration

    def setName(self, name):
        self.name = name

    def setDateStart(self, dateStart):
        self.dateStart = dateStart

    def setState(self, state):
        self.state = state
    
    def setDateEnd(self, dateEnd):
        self.dateEnd = dateEnd