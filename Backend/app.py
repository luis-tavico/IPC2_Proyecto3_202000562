#from re import I
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from database import DataBase
import xml.etree.ElementTree as ET
import re

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
    db.readConsumptionFile(xml_content)
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
        return jsonify({"mensaje": "¡Recurso creado exitosamente!"}), 201
    else:
        return jsonify({"mensaje": "¡Error! Recurso repetido"}), 400

@app.route("/editarRecurso", methods=["PUT"])
def update_resource():
    data = request.get_json()
    response = db.updateResource(data)
    if response:
        return jsonify({"mensaje": "¡Recurso actualizado exitosamente!"}), 200
    else:
        return jsonify({"mensaje": "¡Error!"}), 400

@app.route("/eliminarRecurso", methods=["DELETE"])
def delete_resource():
    data = request.get_json()
    id = data["id"]
    response = db.deleteResource(id)
    if response:
        return jsonify({"mensaje": "¡Recurso eliminado exitosamente!"}), 200
    else:
        return jsonify({"mensaje": "¡Error!"}), 400

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
        return jsonify({"mensaje": "¡Categoria creada exitosamente!"}), 201
    else:
        return jsonify({"mensaje": "¡Error! Categoria repetida"}), 400

@app.route("/editarCategoria", methods=["PUT"])
def update_category():
    data = request.get_json()
    print(data)
    response = db.updateCategory(data)
    if response:
        return jsonify({"mensaje": "¡Categoria actualizada exitosamente!"}), 200
    else:
        return jsonify({"mensaje": "¡Error!"}), 400

@app.route("/eliminarCategoria", methods=["DELETE"])
def delete_category():
    data = request.get_json()
    id = data["id"]
    response = db.deleteCategory(id)
    if response:
        return jsonify({"mensaje": "¡Categoria eliminada exitosamente!"}), 200
    else:
        return jsonify({"mensaje": "¡Error!"}), 400
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
        return jsonify({"mensaje": "¡Configuracion creada exitosamente!"}), 201
    else:
        return jsonify({"mensaje": "¡Error! Configuracion repetida"}), 400

@app.route("/editarConfiguracion", methods=["PUT"])
def update_configuration():
    data = request.get_json()
    idCategory = data.pop("idCategoria")
    response = db.updateConfiguration(data, idCategory)
    if response:
        return jsonify({"mensaje": "¡Configuracion actualizada exitosamente!"}), 200
    else:
        return jsonify({"mensaje": "¡Error!"}), 400

@app.route("/eliminarConfiguracion", methods=["DELETE"])
def delete_configuration():
    data = request.get_json()
    idConfiguration = data["idConfiguracion"]
    idCategory = data["idCategoria"]
    response = db.deleteConfiguration(idConfiguration, idCategory)
    if response:
        return jsonify({"mensaje": "¡Configuracion eliminada exitosamente!"}), 200
    else:
        return jsonify({"mensaje": "¡Error!"}), 400

######################## RESOURCES IN CONFIGURATIONS ####################################
@app.route("/recursosConfiguracion", methods=["POST"])
def get_resources_in_configuration():
    data = request.get_json()
    idCategory = data.pop("idCategoria")
    idConfiguration = data.pop("idConfiguracion")
    resources = db.getResourcesInConfiguration(idCategory, idConfiguration)
    return jsonify({"recursos":resources}), 200

@app.route("/agregarRecursoConfiguracion", methods=["POST"])
def create_resource_in_configuration():
    data = request.get_json()
    idCategory = data.pop("idCategoria")
    idConfiguration = data.pop("idConfiguracion")
    response = db.addResourceInConfiguration(idCategory, idConfiguration, data)
    if response:
        return jsonify({"mensaje": "¡Recurso agregado exitosamente!"}), 201
    else:
        return jsonify({"mensaje": "¡Error! Recurso repetido"}), 400

@app.route("/editarRecursoConfiguracion", methods=["PUT"])
def update_resource_in_configuration():
    data = request.get_json()
    idCategory = data.pop("idCategoria")
    idConfiguration = data.pop("idConfiguracion")
    response = db.updateResourceInConfiguration(idCategory, idConfiguration, data)
    if response:
        return jsonify({"mensaje": "¡Recurso actualizado exitosamente!"}), 200
    else:
        return jsonify({"mensaje": "¡Error!"}), 400

@app.route("/eliminarRecursoConfiguracion", methods=["DELETE"])
def delete_resource_in_configuration():
    data = request.get_json()
    idCategory = data.pop("idCategoria")
    idConfiguration = data.pop("idConfiguracion")
    idResource = data.pop("idRecurso")
    response = db.deleteResourceInConfiguration(idCategory, idConfiguration, idResource)
    if response:
        return jsonify({"mensaje": "¡Recursos eliminado exitosamente!"}), 200
    else:
        return jsonify({"mensaje": "¡Error!"}), 400

######################## CUSTOMERS ####################################
@app.route("/clientes")
def get_customers():
    customers = db.getCustomers()
    print(customers)
    return jsonify({"clientes":customers}), 200

@app.route("/crearCliente", methods=["POST"])
def create_customer():
    data = request.get_json()
    response = db.createCustomer(data)
    if response:
        return jsonify({"mensaje": "¡Cliente creado exitosamente!"}), 201
    else:
        return jsonify({"mensaje": "¡Error! Cliente repetido"}), 400


