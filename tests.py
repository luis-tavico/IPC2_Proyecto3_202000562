from modelResource import Resource
from modelCategory import Category
from modelConfiguration import Configuration
from modelCustomer import Customer

resources = []
resources.append(Resource("r1", "system", "sys", "saber", "Software", 10, 2))
configurations = []
configurations.append(Configuration("c1", "config1", "configuration1", resources))
categories = []
categories.append(Category("a1", "ctg1", "dsc1", "carga1", configurations))
#categories.append(Category("a2", "ctg2", "dsc2", "carga2","configuracion2"))
custumers = []
custumers.append(Customer("21349", "Juan", "20 calle zona 1", "juan@email.com", "jn", "123", None))

def get_category():
    tmp = []
    cnf = []
    rsc = []
    for category in categories:
        tmp.append({"id": category.getId(), "nombre": category.getName(), "descripcion": category.getDescription(),
        "carga trabajo": category.getWorkLoad(), "configuraciones": cnf})
        configurations = category.getConfigurations()
        for configuration in configurations:
            cnf.append({"id": configuration.getId(), "nombre": configuration.getName(), "descripcion": configuration.getDescription(), 
            "recursos": rsc})
            resources = configuration.getResources()
            for resource in resources:
                rsc.append({"id": resource.getId(), "cantidad": resource.getQuantity()})
    return tmp

print(get_category())


