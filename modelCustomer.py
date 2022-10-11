class Customer:

    def __init__(self, nit, customerName, customerAddress, customerEmail, userName, userKey, instances):
        self.nit = nit
        self.customerName = customerName
        self.customerAddress = customerAddress
        self.customerEmail = customerEmail
        self.userName = userName
        self.userKey = userKey
        self.instances = instances

    #Methods get
    def getNit(self):
        return self.nit

    def getCustomerName(self):
        return self.customerName

    def getCustomerAddress(self):
        return self.customerAddress

    def getCustomerEmail(self):
        return self.customerEmail

    def getUserName(self):
        return self.userName
    
    def getUserKey(self):
        return self.userKey

    def getInstances(self):
        return self.instances

    #Methods set
    def setNit(self, nit):
        self.nit = nit

    def setCustomerName(self, customerName):
        self.customerName = customerName

    def setCustomerAddress(self, customerAddress):
        self.customerAddress = customerAddress

    def setCustomerEmail(self, customerEmail):
        self.customerEmail = customerEmail

    def setUserName(self, userName):
        self.userName = userName
    
    def setUserKey(self, userKey):
        self.userKey = userKey

    def setInstances(self, instances):
        self.instances = instances