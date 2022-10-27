from lxml import etree
import xml.etree.ElementTree as ET
import re
from datetime import datetime

class DataBase:

    def __init__(self):
        self.resources = []
        self.categories = []
        self.customers = []
        self.consumptions = []
        self.bills = []
        self.numberbill = 1000
        self.loadData()

    ################################ READ FILE CONFIGURATIONS ################################
    def readConfigurationFile(self, xml_content):
        quantityResources = 0
        quantityCategories = 0
        quantityConfigurations = 0
        quantityCustomers = 0
        quantityInstances = 0
        fileConfigurations = ET.fromstring(xml_content)

        listResources = fileConfigurations.find('listaRecursos')
        if listResources != None:
            for resource in listResources:
                idResource = resource.attrib['id']
                nameResourse = resource.find('nombre').text
                abbreviationResource = resource.find('abreviatura').text
                metricsResource = resource.find('metrica').text
                typeResource = resource.find('tipo').text.capitalize()
                valuexHour = resource.find('valorXhora').text
                self.resources.append({"id":idResource, "nombre":nameResourse, "abreviatura":abbreviationResource,
                "metrica":metricsResource, "tipo":typeResource, "valorXhora":valuexHour})
                quantityResources += 1

        listCategories = fileConfigurations.find('listaCategorias')
        if listCategories != None:
            for category in listCategories:
                idCategory = category.attrib['id']
                nameCategory = category.find('nombre').text
                descriptionCategory = category.find('descripcion').text
                workLoadCategory = category.find('cargaTrabajo').text
                configurations = []
                for listConfigurations in category.findall('listaConfiguraciones'):
                    for configuration in listConfigurations:
                        idConfiguration = configuration.attrib['id']
                        nameConfiguration = configuration.find('nombre').text
                        descriptionConfiguration = configuration.find('descripcion').text
                        resources = []
                        for resourcesConfiguration in configuration.findall('recursosConfiguracion'):
                            for resource in resourcesConfiguration:
                                idResource = resource.attrib['id']
                                quantityResource = resourcesConfiguration.find(".//recurso[@id='"+idResource+"']").text
                                resources.append({"id":idResource, "cantidad":quantityResource})
                        configurations.append({"id":idConfiguration, "nombre":nameConfiguration, "descripcion":descriptionConfiguration, "recursos":resources})
                        quantityConfigurations += 1
                self.categories.append({"id":idCategory, "nombre":nameCategory, "descripcion":descriptionCategory, "cargaTrabajo":workLoadCategory, "configuraciones":configurations})
                quantityCategories += 1

        customerList = fileConfigurations.find('listaClientes')
        if customerList != None:
            for customer in customerList:
                nitCustomer = customer.attrib['nit']
                nameCustomer = customer.find('nombre').text
                userCustomer = customer.find('usuario').text
                keyCustomer = customer.find('clave').text
                addresCustomer = customer.find('direccion').text
                emailCustomer = customer.find('correoElectronico').text
                instances = []
                for listInstances in customer.findall('listaInstancias'):
                    for instance in listInstances:
                        idInstance = instance.attrib['id']
                        idConfiguration= instance.find('idConfiguracion').text
                        nameInstance = instance.find('nombre').text
                        dateStart = instance.find('fechaInicio').text
                        dateStart = self.extractDate(dateStart)
                        state = instance.find('estado').text.capitalize()
                        dateEnd = instance.find('fechaFinal').text
                        if dateEnd != None:
                            dateEnd = self.extractDate(dateEnd)
                        else:
                            dateEnd = ""
                        instances.append({"id":idInstance, "idConfiguracion":idConfiguration, "nombre":nameInstance, "fechaInicio":dateStart, "estado":state, "facturado":False, "fechaFinal":dateEnd})
                        quantityInstances += 1
                self.customers.append({"nit": nitCustomer, "nombre": nameCustomer, "direccion": addresCustomer, "correoElectronico": emailCustomer, 
                "usuario": userCustomer, "clave": keyCustomer, "instancias":instances})
                quantityCustomers += 1

        listConsumptions = fileConfigurations.find('listadoConsumos')
        if listConsumptions != None:
            for consumption in listConsumptions:
                idCustomer = consumption.attrib['nitCliente']
                idInstance = consumption.attrib['idInstancia']
                time = consumption.find('tiempo').text
                dateAndHour = consumption.find('fechaHora').text
                self.consumptions.append({"nitCliente":idCustomer, "idInstancia":idInstance,
                                        "tiempo":time, "fechaHora":dateAndHour})
        message = str(quantityResources)+" recursos, "+str(quantityCategories)+" categorias, "+str(quantityCustomers)+" clientes, agregados exitosamente"
        return message

    ################################ READ FILE CONSUMPTIONS ################################
    def readConsumptionFile(self, xml_content):
        listConsumptions = ET.fromstring(xml_content)

        for consumption in listConsumptions:
            idCustomer = consumption.attrib['nitCliente']
            idInstance = consumption.attrib['idInstancia']
            time = consumption.find('tiempo').text
            #time = self.convertTime(time)
            dateAndHour = consumption.find('fechaHora').text
            dateAndHour = self.extractDateAndTime(dateAndHour)
            self.consumptions.append({"nitCliente":idCustomer, "idInstancia":idInstance,
                                    "tiempo":time, "fechaHora":dateAndHour})

    ################################ LOAD DATA ################################
    def loadData(self):
        exist = True
        try:
            archivo = open("./database.xml")
            archivo.close()
        except FileNotFoundError:
          exist = False  

        if exist:
            file_xml = etree.parse("./database.xml")
            content_xml = etree.tostring(file_xml, encoding='utf8', method='xml')
            self.readConfigurationFile(content_xml)

    ################################ SAVE ################################
    def saveData(self):   
        database = ET.tostring(ET.Element('database'))
        file_xml = open("./database.xml", "wb")
        file_xml.write(database)  
        file_xml.close() 

        file_xml = ET.parse("./database.xml")
        database = file_xml.getroot() 

        if len(self.resources) > 0:
            listResources = ET.Element('listaRecursos')
            for rsc in self.resources:
                resource = ET.SubElement(listResources, 'recurso')
                resource.set("id", rsc["id"])
                nameResource = ET.SubElement(resource, 'nombre')
                nameResource.text = rsc["nombre"]
                abbreviationResource = ET.SubElement(resource, 'abreviatura')
                abbreviationResource.text = rsc["abreviatura"]
                metricsResource = ET.SubElement(resource, 'metrica')
                metricsResource.text = rsc["metrica"]
                typeResource = ET.SubElement(resource, 'tipo')
                typeResource.text = rsc["tipo"]
                valueResource = ET.SubElement(resource, 'valorXhora')
                valueResource.text = str(rsc["valorXhora"])
            database.append(listResources)

        if len(self.categories) > 0:
            listCategories = ET.Element('listaCategorias')
            for ctg in self.categories:
                category = ET.SubElement(listCategories, 'categoria')
                category.set("id", ctg["id"])
                nameCategory = ET.SubElement(category, 'nombre')
                nameCategory.text = ctg["nombre"]
                descriptionCategory = ET.SubElement(category, 'descripcion')
                descriptionCategory.text = ctg["descripcion"]
                workLoadCategory = ET.SubElement(category, 'cargaTrabajo')
                workLoadCategory.text = ctg["cargaTrabajo"]
                if "configuraciones" in ctg:
                    configs = ctg["configuraciones"]                  
                    listConfigurations = ET.SubElement(category, 'listaConfiguraciones')
                    for cfg in configs:
                        configuration = ET.SubElement(listConfigurations, 'configuracion')
                        configuration.set("id", cfg["id"])
                        nameConfiguration = ET.SubElement(configuration, 'nombre')
                        nameConfiguration.text = cfg["nombre"]
                        descriptionConfiguration = ET.SubElement(configuration, 'descripcion')
                        descriptionConfiguration.text = cfg["descripcion"]
                        if "recursos" in cfg:
                            resours = cfg["recursos"]
                            listResources = ET.SubElement(configuration, 'recursosConfiguracion')
                            for rsc in resours:
                                resource = ET.SubElement(listResources, 'recurso')
                                resource.set("id", rsc["id"])
                                resource.text = rsc["cantidad"]
            database.append(listCategories)

        if len(self.customers) > 0:
            listCustomers = ET.Element('listaClientes')
            for ctm in self.customers:
                customer = ET.SubElement(listCustomers, 'cliente')
                customer.set("nit", ctm["nit"])
                nameCustomer = ET.SubElement(customer, 'nombre')
                nameCustomer.text = ctm["nombre"]
                userCustomer = ET.SubElement(customer, 'usuario')
                userCustomer.text = ctm["usuario"]
                passwordCustomer = ET.SubElement(customer, 'clave')
                passwordCustomer.text = ctm["clave"]
                addresCustomer = ET.SubElement(customer, 'direccion')
                addresCustomer.text = ctm["direccion"]
                emailCustomer = ET.SubElement(customer, 'correoElectronico')
                emailCustomer.text = ctm["correoElectronico"]
                if "instancias" in ctm:
                    instans = ctm["instancias"]
                    listaInstances = ET.SubElement(customer, 'listaInstancias')
                    for intc in instans:
                        instance = ET.SubElement(listaInstances, 'instancia')
                        instance.set("id", intc["id"])
                        idConfiguracion = ET.SubElement(instance, 'idConfiguracion')
                        idConfiguracion.text = intc["idConfiguracion"]
                        nameInstance = ET.SubElement(instance, 'nombre')
                        nameInstance.text = intc["nombre"]
                        dateStartInstance = ET.SubElement(instance, 'fechaInicio')
                        #date = date.strftime("%d/%m/%Y")
                        dateStartInstance.text = intc["fechaInicio"].strftime("%d/%m/%Y")
                        stateInstance = ET.SubElement(instance, 'estado')
                        stateInstance.text = intc["estado"]
                        dateEndInstance = ET.SubElement(instance, 'fechaFinal')
                        if intc["fechaFinal"] != "":
                            dateEndInstance.text = intc["fechaFinal"].strftime("%d/%m/%Y")
                        else:
                            dateEndInstance.text = intc["fechaFinal"]
            database.append(listCustomers)

        if len(self.consumptions) > 0:
            listConsumptions = ET.Element('listadoConsumos')
            for cmpt in self.consumptions:
                consumption = ET.SubElement(listConsumptions, 'consumo')
                consumption.set("nitCliente", cmpt["nitCliente"])
                consumption.set("idInstancia", cmpt["idInstancia"])
                time = ET.SubElement(consumption, 'tiempo')
                time.text = cmpt["tiempo"]
                dateAndHour = ET.SubElement(consumption, 'fechaHora')
                dateAndHour.text = cmpt["fechaHora"].strftime("%d/%m/%Y %H:%M")
            database.append(listConsumptions)

        file_xml.write("./database.xml")

    ################################ RESOURCES ################################
    def createResource(self, rsc):
        for resource in self.resources:
            if resource['id'] == rsc["id"]:
                return False
        self.resources.append(rsc)
        self.saveData()
        return True

    def updateResource(self, rsc):
        for resource in self.resources:
            if resource['id'] == rsc["id"]:
                index = self.resources.index(resource)                
                self.resources[index] = rsc
                self.saveData()
                return True
        return False

    def deleteResource(self, id):
        for resource in self.resources:
            if resource['id'] == id:
                index = self.resources.index(resource)
                self.resources.pop(index)
                self.saveData()
                return True
        return False
                    
    def getResources(self):
        return self.resources

   ################################ CATEGORIES ################################
    def createCategory(self, ctg):
        for category in self.categories:
            if category['id'] == ctg['id']:
                return False
        self.categories.append(ctg)
        self.saveData()
        return True

    def updateCategory(self, ctg):
        for category in self.categories:
            if category['id'] == ctg["id"]:
                index = self.categories.index(category)                
                self.categories[index] = ctg
                self.saveData()
                return True
        return False

    def deleteCategory(self, id):
        for category in self.categories:
            if category['id'] == id:
                index = self.categories.index(category)
                self.categories.pop(index)
                self.saveData()
                return True
        return False
                    
    def getCategories(self):
        return self.categories

   ################################ CONFIGURATIONS ################################
    def createConfiguration(self, cnf, idCategory):
        for category in self.categories:
            if category['id'] == idCategory:
                if not ("configuraciones" in category):
                    category['configuraciones'] = []
                configurations = category["configuraciones"]
                configurations.append(cnf)
                self.saveData()     
                return True
        return False              
        
    def updateConfiguration(self, cnf, idCategory):
        for category in self.categories:
            if category['id'] == idCategory:
                configurations = category["configuraciones"]
                for configuration in configurations:
                    if configuration['id'] == cnf['id']:
                        index = configurations.index(configuration)                
                        configurations[index] = cnf
                        self.saveData()     
                        return True
        return False         

    def deleteConfiguration(self, idConfiguration, idCategory):
        for category in self.categories:
            if category['id'] == idCategory:
                configurations = category["configuraciones"]
                for configuration in configurations:
                    if configuration['id'] == idConfiguration:
                        index = configurations.index(configuration)                
                        configurations.pop(index)
                        self.saveData()     
                        return True
        return False         
                    
    def getConfigurations(self, idCategory):
        for category in self.categories:
            if category['id'] == idCategory:
                if not ("configuraciones" in category):
                    return []
                configurations = category["configuraciones"]
                return configurations        

   ################################ RESOURCES IN CATEGORIES ################################
    def addResourceInConfiguration(self, idCategory, idConfiguration, rsc):
        for category in self.categories:
            if category['id'] == idCategory:
                configurations = category["configuraciones"]
                for configuration in configurations:
                    if configuration['id'] == idConfiguration:
                        if not ("recursos" in configuration):
                            configuration['recursos'] = []
                        resources = configuration["recursos"]
                        resources.append(rsc)
                        self.saveData()     
                        return True
        return False              
        
    def updateResourceInConfiguration(self, idCategory, idConfiguration, rsc):
        for category in self.categories:
            if category['id'] == idCategory:
                configurations = category["configuraciones"]
                for configuration in configurations:
                    if configuration['id'] == idConfiguration:
                        resources = configuration["recursos"]
                        for resource in resources:
                            if resource['id'] == rsc['id']:
                                index = resources.index(resource)                
                                resources.pop(index)
                                self.saveData()     
                                return True
        return False     

    def deleteResourceInConfiguration(self, idCategory, idConfiguration, idResource):
        for category in self.categories:
            if category['id'] == idCategory:
                configurations = category["configuraciones"]
                for configuration in configurations:
                    if configuration['id'] == idConfiguration:
                        resources = configuration["instancias"]
                        for resource in resources:
                            if resource['id'] == idResource:
                                index = resources.index(resource)                
                                resources.pop(index)
                                self.saveData()     
                                return True
        return False          
                    
    def getResourcesInConfiguration(self, idCategory, idConfiguration):
        for category in self.categories:
            if category['id'] == idCategory:
                configurations = category["configuraciones"]
                for configuration in configurations:
                    if configuration['id'] == idConfiguration:
                        if not ("recursos" in configuration):
                            return []
                        resources = configuration["recursos"]
                        return resources     
                        
    ################################ CUSTOMERS ################################
    def createCustomer(self, ctm):
        for customer in self.customers:
            if customer['nit'] == ctm['nit']:
                return False
        self.customers.append(ctm)
        self.saveData()   
        return True

    def updateCustomer(self, ctm):
        for customer in self.customers:
            if customer['nit'] == ctm["nit"]:
                index = self.customers.index(customer)                
                self.customers[index] = ctm
                self.saveData()   
                return True
        return False

    def deleteCustomer(self, nit):
        for customer in self.customers:
            if customer['nit'] == nit:
                index = self.customers.index(customer)
                self.customers.pop(index)
                self.saveData()   
                return True
        return False
                    
    def getCustomers(self):
        return self.customers