@app.route("/editarCliente", methods=["PUT"])
def update_customer():
    data = request.get_json()
    response = db.updateCustomer(data)
    if response:
        return jsonify({"mensaje": "¡Cliente actualizado exitosamente!"}), 200
    else:
        return jsonify({"mensaje": "¡Error!"}), 400


@app.route("/eliminarCliente", methods=["DELETE"])
def delete_customer():
    data = request.get_json()
    nit = data["nit"]
    response = db.deleteCustomer(nit)
    if response:
        return jsonify({"mensaje": "¡Cliente actualizado exitosamente!"}), 200
    else:
        return jsonify({"mensaje": "¡Error!"}), 400

######################## INSTANCES ####################################
@app.route("/instancias", methods=["POST"])
def get_instances():
    nitCustomer = request.get_json()
    nitCustomer = nitCustomer["nitCliente"]
    instances = db.getInstances(nitCustomer)
    print(instances)
    return jsonify({"instancias":instances}), 200

@app.route("/crearInstancia", methods=["POST"])
def create_instance():
    data = request.get_json()
    nitCustomer = data.pop("nitCliente")
    dateStart = data["fechaInicio"]
    dateEnd = data["fechaFinal"]
    dateStart = re.findall(r'(\d{2})/(\d{2})/(\d{4})', dateStart)
    dateEnd = re.findall(r'(\d{2})/(\d{2})/(\d{4})', dateEnd)
    if len(dateStart) > 0 and len(dateEnd) > 0:
        dateStart = dateStart[0]
        dateStart = '/'.join(dateStart)
        dateEnd = dateEnd[0]
        dateEnd = '/'.join(dateEnd)
        dateS = datetime.strptime(dateStart, '%d/%m/%Y').date()
        dateE = datetime.strptime(dateEnd, '%d/%m/%Y').date()
        data["fechaInicio"] = dateS
        data["fechaFinal"] = dateE
    print(data)
    response = db.createInstance(data, nitCustomer)
    if response:
        return jsonify({"mensaje": "¡Instancia creada exitosamente!"}), 201
    else:
        return jsonify({"mensaje": "¡Error! Instancia repetida"}), 400

@app.route("/editarInstancia", methods=["PUT"])
def update_instance():
    data = request.get_json()
    nitCustomer = data.pop("nitCliente")
    dateStart = data["fechaInicio"]
    dateEnd = data["fechaFinal"]
    dateStart = re.findall(r'(\d{2})/(\d{2})/(\d{4})', dateStart)
    dateEnd = re.findall(r'(\d{2})/(\d{2})/(\d{4})', dateEnd)
    if len(dateStart) > 0 and len(dateEnd) > 0:
        dateStart = dateStart[0]
        dateStart = '/'.join(dateStart)
        dateEnd = dateEnd[0]
        dateEnd = '/'.join(dateEnd)
        dateS = datetime.strptime(dateStart, '%d/%m/%Y').date()
        dateE = datetime.strptime(dateEnd, '%d/%m/%Y').date()
        data["fechaInicio"] = dateS
        data["fechaFinal"] = dateE
    response = db.updateInstance(data, nitCustomer)
    if response:
        return jsonify({"mensaje": "¡Instancia actualizada exitosamente!"}), 200
    else:
        return jsonify({"mensaje": "¡Error!"}), 400

@app.route("/eliminarInstancia", methods=["DELETE"])
def delete_instance():
    data = request.get_json()
    idCustomer = data.pop("nitCliente")
    idInstance = data.pop("idInstancia")
    response = db.deleteInstance(idCustomer, idInstance)
    if response:
        return jsonify({"mensaje": "¡Instancia eliminada exitosamente!"}), 201
    else:
        return jsonify({"mensaje": "¡Error!"}), 400

######################## CONSUMPTIONS ####################################
@app.route("/consumos")
def get_consumptions():
    consumptions = db.getConsumptions()
    return jsonify({"consumos":consumptions}), 200

######################## BILLS ####################################
@app.route("/generarFactura", methods=["POST"])
def generate_Invoice():
    data = request.get_json()
    dateStart = data["fechaInicio"]
    dateEnd = data["fechaFinal"]
    dateStart = re.findall(r'(\d{2})/(\d{2})/(\d{4})', dateStart)
    dateEnd = re.findall(r'(\d{2})/(\d{2})/(\d{4})', dateEnd)
    if len(dateStart) > 0 and len(dateEnd) > 0:
        dateStart = dateStart[0]
        dateStart = '/'.join(dateStart)
        dateEnd = dateEnd[0]
        dateEnd = '/'.join(dateEnd)
        dateS = datetime.strptime(dateStart, '%d/%m/%Y').date()
        dateE = datetime.strptime(dateEnd, '%d/%m/%Y').date()
        print(dateS, dateE)
        response = db.generateInvoice(dateS, dateE)
        if response:
            return jsonify(request.get_json()), 201
        else:
            return jsonify({"mensaje": "No se encontraron fechas"}), 400
    else:
        return jsonify({"mensaje": "No se encontraron fechas"}), 400