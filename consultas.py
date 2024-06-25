from main import connect_database
import psycopg2


def create_tables(conn):
    commands = (
        """
        CREATE TABLE IF NOT EXISTS Sena (
            id_sena SERIAL PRIMARY KEY,
            nombre VARCHAR(255),
            direccion VARCHAR(255),
            cod_departamento INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Departamento (
            id_departamento SERIAL PRIMARY KEY,
            nombre VARCHAR(255)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS ProgramasFormacion (
            id_programa SERIAL PRIMARY KEY,
            nombre_programa VARCHAR(255),
            nivel_formacion VARCHAR(255),
            ficha INTEGER,
            duracion INTEGER,
            cod_sena INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Aprendiz (
            id_aprendiz SERIAL PRIMARY KEY,
            apellido_paterno VARCHAR(255),
            apellido_materno VARCHAR(255),
            nombre VARCHAR(255),
            email VARCHAR(255),
            cod_programa_formacion INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Clase (
            id_clase SERIAL PRIMARY KEY,
            nombre_clase VARCHAR(255),
            descripcion TEXT,
            horario VARCHAR(255),
            ambiente VARCHAR(255)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Inscripcion (
            cod_aprendiz INTEGER,
            cod_clase INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Asistencia (
            cod_clase INTEGER,
            cod_aprendiz INTEGER,
            estado BOOLEAN,
            asistencia VARCHAR(255),
            fecha TIMESTAMP
        )
        """
    )
    try:
        # Conectar a la base de datos
        conn = connect_database()
        cur = conn.cursor()
        
        # Ejecutar cada comando SQL
        for command in commands:
            cur.execute(command)
        
        # Confirmar los cambios
        conn.commit()
        print("Tablas creadas correctamente")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()          

def create_relationships(conn):
    commands = (
        """
        ALTER TABLE "Sena"
        ADD CONSTRAINT fk_sena_departamento
        FOREIGN KEY ("cod_departamento") REFERENCES "Departamento" ("id_departamento")
        """,
        """
        ALTER TABLE "ProgramasFormacion"
        ADD CONSTRAINT fk_programasformacion_sena
        FOREIGN KEY ("cod_sena") REFERENCES "Sena" ("id_sena")
        """,
        """
        ALTER TABLE "Aprendiz"
        ADD CONSTRAINT fk_aprendiz_programasformacion
        FOREIGN KEY ("cod_programa_formacion") REFERENCES "ProgramasFormacion" ("id_programa")
        """,
        """
        ALTER TABLE "Aprendiz"
        ADD CONSTRAINT fk_aprendiz_inscripcion
        FOREIGN KEY ("id_aprendiz") REFERENCES "Inscripcion" ("cod_aprendiz")
        """,
        """
        ALTER TABLE "Clase"
        ADD CONSTRAINT fk_clase_inscripcion
        FOREIGN KEY ("id_clase") REFERENCES "Inscripcion" ("cod_clase")
        """,
        """
        ALTER TABLE "Asistencia"
        ADD CONSTRAINT fk_asistencia_clase
        FOREIGN KEY ("cod_clase") REFERENCES "Clase" ("id_clase")
        """,
        """
        ALTER TABLE "Asistencia"
        ADD CONSTRAINT fk_asistencia_aprendiz
        FOREIGN KEY ("cod_aprendiz") REFERENCES "Aprendiz" ("id_aprendiz")
        """
    )
    try:
        # Conectar a la base de datos
        conn = connect_database()
        cur = conn.cursor()
        
        # Ejecutar cada comando SQL
        for command in commands:
            cur.execute(command)
        
        # Confirmar los cambios
        conn.commit()
        print("Relaciones creadas correctamente")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()