class Category:

    def __init__(self, id, name, description, workLoad, configurations):
        self.id = id 
        self.name = name
        self.description = description
        self.workLoad = workLoad
        self.configurations = configurations

    #Methods get

    def getId(self):
        return self.id

    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description

    def getWorkLoad(self):
        return self.workLoad

    def getConfigurations(self):
        return self.configurations

    #Methods set

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name
    
    def setDescription(self, description):
        self.description = description

    def setWorkLoad(self, workLoad):
        self.workLoad = workLoad

    def setConfigurations(self, configurations):
        self.configurations = configurations