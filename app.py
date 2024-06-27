from flask import Flask
from flasgger import Swagger
from services import lista_asistencia, inasistencias_por_dia, dia_mas_fallas_estudiantes

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/listado-asistencia')
def obtener_aprendices():
    """
    Obtener la lista de asistencia
    ---
    responses:
      200:
        description: Lista de asistencia
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              estado:
                type: string
              asistio:
                type: boolean
              nombre:
                type: string
              primer_apellido:
                type: string
              segundo_apellido:
                type: string
              fecha:
                type: string
              dia:
                type: string
    """
    return lista_asistencia()    


@app.route('/inasistencia/<nombre>', methods=['GET'])
def inasitencia_aprendiz(nombre):
    """
    Obtener inasistencias por aprendiz
    ---
    parameters:
      - name: nombre
        in: path
        type: string
        required: true
        description: Nombre del aprendiz
    responses:
      200:
        description: Inasistencias del aprendiz
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              estado:
                type: string
              asistio:
                type: boolean
              nombre:
                type: string
              primer_apellido:
                type: string
              segundo_apellido:
                type: string
              fecha:
                type: string
              dia:
                type: string
    """
    return inasistencias_por_dia(nombre)

@app.route('/promedio-fallas-aprendices')
def promedio_fallas_aprendices():
    """
    Obtener el día con más fallas de los aprendices
    ---
    responses:
      200:
        description: Día con más fallas de los aprendices
        schema:
          type: object
          properties:
            dia:
              type: string
            fallas:
              type: integer
    """
    return dia_mas_fallas_estudiantes()


if __name__ == '__main__':
    app.run(debug=True)
