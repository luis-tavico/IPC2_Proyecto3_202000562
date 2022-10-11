from flask import Flask, request, jsonify
from flask_cors import CORS
from modelResource import Resource
from modelCategory import Category
from modelConfiguration import Configuration
from modelCustomer import Customer

app = Flask(__name__)
CORS(app)

resources = []
resources.append(Resource("r1", "system", "sys", "saber", "Software", 10, 2))
configurations = []
configurations.append(Configuration("c1", "config1", "configuration1", resources))
categories = []
categories.append(Category("a1", "ctg1", "dsc1", "carga1", configurations))
#categories.append(Category("a2", "ctg2", "dsc2", "carga2","configuracion2"))
customers = []
customers.append(Customer("21349", "Juan", "20 calle zona 1", "juan@email.com", "jn", "123", None))

@app.route("/categoria", methods=["POST"])
def create_category():
    data = request.get_json()
    id = data["id"]
    name = data["nombre"]
    description = data["descripcion"]
    workLoad = data["cargaTrabajo"]
    configurations = data["configuraciones"]
    for category in categories:
        if category.getId() == id:
            return jsonify({"mensaje": "Categoria repetida"}), 400
    categories.append(Category(id, name, description, workLoad, configurations))
    return jsonify(request.get_json()), 201

@app.route("/categoria", methods=["GET"])
def get_category():
    tmp = []
    cnf = []
    rsc = []
    for category in categories:
        tmp.append({"id": category.getId(), "nombre": category.getName(), "descripcion": category.getDescription(),
        "carga trabajo": category.getWorkLoad(), "configuraciones": cnf})
        for configuration in configurations:
            cnf.append({"id": configuration.getId(), "nombre": configuration.getName(), "descripcion": configuration.getDescription(), 
            "recursos": rsc})
            resources = configuration.getResources()
            for resource in resources:
                rsc.append({"id": resource.getId(), "cantidad": resource.getQuantity()})
    return jsonify(tmp), 200

@app.route("/categoria", methods=["PUT"])
def update_category():
    #data = request.args.get("id")
    data = request.get_json()
    id = data["id"]
    name = data["nombre"]
    description = data["descripcion"]
    workLoad = data["cargaTrabajo"]
    configurations = data["configuraciones"]
    for category in categories:
        if category.getId() == id:
            category.setName(name)
            category.setDescription(description)
            category.setWorkLoad(workLoad)
            category.setConfigurations(configurations)
    return jsonify({"mensaje": "Categoria actualizada"}), 200

@app.route("/categoria", methods=["DELETE"])
def delete_category():
    data = request.get_json()
    id = data["id"]
    for category in categories:
        if category.getId() == id:
            categories.remove(category)
    return jsonify({"mensaje": "Categoria eliminada"}), 200

@app.route("/recurso", methods=["POST"])
def create_resource():
    data = request.get_json()
    id = data["id"]
    name = data["nombre"]
    abbreviation = data["abreviatura"]
    metric = data["metrica"]
    type = data["tipo"]
    value = data["valorXhora"]
    for resource in resources:
        if resource.getId() == id:
            return jsonify({"mensaje": "Recurso repetido"}), 400
    categories.append(Category(id, name, abbreviation, metric, type, value))
    return jsonify(request.get_json()), 201

@app.route("/recurso", methods=["GET"])
def get_resource():
    tmp = []
    for resource in resources:
        tmp.append({"id": resource.getId(), "nombre": resource.getName(), "abreviatura": resource.getAbbreviation(),
        "metrica": resource.getMetricName(), "tipo": resource.getType(), "valorXhora": resource.getNumericalValue()})
    return jsonify(tmp), 200

@app.route("/recurso", methods=["PUT"])
def update_update():
    #data = request.args.get("id")
    data = request.get_json()
    id = data["id"]
    name = data["nombre"]
    abbreviation = data["abreviatura"]
    metric = data["metrica"]
    type = data["tipo"]
    value = data["valorXhora"]
    for resource in resources:
        if resource.getId() == id:
            resource.setName(name)
            resource.setAbbreviation(abbreviation)
            resource.setMetricName(metric)
            resource.setType(type)
            resource.setNumericalValue(value)
    return jsonify({"mensaje": "Recurso actualizado"}), 200

@app.route("/recurso", methods=["DELETE"])
def delete_resource():
    data = request.get_json()
    id = data["id"]
    for resource in resources:
        if resource.getId() == id:
            resources.remove(resource)
    return jsonify({"mensaje": "Recurso eliminada"}), 200

@app.route("/cliente", methods=["POST"])
def create_customer():
    data = request.get_json()
    nit = data["nit"]
    name = data["nombre"]
    user = data["usuario"]
    password = data["clave"]
    address = data["direccion"]
    email = data["correoElectronico"]
    for customer in customers:
        if customer.getNit() == nit:
            return jsonify({"mensaje": "Cliente repetido"}), 400
    customers.append(Customer(nit, name, address, email, user, password, None))
    return jsonify(request.get_json()), 201

@app.route("/cliente", methods=["GET"])
def get_customer():
    tmp = []
    cnf = []
    for customer in customers:
        tmp.append({"nit": customer.getNit(), "nombre": customer.getCustomerName(), "direccion": customer.getCustomerAddress(),
        "correo electronico": customer.getCustomerEmail(), "usuario": customer.getUserName(), "clave": customer.getUserKey()})
        #instances = customer.getInstances()
        #for instance in instances:
            #cnf.append({"id": configuration.getId(), "nombre": configuration.getName(), "descripcion": configuration.getDescription()})
    return jsonify(tmp), 200