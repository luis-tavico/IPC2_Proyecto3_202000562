from lxml import etree
import xml.etree.ElementTree as ET

class DataBase:

    def __init__(self):
        self.resources = []
        self.categories = []
        self.customers = []
        self.configurations = []
        self.instances = []
        self.consumptions = []
        self.loadData()

    ################################ READ FILE CONFIGURATIONS ################################
    def readConfigurationFile(self, xml_content):
        fileConfigurations = ET.fromstring(xml_content)

        listResources = fileConfigurations.find('listaRecursos')
        if listResources != None:
            for resource in listResources:
                idResource = resource.attrib['id']
                nameResourse = resource.find('nombre').text
                abbreviationResource = resource.find('abreviatura').text
                metricsResource = resource.find('metrica').text
                typeResource = resource.find('tipo').text
                valuexHour = resource.find('valorXhora').text
                self.resources.append({"id":idResource, "nombre":nameResourse, "abreviatura":abbreviationResource,
                "metrica":metricsResource, "tipo":typeResource, "valorXhora":valuexHour})

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
                self.categories.append({"id":idCategory, "nombre":nameCategory, "descripcion":descriptionCategory, "cargaTrabajo":workLoadCategory, "configuraciones":configurations})
        
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
                        idCategory = instance.find('idCategoria').text
                        nameInstance = instance.find('nombre').text
                        dateStart = instance.find('fechaInicio').text
                        state = instance.find('estado').text
                        dateEnd = instance.find('fechaFinal').text
                        instances.append({"id":idInstance, "idCategoria":idCategory, "nombre":nameInstance, "fechaInicio":dateStart, "estado":state, "fechaFinal":dateEnd})
            self.customers.append({"nit": nitCustomer, "nombre": nameCustomer, "direccion": addresCustomer, "correoElectronico": emailCustomer, 
            "usuario": userCustomer, "clave": keyCustomer, "instancias":instances})

        listConsumptions = fileConfigurations.find('listadoConsumos')
        if listConsumptions != None:
            for consumption in listConsumptions:
                idCustomer = consumption.attrib['nitCliente']
                idInstance = consumption.attrib['idInstancia']
                time = consumption.find('tiempo').text
                dateAndHour = consumption.find('fechaHora').text
                self.consumptions.append({"nitCliente":idCustomer, "idInstancia":idInstance,
                                        "tiempo":time, "fechaHora":dateAndHour})

    ################################ READ FILE CONSUMPTIONS ################################
    def readConsumptionFile(self, xml_content):
        listConsumptions = ET.fromstring(xml_content)

        for consumption in listConsumptions:
            idCustomer = consumption.attrib['nitCliente']
            idInstance = consumption.attrib['idInstancia']
            time = consumption.find('tiempo').text
            dateAndHour = consumption.find('fechaHora').text
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
        else:
            database = ET.tostring(ET.Element('database'))
            file_xml = open("./database.xml", "wb")
            file_xml.write(database)  
            file_xml.close()

    ################################ SAVE ################################
    def saveData(self):    
        file_xml = ET.parse("./database.xml")
        database = file_xml.getroot() 

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
            configs = ctg["configuraciones"]
            listConfigurations = ET.SubElement(category, 'listaConfiguraciones')
            for cfg in configs:
                configuration = ET.SubElement(listConfigurations, 'configuracion')
                configuration.set("id", cfg["id"])
                nameConfiguration = ET.SubElement(configuration, 'nombre')
                nameConfiguration.text = cfg["nombre"]
                descriptionConfiguration = ET.SubElement(configuration, 'descripcion')
                descriptionConfiguration.text = cfg["descripcion"]
                resours = cfg["recursos"]
                listResources = ET.SubElement(configuration, 'recursosConfiguracion')
                for rsc in resours:
                    resource = ET.SubElement(listResources, 'recurso')
                    resource.set("id", rsc["id"])
                    resource.text = rsc["cantidad"]
        database.append(listCategories)

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
            instans = ctm["instancias"]
            listaInstances = ET.SubElement(customer, 'listaInstancias')
            for intc in instans:
                instance = ET.SubElement(listaInstances, 'instancia')
                instance.set("id", intc["id"])
                idCategory = ET.SubElement(instance, 'idCategoria')
                idCategory.text = intc["idCategoria"]
                nameInstance = ET.SubElement(instance, 'nombre')
                nameInstance.text = intc["nombre"]
                dateStartInstance = ET.SubElement(instance, 'fechaInicio')
                dateStartInstance.text = intc["fechaInicio"]
                stateInstance = ET.SubElement(instance, 'estado')
                stateInstance.text = intc["estado"]
                dateEndInstance = ET.SubElement(instance, 'fechaFinal')
                dateEndInstance.text = intc["fechaFinal"]
        database.append(listCustomers)

        listConsumptions = ET.Element('listadoConsumos')
        database.append(listConsumptions)

        file_xml.write("./database.xml")

    ################################ RESOURCES ################################
    def newResource(self, rsc):
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
    def newCategory(self, ctg):
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
                self.categories[index] = category
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

    ################################ CUSTOMERS ################################
    def newCustomer(self, ctm):
        for customer in self.customers:
            if customer['id'] == ctm['id']:
                return False
        self.customers.append(ctm)
        return True

    def updateCustomer(self, ctm):
        for customer in self.customers:
            if customer['id'] == ctm["id"]:
                index = self.customers.index(customer)                
                self.customers[index] = ctm
                return True
        return False

    def deleteCustomer(self, id):
        for customer in self.customers:
            if customer['id'] == id:
                index = self.customers.index(customer)
                self.customers.pop(index)
                return True
        return False
                    
    def getCustomers(self):
        return self.customers


