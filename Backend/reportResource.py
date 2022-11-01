import pdfkit

class Report:

    def __init__(self):
        self.report = ""

    def generateReport(self, resource):
        self.report += """<!doctype html>
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
        self.report += '<body>\n'
        self.report += '<br>\n'
        self.report += '    <div class="card text-center">\n'
        self.report += '        <div class="card-header">\n'
        self.report += '          REPORTE\n'
        self.report += '        </div>\n'
        self.report += '        <div class="card-body">\n'
        self.report += '          <h5 class="card-title">Recurso</h5>\n'
        self.report += '          <p class="card-text">Detalles del recurso que mas ingresos genero:<br>\n'
        self.report += '          ID: '+resource["id"]+'</p>\n'
        self.report += '        </div>\n'
        self.report += '        <div class="card-footer text-muted">\n'
        self.report += '          De: '+resource["fechaInicio"]+' A: '+resource["fechaFinal"]+'\n'
        self.report += '        </div>\n'
        self.report += '      </div>\n'
        self.report += """"  <!-- Bootstrap JavaScript Libraries -->
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"
    integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous">
  </script>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js"
    integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz" crossorigin="anonymous">
  </script>
</body>

</html>"""
        f = "reports/reportResource.html"
        p = 'reportResource.pdf'
        bill = open(f, "w")
        bill.write(self.report)
        bill.close()  
        pdfkit.from_file(f, p)