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
    fileConfigurations = ET.fromstring(xml_content)
    print(fileConfigurations)
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

@app.route("/nuevoRecurso", methods=["POST"])
def create_resource():
    data = request.get_json()
    response = db.newResource(data)
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

@app.route("/nuevaCategoria", methods=["POST"])
def create_category():
    data = request.get_json()
    response = db.newCategory(data)
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

######################## CUSTOMERS ####################################
@app.route("/clientes")
def get_customers():
    customers = db.getCustomers()
    return jsonify({"clientes":customers}), 200

@app.route("/nuevoCliente", methods=["POST"])
def create_customer():
    data = request.get_json()
    response = db.newCustomer(data)
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
    id = data["id"]
    response = db.deleteCustomer(id)
    if response:
        return jsonify({"mensaje": "Cliente eliminado"}), 200