"""db = DataBase()
file_xml = etree.parse("Backend/files/archivoConfiguraciones.xml")
content_xml = etree.tostring(file_xml, encoding='utf8', method='xml')
db.readConfigurationFile(content_xml)
print(db.resources)
print(db.categories)
print(db.customers)
file_xml = etree.parse("Backend/files/archivoConsumos.xml")
content_xml = etree.tostring(file_xml, encoding='utf8', method='xml')
db.readConsumptionFile(content_xml)
print(db.consumptions)
db.saveData()"""





#db = DataBase()
#db.loadData()
"""db.readConfigurationFile("files/archivoConfiguraciones.xml")
resource = {"id":"r1", "nombre":"system", "abreviatura":"sys",
                "metrica":"saber", "tipo":"Software", "valorXhora":"30"}
db.newResource(resource)
resource = {"id":"r2", "nombre":"system", "abreviatura":"sys",
                "metrica":"saber", "tipo":"Hardware", "valorXhora":"50"}
db.newResource(resource)
resource = {"id":"r2", "nombre":"system", "abreviatura":"sys",
                "metrica":"saber", "tipo":"Hardware", "valorXhora":"50"}
db.delete(resource)"""



#db = DataBase()
#db.readConsumptionFile(xml_content)
"""def newResource(self, rsc):
    for resource in self.resources:
        if resource['id'] == rsc["id"]:
            return False
    self.resources.append(rsc)
    self.saveNewResource(rsc)
    return True

def saveNewResource(self, rsc):
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

def updateResource(self, rsc):
    for resource in self.resources:
        if resource['id'] == rsc["id"]:
            index = self.resources.index(resource)                
            self.resources[index] = rsc
            self.saveUpdateResource(rsc)
            return True
    return False

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

def deleteResource(self, id):
    for resource in self.resources:
        if resource['id'] == id:
            index = self.resources.index(resource)
            self.saveDeleteResource(id)
            self.resources.pop(index)
            return True
    return False

def saveDeleteResource(self, rsc):
    file_xml = ET.parse(self.pathFileConfigurations)
    fileConfigurations = file_xml.getroot() 

    for listResources in fileConfigurations.findall('listaRecursos'):
        for resource in listResources:
            idResource = resource.attrib['id']
            if idResource == rsc["id"]:
                listResources.remove(resource)

                file_xml.write(self.pathFileConfigurations)
                
def getResources(self):
    return self.resources"""