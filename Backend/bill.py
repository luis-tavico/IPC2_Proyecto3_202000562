import pdfkit

class Bill:

    def __init__(self):
        self.invoice = ""

    def generateBill(self, bill):
        self.invoice += """<!doctype html>
<html lang="es">

<head>
  <title>Factura</title>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS v5.2.1 -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
</head>\n"""
        self.invoice += '<body>\n'
        self.invoice += '    <div class="container">\n'
        self.invoice += '        <div class="row">\n'
        self.invoice += '            <div class="col-12">\n'
        self.invoice += '              <br/>\n'
        self.invoice += '              <div class="card">\n'
        self.invoice += '                <div class="card-header">\n'
        self.invoice += '                    <div class="container">\n'
        self.invoice += '                        <div class="row align-items-start">\n'
        self.invoice += '                          <div class="col">\n'
        self.invoice += '                            <p class="card-text">Fecha: '+bill["fecha"]+'</p>\n'
        self.invoice += '                          </div>\n'
        self.invoice += '                          <div class="col text-end">\n'
        self.invoice += '                            <p class="card-text">Estado: '+bill["estado"]+'</p>\n'
        self.invoice += '                          </div>\n'
        self.invoice += '                        </div>\n'
        self.invoice += '                    </div>\n'
        self.invoice += '                </div>\n'
        self.invoice += '                <div class="card-body">\n'
        self.invoice += '                    <div class="container">\n'
        self.invoice += '                        <div class="row align-items-start">\n'
        self.invoice += '                          <div class="col">\n'
        self.invoice += '                            <h1 class="card-title">FACTURA</h1>\n'
        self.invoice += '                          </div>\n'
        self.invoice += '                          <div class="col">\n'
        self.invoice += '                            <p class="card-text">Factura: '+bill["numero"]+'<br>\n'
        self.invoice += '                                Fecha de Emision: '+bill["fecha"]+'<br></p>\n'
        self.invoice += '                          </div>\n'
        self.invoice += '                          <div class="col">\n'
        self.invoice += '                            <p class="card-text">NIT: '+bill["nitCliente"]+'<br>\n'
        self.invoice += '                                Nombre: '+bill["nombreCliente"]+'<br>\n'
        self.invoice += '                                Direccion: '+bill["direccionCliente"]+'<br></p>\n'
        self.invoice += '                          </div>\n'
        self.invoice += '                        </div>\n'
        self.invoice += '                    </div>\n'
        self.invoice += '                    <hr class="border border-secondary border- opacity-5">\n'
        self.invoice += '                    <h5>Instancia '+bill["idInstancia"]+'</h5>\n'
        self.invoice += '                    <div class="table-responsive">\n'
        self.invoice += '                        <table class="table table-default">\n'
        self.invoice += '                            <thead class="table-light border border-start-0 border-end-0">\n'
        self.invoice += '                                <tr>\n'
        self.invoice += '                                    <th scope="col">Recurso</th>\n'
        self.invoice += '                                    <th scope="col">Cantidad</th>\n'
        self.invoice += '                                    <th scope="col">Valor por Hora</th>\n'
        self.invoice += '                                    <th scope="col">Tiempo</th>\n'
        self.invoice += '                                    <th scope="col">Importe</th>\n'
        self.invoice += '                                </tr>\n'
        self.invoice += '                            </thead>\n'
        self.invoice += '                            <tbody>\n'
        consumptions = bill["consumos"]
        for consumption in consumptions:
          self.invoice += '                                <tr>\n'
          self.invoice += '                                    <td>'+consumption["nombre"]+'</td>\n'
          self.invoice += '                                    <td>'+str(consumption["cantidad"])+'</td>\n'
          self.invoice += '                                    <td>Q.'+str(consumption["valorXhora"])+'</td>\n'
          self.invoice += '                                    <td>'+str(consumption["tiempo"])+'hrs</td>\n'
          self.invoice += '                                    <td>Q.'+str(consumption["importe"])+'</td>\n'
          self.invoice += '                                </tr>\n'
        self.invoice += '                            </tbody>\n'
        self.invoice += '                        </table>\n'
        self.invoice += '                    </div>\n'
        self.invoice += '                    <div class="offset-md-10 border border-start-0 border-end-0 text-center">\n'
        self.invoice += '                        <strong>Subtotal</strong> Q.'+str(bill["total"])+'\n'
        self.invoice += '                    </div>\n'
        self.invoice += '                    <hr class="border border-secondary border-opacity-5">\n'
        self.invoice += '                    <div class="offset-md-10 border border-start-0 border-end-0 text-center">\n'
        self.invoice += '                        <strong>TOTAL</strong> Q.'+str(bill["total"])+'\n'
        self.invoice += '                    </div>\n'
        self.invoice += '                </div>\n'
        self.invoice += '                <div class="card-footer text-muted">\n'
        self.invoice += '                </div>\n'
        self.invoice += '            </div>\n'
        self.invoice += '            <br>\n'
        self.invoice += '            </div>\n'
        self.invoice += '        </div>\n'
        self.invoice += '    </div>\n'
        self.invoice += """"  <!-- Bootstrap JavaScript Libraries -->
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"
    integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous">
  </script>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js"
    integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz" crossorigin="anonymous">
  </script>
</body>

</html>"""
        f = "reports/factura-"+bill["numero"]+".html"
        p = 'factura-'+bill["numero"]+'.pdf'
        bill = open(f, "w")
        bill.write(self.invoice)
        bill.close()  
        pdfkit.from_file(f, p)