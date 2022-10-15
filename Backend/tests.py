from lxml import etree
import xml.etree.ElementTree as ET

xml_Configurations = """<archivoConfiguraciones>
    <listaRecursos>
        <recurso id="$idRecurso">
            <nombre>$nombreRecurso </nombre>
            <abreviatura> $abreviaturaRecurso </abreviatura>
            <metrica> $NombreMetrica </metrica>
            <tipo> $tipoRecurso </tipo>
            <valorXhora> valorNumerico </valorXhora>
        </recurso>
    </listaRecursos>
    <listaCategorias>
        <categoria id="$idCategoria">
            <nombre> $nombreCategoria </nombre>
            <descripcion> $descripcionCategoria </descripcion>
            <cargaTrabajo> $descripcionCargaTrabajo </cargaTrabajo>
            <listaConfiguraciones>
                <configuracion id="$idConfiguracion">
                    <nombre> $nombreConfiguracion </nombre>
                    <descripcion> $descripcionConfiguracion </descripcion>
                    <recursosConfiguracion>
                        <recurso id="$idRecurso"> cantidadRecurso </recurso>
                    </recursosConfiguracion>
                </configuracion>
            </listaConfiguraciones>
        </categoria>
    </listaCategorias>
    <listaClientes>
        <cliente nit="$nitCliente">
            <nombre> $nombreCliente </nombre>
            <usuario> $nombreUsuario </usuario>
            <clave> $claveUsuario </clave>
            <direccion> $direccionCliente </direccion>
            <correoElectronico> $eMailCliente </correoElectronico>
            <listaInstancias>
                <instancia id="idInstancia">
                    <idCategoria> $idCategoria </idCategoria>
                    <nombre> $nombreInstancia </nombre>
                    <fechaInicio> $descripcionFecha </fechaInicio>
                    <estado> $estado </estado>
                    <fechaFinal> $descripcionFecha </fechaFinal>
                </instancia>
            </listaInstancias>
        </cliente>
    </listaClientes>
</archivoConfiguraciones>"""

"""content = {"content":xml_Configurations}
print(content.__class__ == dict)
content_fileXml_configurations = content["content"]
"""

"""tree = etree.parse('C:/Users/Luis T/Desktop/archivoConfiguraciones.xml')
xml_str = etree.tostring(tree, encoding='utf8', method='xml')
print(xml_str)"""
"""fileConfigurations = ET.fromstring(xml_str)
listResources = fileConfigurations.find('listaRecursos')
for resource in listResources:
    idResource = resource.attrib['id']
    print(idResource)
    nameResourse = resource.find('nombre').text
    print(nameResourse)
"""