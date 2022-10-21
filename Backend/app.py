from re import I
from flask import Flask, request, jsonify
from flask_cors import CORS
from database import DataBase
import xml.etree.ElementTree as ET

app = Flask(__name__)
CORS(app)

db = DataBase()

######################## LOAD FILE CONFIGURATIONS ####################################
@app.route("/archivoConfiguracion", methods=["POST"])
def file_configuration():
    xml_content = request.get_data()
    xml_content = xml_content.decode('UTF-8')
    db.readConfigurationFile(xml_content)
    return jsonify({"mensaje": "Recibido"}), 200

######################## LOAD FILE CONSUMPTIONS ####################################
@app.route("/archivoConsumos", methods=["POST"])
def file_Consumptions():
    xml_content = request.get_data()
    xml_content = xml_content.decode('UTF-8')
    fileConsumptions = ET.fromstring(xml_content)
    print(fileConsumptions)
    return jsonify({"mensaje": "Recibido"}), 200

######################## RESOURCES ####################################
@app.route("/recursos")
def get_resources():
    resources = db.getResources()
    return jsonify({"recursos":resources}), 200

@app.route("/crearRecurso", methods=["POST"])
def create_resource():
    data = request.get_json()
    response = db.createResource(data)
    if response:
        return jsonify(request.get_json()), 201
    else:
        return jsonify({"mensaje": "Recurso repetido"}), 400

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
        return jsonify({"mensaje": "Recurso eliminado"}), 200

######################## CATEGORIES ####################################
@app.route("/categorias")
def get_categories():
    categories = db.getCategories()
    return jsonify({"categorias":categories}), 200

@app.route("/crearCategoria", methods=["POST"])
def create_category():
    data = request.get_json()
    response = db.createCategory(data)
    if response:
        return jsonify(request.get_json()), 201
    else:
        return jsonify({"mensaje": "Categoria repetida"}), 400

@app.route("/editarCategoria", methods=["PUT"])
def update_category():
    data = request.get_json()
    response = db.updateCategory(data)
    if response:
        return jsonify({"mensaje": "Categoria actualizada"}), 200

@app.route("/eliminarCategoria", methods=["DELETE"])
def delete_category():
    data = request.get_json()
    id = data["id"]
    response = db.deleteCategory(id)
    if response:
        return jsonify({"mensaje": "Categoria eliminada"}), 200

######################## CONFIGURATIONS ####################################
@app.route("/configuraciones", methods=["POST"])
def get_configurations():
    idCategory = request.get_json()
    idCategory = idCategory["idCategoria"]
    configurations = db.getConfigurations(idCategory)
    return jsonify({"configuraciones":configurations}), 200

@app.route("/crearConfiguracion", methods=["POST"])
def create_configuration():
    data = request.get_json()
    idCategory = data.pop("idCategoria")
    response = db.createConfiguration(data, idCategory)
    if response:
        return jsonify(request.get_json()), 201
    else:
        return jsonify({"mensaje": "Categoria repetida"}), 400

@app.route("/editarConfiguracion", methods=["PUT"])
def update_configuration():
    data = request.get_json()
    response = db.updateCategory(data)
    if response:
        return jsonify({"mensaje": "Categoria actualizada"}), 200

@app.route("/eliminarConfiguracion", methods=["DELETE"])
def delete_configuration():
    data = request.get_json()
    id = data["id"]
    response = db.deleteCategory(id)
    if response:
        return jsonify({"mensaje": "Categoria eliminada"}), 200

######################## RESOURCES IN CATEGORIES ####################################
@app.route("/recursosConfiguracion", methods=["POST"])
def get_resources_in_configuration():
    data = request.get_json()
    idCategory = data.pop("idCategoria")
    idConfiguration = data.pop("idConfiguracion")
    resources = db.getResourcesInCategory(idCategory, idConfiguration)
    return jsonify({"recursos":resources}), 200

@app.route("/crearRecursoConfiguracion", methods=["POST"])
def create_resource_in_configuration():
    data = request.get_json()
    idCategory = data.pop("idCategoria")
    idConfiguration = data.pop("idConfiguracion")
    response = db.createResourceInCategory(idCategory, idConfiguration, data)
    if response:
        return jsonify(request.get_json()), 201
    else:
        return jsonify({"mensaje": "Recurso repetido"}), 400

@app.route("/editarRecursoConfiguracion", methods=["PUT"])
def update_resource_in_configuration():
    data = request.get_json()
    response = db.updateCategory(data)
    if response:
        return jsonify({"mensaje": "Categoria actualizada"}), 200

@app.route("/eliminarRecursoConfiguracion", methods=["DELETE"])
def delete_resource_in_configuration():
    data = request.get_json()
    id = data["id"]
    response = db.deleteCategory(id)
    if response:
        return jsonify({"mensaje": "Categoria eliminada"}), 200

######################## CUSTOMERS ####################################
@app.route("/clientes")
def get_customers():
    customers = db.getCustomers()
    return jsonify({"clientes":customers}), 200

@app.route("/crearCliente", methods=["POST"])
def create_customer():
    data = request.get_json()
    response = db.createCustomer(data)
    if response:
        return jsonify(request.get_json()), 201
    else:
        return jsonify({"mensaje": "Cliente repetido"}), 400

@app.route("/editarCliente", methods=["PUT"])
def update_customer():
    data = request.get_json()
    response = db.updateCustomer(data)
    if response:
        return jsonify({"mensaje": "Cliente actualizado"}), 200

@app.route("/eliminarCliente", methods=["DELETE"])
def delete_customer():
    data = request.get_json()
    nit = data["nit"]
    response = db.deleteCustomer(nit)
    if response:
        return jsonify({"mensaje": "Cliente eliminado"}), 200

######################## INSTANCES ####################################
@app.route("/instancias", methods=["POST"])
def get_instances():
    nitCustomer = request.get_json()
    nitCustomer = nitCustomer["nitCliente"]
    configurations = db.getInstances(nitCustomer)
    return jsonify({"configuraciones":configurations}), 200

@app.route("/crearInstancia", methods=["POST"])
def create_instance():
    data = request.get_json()
    nitCustomer = data.pop("nitCliente")
    response = db.createInstance(data, nitCustomer)
    if response:
        return jsonify(request.get_json()), 201
    else:
        return jsonify({"mensaje": "Instancia repetida"}), 400

@app.route("/editarInstancia", methods=["PUT"])
def update_instance():
    data = request.get_json()
    nitCustomer = data.pop("nitCliente")
    response = db.updateInstance(data, nitCustomer)
    if response:
        return jsonify({"mensaje": "Instancia actualizada"}), 200

@app.route("/eliminarInstancia", methods=["DELETE"])
def delete_instance():
    data = request.get_json()
    idCustomer = data.pop("nitCliente")
    idInstance = data.pop("idInstancia")
    response = db.deleteInstance(idCustomer, idInstance)
    if response:
        return jsonify({"mensaje": "Instancia eliminada"}), 200