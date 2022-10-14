import xml.etree.ElementTree as ET

class DataBase:

    def __init__(self):
        self.pathFileConfigurations = ""
        self.pathFileConsumptions = ""
        self.resources = []
        self.categories = []
        self.configurations = []
        self.instances = []
        self.customers = []

    def readConfigurationFile(self, path):
        self.pathFileConfigurations = path
        file_xml = ET.parse(self.pathFileConfigurations)
        fileConfigurations = file_xml.getroot()

        for listResources in fileConfigurations.findall('listaRecursos'):
            for resource in listResources:
                idResource = resource.attrib['id']
                nameResourse = resource.find('nombre').text
                abbreviationResource = resource.find('abreviatura').text
                metricsResource = resource.find('metrica').text
                typeResource = resource.find('tipo').text
                valuexHour = resource.find('valorXhora').text
                self.resources.append({"id":idResource, "nombre":nameResourse, "abreviatura":abbreviationResource,
                "metrica":metricsResource, "tipo":typeResource, "valorXhora":valuexHour})

        for listCategories in fileConfigurations.findall('listaCategorias'):
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
        
        for customerList in fileConfigurations.findall('listaClientes'):
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
            self.customers.append({"nit": nitCustomer, "nombre": nameCustomer, "direccion": addresCustomer, "correo electronico": emailCustomer, 
            "usuario": userCustomer, "clave": keyCustomer, "instancias":instances})

    def readConsumptionFile(self, path):
        self.pathFileConsumptions = path
        file_xml = ET.parse(self.pathFileConsumptions)
        listConsumptions = file_xml.getroot()

        for consumption in listConsumptions:
            idCustomer = consumption.attrib['nitCliente']
            idInstance = consumption.attrib['idInstancia']
            time = consumption.find('tiempo').text
            dateAndHour = consumption.find('fechaHora').text

    def saveChangesInFileConfigurations(self, rsc):
        file_xml = ET.parse(self.pathFileConfigurations)
        fileConfigurations = file_xml.getroot() 

        listResources = fileConfigurations.find('listaRecursos')

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

        #listResources.append(resource)

        file_xml.write(self.pathFileConfigurations)

    def edit(self, rsc):
        file_xml = ET.parse(self.pathFileConfigurations)
        fileConfigurations = file_xml.getroot() 

        for listResources in fileConfigurations.findall('listaRecursos'):
            for resource in listResources:
                idResource = resource.attrib['id']
                if idResource == rsc["id"]:
                    nameResource = resource.find('nombre')
                    nameResource.text = rsc["nombre"]
                    #nameResource.set("nombre", rsc["nombre"])
                    """abbreviationResource = ET.SubElement(resource, 'abreviatura')
                    abbreviationResource.text = rsc["abreviatura"]
                    metricsResource = ET.SubElement(resource, 'metrica')
                    metricsResource.text = rsc["metrica"]
                    typeResource = ET.SubElement(resource, 'tipo')
                    typeResource.text = rsc["tipo"]
                    valueResource = ET.SubElement(resource, 'valorXhora')
                    valueResource.text = str(rsc["valorXhora"])"""

                    file_xml.write(self.pathFileConfigurations)

    def delete(self, rsc):
        file_xml = ET.parse(self.pathFileConfigurations)
        fileConfigurations = file_xml.getroot() 

        for listResources in fileConfigurations.findall('listaRecursos'):
            for resource in listResources:
                idResource = resource.attrib['id']
                if idResource == rsc["id"]:
                    listResources.remove(resource)

                    file_xml.write(self.pathFileConfigurations)


    def newResource(self, rsc):
        for resource in self.resources:
            if resource['id'] == id:
                return False
        self.resources.append(rsc)
        self.saveChangesInFileConfigurations(rsc)
        return True

    def getResources(self):
        return self.resources

    def updateResource(self, rsc):
        for resource in self.resources:
            if resource['id'] == rsc["id"]:
                index = self.resources.index(resource)                
                self.resources[index] = (rsc)
                return True
        return False

    def deleteResource(self, id):
        for resource in self.resources:
            if resource['id'] == id:
                index = self.resources.index(resource)
                self.resources.pop(index)
                return True
        return False

#db.readConsumptionFile("consumptionList.xml")
"""db = DataBase()
db.readConfigurationFile("files/archivoConfiguraciones.xml")
resource = {"id":"r1", "nombre":"system", "abreviatura":"sys",
                "metrica":"saber", "tipo":"Software", "valorXhora":"30"}
db.newResource(resource)
resource = {"id":"r2", "nombre":"system", "abreviatura":"sys",
                "metrica":"saber", "tipo":"Hardware", "valorXhora":"50"}
db.newResource(resource)
resource = {"id":"r2", "nombre":"system", "abreviatura":"sys",
                "metrica":"saber", "tipo":"Hardware", "valorXhora":"50"}
db.delete(resource)"""