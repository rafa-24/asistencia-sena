from main import connect_database
from datetime import datetime
import pandas as pd

conn = connect_database()
cur = conn.cursor()


def lista_asistencia():
    estudiantes = []
    try:
        cur.execute('SELECT * FROM asistencia_aprendices;')
        asitencias = cur.fetchall()

        for a in asitencias:
            obj = {
                'id': a[0],
                'estado': a[1],
                'asistio': a[2],
                'nombre':a[3],
                'primer_apellido':a[4],
                'segundo_apellido':a[5],
                'fecha': a[6]
            }
            estudiantes.append(obj)
        return estudiantes   
    except:
        print('Error')


# Inasistencia por estudiante
def inasistencias_por_dia(nombre):
    counter_inasitencia = 0
    inasistencia = []
    lista_estudiantes = lista_asistencia()

    try:        
        for estudiante in lista_estudiantes:
                if estudiante['nombre'] == nombre:
                    inasistencia.append(estudiante)
                    for index in inasistencia:
                        if index['asistio'] == 'F':
                            counter_inasitencia += 1                                     
    except Exception as e:
        return f'ocurrio un error {e}'
    finally:
        return f'la inasistencia del Aprendiz {nombre} es {counter_inasitencia}'


def obtener_dia_semana(fecha):
    # Diccionario para traducir días de la semana del inglés al español
    dias_semana = {
        'Monday': 'lunes',
        'Tuesday': 'martes',
        'Wednesday': 'miércoles',
        'Thursday': 'jueves',
        'Friday': 'viernes',
        'Saturday': 'sábado',
        'Sunday': 'domingo'
    }

    # Obtener el día de la semana en inglés
    dia_ingles = fecha.strftime("%A")
    # Traducir al español
    dia_espanol = dias_semana[dia_ingles]
    return dia_espanol

# Dia con mas falla por estudiante
def dia_mas_fallas_estudiantes():
        result = ''
        arr = []
        data = lista_asistencia()  # Asumiendo que lista_asistencia() devuelve una lista de diccionarios con la clave "fecha"
        for index in data:
            fecha = index["fecha"]
            result = obtener_dia_semana(fecha)
            index['dia'] = result
            arr.append(index)
        df = pd.DataFrame(arr)
        faltas = df[(df['asistio'] == 'F') & (df['dia'] != 'domingo')]
        contador_faltas = faltas['dia'].value_counts()
        dia_con_mas_faltas = contador_faltas.idxmax()
    
        return f'el dia con mas inasistencia de todos los aprendices es el {dia_con_mas_faltas}'
                 







