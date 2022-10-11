import xml.etree.ElementTree as ET
from modelCategory import Category
from modelConfiguration import Configuration
from modelResource import Resource
from modelCustomer import Customer

class LoadFile:

    def __init__(self):
        self.categories = []

    def readConfigurationFile(self, path):
        file_xml = ET.parse(path)
        fileConfigurations = file_xml.getroot()

        for listResources in fileConfigurations.findall('listaRecursos'):
            for resource in listResources:
                idResource = resource.attrib['id']
                nameResourse = resource.find('nombre').text
                abbreviationResource = resource.find('abreviatura').text
                metricsResource = resource.find('metrica').text
                typeResource = resource.find('tipo').text
                valuexHour = resource.find('valorXhora').text

        for listCategories in fileConfigurations.findall('listaCategorias'):
            for category in listCategories:
                idCategory = category.attrib['id']
                nameCategory = category.find('nombre').text
                descriptionCategory = category.find('descripcion').text
                workLoadCategory = category.find('cargaTrabajo').text
                newCategory = Category(idCategory, nameCategory, descriptionCategory, workLoadCategory, [])
                for listConfigurations in category.findall('listaConfiguraciones'):
                    for configuration in listConfigurations:
                        idConfiguration = configuration.attrib['id']
                        nameConfiguration = configuration.find('nombre').text
                        descriptionConfiguration = configuration.find('descripcion').text
                        newConfiguration = Configuration(idConfiguration, nameConfiguration, descriptionConfiguration, [])
                        configurations = newCategory.getConfigurations()
                        configurations.append(newConfiguration)
                        for resourcesConfiguration in configuration.findall('recursosConfiguracion'):
                            for resource in resourcesConfiguration:
                                idResource = resource.attrib['id']
                                quantityResource = resourcesConfiguration.find(".//recurso[@id='"+idResource+"']").text
                                resourceInConfiguration = Resource(idResource, None, None, None, None, None, quantityResource)
                self.categories.append(newCategory)

        '''for category in self.categories:
            print(category.getId())
            print(category.getName())
            print(category.getDescription())
            print(category.getWorkLoad())
            configurations = category.getConfigurations()
            for configuration in configurations:
                print(configuration.getId())'''
        
        for customerList in fileConfigurations.findall('listaClientes'):
            for customer in customerList:
                nitCustomer = customer.attrib['nit']
                nameCustomer = customer.find('nombre')
                userCustomer = customer.find('usuario')
                keyCustomer = customer.find('clave')
                direcctionCustomer = customer.find('direccion')
                emailCustomer = customer.find('correoElectronico')
                for listInstances in customer.findall('listaInstancias'):
                    for instance in listInstances:
                        idInstance = instance.attrib['id']
                        idCategory = instance.find('idCategoria')
                        nameInstance = instance.find('nombre')
                        dateStart = instance.find('fechaInicio')
                        state = instance.find('estado')
                        dateEnd = instance.find('fechaFinal')

    def readConsumptionFile(self, path):
        file_xml = ET.parse(path)
        listConsumptions = file_xml.getroot()

        for consumption in listConsumptions:
            idCustomer = consumption.attrib['nitCliente']
            idInstance = consumption.attrib['idInstancia']
            time = consumption.find('tiempo').text
            dateAndHour = consumption.find('fechaHora').text

    '''def reportar(self):
        file_xml = ET.parse("./ArchivoSalida.xml")
        fileConfigurations = file_xml.getroot()

        nombrePaciente = self.paciente.getNombre()
        edadPaciente = str(self.paciente.getEdad())
        periodosPaciente = str(self.paciente.getPeriodos())
        tamañoRejillaPaciente = str(self.paciente.getTamañoRejilla())
        resultadoPaciente = self.paciente.getResultado()
        nPaciente = str(self.paciente.getN())
        n1Paciente = str(self.paciente.getN1())
        paciente = ET.Element('paciente')
        datospersonales = ET.SubElement(paciente, 'datospersonales')
        nombre = ET.SubElement(datospersonales, 'nombre')
        nombre.text = nombrePaciente
        edad = ET.SubElement(datospersonales, 'edad')
        edad.text = edadPaciente
        periodos = ET.SubElement(paciente, 'periodos')
        periodos.text = periodosPaciente
        m = ET.SubElement(paciente, 'm')
        m.text = tamañoRejillaPaciente
        resultado = ET.SubElement(paciente, 'resultado')
        resultado.text = resultadoPaciente
        n = ET.SubElement(paciente, 'n')
        n.text = nPaciente
        n1 = ET.SubElement(paciente, 'n1')
        n1.text = n1Paciente

        pacientes.append(paciente)
        archivo_xml.write("./Datos.xml")'''

object = LoadFile()
object.readConfigurationFile("configurationFile.xml")
#object.readConsumptionFile("consumptionList.xml")