################################ INSTANCES ################################
    def createInstance(self, inst, nitCustomer):
        for customer in self.customers:
            if customer['nit'] == nitCustomer:
                if not ("instancias" in customer):
                    customer['instancias'] = []
                instances = customer["instancias"]
                inst["facturado"]=False
                instances.append(inst)
                self.saveData()     
                return True
        return False              
        
    def updateInstance(self, inst, nitCustomer):
        for customer in self.customers:
            if customer['nit'] == nitCustomer:
                instances = customer["instancias"]
                for instance in instances:
                    if instance['id'] == inst['id']:
                        index = instances.index(instance)
                        inst["facturado"]=False          
                        instances[index] = inst
                        self.saveData()     
                        return True
        return False     

    def deleteInstance(self, nitCustomer, idInstance):
        for customer in self.customers:
            if customer['nit'] == nitCustomer:
                instances = customer["instancias"]
                for instance in instances:
                    if instance['id'] == idInstance:
                        index = instances.index(instance)                
                        instances.pop(index)
                        self.saveData()     
                        return True
        return False         
                    
    def getInstances(self, nitCustomer):
        for customer in self.customers:
            if customer['nit'] == nitCustomer:
                if not ("instancias" in customer):
                    return []
                instances = customer["instancias"]
                return instances    

