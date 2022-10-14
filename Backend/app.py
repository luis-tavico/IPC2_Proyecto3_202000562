from flask import Flask, request, jsonify
from flask_cors import CORS
from database import DataBase

app = Flask(__name__)
CORS(app)

db = DataBase()
db.readConfigurationFile("files/archivoConfiguraciones.xml")
#r1 = {'id': 'r1', 'nombre': 'system', 'abreviatura': 'sys', 'metrica': 'saber', 'tipo': 'Hardware', 'valorXhora': '10'}
#r2 = {'id': 'r2', 'nombre': 'system', 'abreviatura': 'sys', 'metrica': 'saber', 'tipo': 'Software', 'valorXhora': '25'}
#r2 = {'id': 'r3', 'nombre': 'system', 'abreviatura': 'sys', 'metrica': 'saber', 'tipo': 'Hardware', 'valorXhora': '25'}
#db.newResource(r1)
#db.newResource(r2)
#db.newResource(r3)

@app.route("/nuevoRecurso", methods=["POST"])
def create_resource():
    data = request.get_json()
    response = db.newResource(data)
    if response:
        return jsonify(request.get_json()), 201
    else:
        return jsonify({"mensaje": "Recurso repetido"}), 400


@app.route("/recursos")
def get_resources():
    rsc = db.getResources()
    return jsonify({"recursos":rsc}), 200

@app.route("/editarRecurso", methods=["PUT"])
def update_resource():
    data = request.get_json()
    response = db.updateResource(data)
    if response:
        return jsonify({"mensaje": "Recurso actualizado"}), 200

@app.route("/eliminarRecurso", methods=["DELETE"])
def delete_resource():
    data = request.get_json()
    id = data["id"]
    response = db.deleteResource(id)
    if response:
        return jsonify({"mensaje": "Recurso eliminada"}), 200

'''@app.route("/categoria", methods=["POST"])
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

@app.route("/configuracion", methods=["POST"])
def create_configuration():
    data = request.get_json()
    id = data["id"]
    name = data["nombre"]
    description = data["descripcion"]
    resources = data["recursosConfiguracion"]
    for configuration in configurations:
        if configuration.getId() == id:
            return jsonify({"mensaje": "Configuracion repetida"}), 400
    configurations.append(Configuration(id, name, description, resources))
    return jsonify(request.get_json()), 201

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

@app.route("/instancia", methods=["POST"])
def create_instance():
    data = request.get_json()
    id = data["id"]
    idCategory = data["idCategoria"]
    name = data["nombre"]
    dateStart = data["fechaInicio"]
    state = data["estado"]
    dateEnd = data["fechaFinal"]
    for instance in instances:
        if instance.getId() == id:
            return jsonify({"mensaje": "Instancia repetida"}), 400
    instances.append(Instance(id, name, idCategory, dateStart, state, dateEnd))
    return jsonify(request.get_json()), 201'''