class Configuration:

    def __init__(self, id, name, description, resources):
        self.id = id
        self.name = name
        self.description = description
        self.resources = resources
    
    #Methods get

    def getId(self):
        return self.id

    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description

    def getResources(self):
        return self.resources

    #Methods set

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name
    
    def setDescription(self, description):
        self.description = description

    def setResources(self, resources):
        self.resources = resources