################################ CONSUMPTIONS ################################        
    def getConsumptions(self):
        return self.consumptions  

################################ BILLS ################################  
    #instance["facturado"] = True
    #self.saveData()
    def generateInvoice(self, dateStart, dateEnd):     
        for consumption in self.consumptions:
            resourcesConsumed = []
            nitCustomer = consumption["nitCliente"]
            idInstance = consumption["idInstancia"]
            for customer in self.customers:
                if customer["nit"] == nitCustomer:
                    instances = customer["instancias"]
                    for instance in instances:  
                        if instance["id"] == idInstance:
                            print(instance["facturado"])
                            if instance["facturado"] == False:
                                if instance["estado"] == "Cancelada":    
                                    if instance["fechaInicio"] >= dateStart and instance["fechaFinal"] <= dateEnd:
                                        for category in self.categories:
                                            configurations = category["configuraciones"]
                                            for configuration in configurations:
                                                if configuration["id"] == instance["idConfiguracion"]:
                                                    resourcesInConfiguration = configuration["recursos"]
                                                    for resourceInConfiguration in resourcesInConfiguration:
                                                        for resource in self.resources:
                                                            if resource["id"] == resourceInConfiguration["id"]:
                                                                resourcesConsumed.append([{"idRecurso":resource["id"], "nombre":resource["nombre"], "valorXhora":resource["valorXhora"], "cantidad":resourceInConfiguration["cantidad"], "tiempo":consumption["tiempo"]}])
                                                                break
                                                    break                                                       
                                else:
                                    if instance["fechaInicio"] >= dateStart and instance["fechaInicio"] <= dateEnd:                                       
                                        for category in self.categories:
                                            configurations = category["configuraciones"]
                                            for configuration in configurations:
                                                if configuration["id"] == instance["idConfiguracion"]:
                                                    resourcesInConfiguration = configuration["recursos"]
                                                    for resourceInConfiguration in resourcesInConfiguration:
                                                        for resource in self.resources:
                                                            if resource["id"] == resourceInConfiguration["id"]:
                                                                resourcesConsumed.append([{"idRecurso":resource["id"], "nombre":resource["nombre"], "valorXhora":resource["valorXhora"], "cantidad":resourceInConfiguration["cantidad"], "tiempo":consumption["tiempo"]}])
                                                                break
                                                    break
                            break
                    break
            self.numberbill += 1
            number = "F-"+str(self.numberbill)
            bill = {"numero":number, "nitCliente":nitCustomer, "idInstancia":idInstance, "fecha":dateEnd, "consumos":resourcesConsumed}
            self.bills.append(bill)
        print(self.bills)
        return True

    def getBills(self):
        return self.bills

################################ FUNCTIONS ################################  
    def extractDate(self, text):
        date = re.findall(r'(\d{2})/(\d{2})/(\d{4})', text)
        if len(date) > 0:
            date = date[0]
            date = '/'.join(date)
            date = datetime.strptime(date, '%d/%m/%Y').date()
        return date

    def extractDateAndTime(self, text):
        date = re.findall(r'(\d{2})/(\d{2})/(\d{4})', text)
        hour = re.findall(r'(\d{2}):(\d{2})', text)

        if len(date) > 0:
            date = date[0]
            date = '/'.join(date)
        if len(hour) > 0:
            hour = hour[0]
            hour = ':'.join(hour)
        
        if hour.__class__ == str:
            timeAndDate = date+" "+hour
            timeAndDate = datetime.strptime(timeAndDate, '%d/%m/%Y %H:%M')
        else:
            timeAndDate = date
            timeAndDate = datetime.strptime(timeAndDate, '%d/%m/%Y').date()
        return timeAndDate

    def convertTime(self, time):
        hour = "0"
        minute = "0"
        if "." in time:
            hour = int(time[:time.index(".")])
            minute = int(time[time.index(".")+1:])
        else:
            hour = time

        minute = int(int(minute)*0.6)
        time = ""
        if int(hour) == 0: time += ""
        elif int(hour) == 1: time += str(hour)+" hora "
        else: time += str(hour)+" horas "
        if int(minute) == 0: time += ""
        elif int(minute) < 2: time += str(hour)+" minuto "
        else: time += str(minute)+" minutos "

        return time





"""def saveNewResource(self, rsc):
    file_xml = ET.parse("./database.xml")
    database = file_xml.getroot() 

    listResources = database.find('listaRecursos')
    if listResources == None:
        listResources = ET.Element('listaRecursos')
        database.append(listResources)

    resource = ET.SubElement(listResources, 'recurso')
    resource.set("id", rsc["id"])
    nameResource = ET.SubElement(resource, 'nombre')
    nameResource.text = rsc["nombre"]
    abbreviationResource = ET.SubElement(resource, 'abreviatura')
    abbreviationResource.text = rsc["abreviatura"]
    metricsResource = ET.SubElement(resource, 'metrica')
    metricsResource.text = rsc["metrica"]
    typeResource = ET.SubElement(resource, 'tipo')
    typeResource.text = rsc["tipo"]
    valueResource = ET.SubElement(resource, 'valorXhora')
    valueResource.text = str(rsc["valorXhora"])

    file_xml.write("./database.xml")

def saveUpdateResource(self, rsc):
    file_xml = ET.parse("./database.xml")
    database = file_xml.getroot() 

    for listResources in database.findall('listaRecursos'):
        for resource in listResources:
            idResource = resource.attrib['id']
            if idResource == rsc["id"]:
                nameResource = resource.find('nombre')
                nameResource.text = rsc["nombre"]
                abbreviationResource = resource.find('abreviatura')
                abbreviationResource.text = rsc["abreviatura"]
                metricsResource = resource.find('metrica')
                metricsResource.text = rsc["metrica"]
                typeResource = resource.find('tipo')
                typeResource.text = rsc["tipo"]
                valueResource = resource.find('valorXhora')
                valueResource.text = rsc["valorXhora"]

                file_xml.write(self.pathFileConfigurations)

def saveDeleteResource(self, rsc):
    file_xml = ET.parse(self.pathFileConfigurations)
    fileConfigurations = file_xml.getroot() 

    for listResources in fileConfigurations.findall('listaRecursos'):
        for resource in listResources:
            idResource = resource.attrib['id']
            if idResource == rsc["id"]:
                listResources.remove(resource)

                file_xml.write(self.pathFileConfigurations)"""