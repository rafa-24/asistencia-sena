CREATE TABLE "Sena" (
  "id_sena" integer PRIMARY KEY,
  "nombre" varchar,
  "direccion" varchar,
  "cod_departamento" integer
);

CREATE TABLE "Departamento" (
  "id_departamento" integer PRIMARY KEY,
  "nombre" varchar
);

CREATE TABLE "ProgramasFormacion" (
  "id_programa" integer PRIMARY KEY,
  "nombre_programa" varchar,
  "nivel_formacion" varchar,
  "ficha" integer,
  "duracion" integer,
  "cod_sena" integer
);

CREATE TABLE "Aprendiz" (
  "id_aprendiz" integer PRIMARY KEY,
  "apellido_paterno" varchar,
  "apellido_materno" varchar,
  "nombre" varchar,
  "email" varchar,
  "cod_programa_formacion" integer
);

CREATE TABLE "Clase" (
  "id_clase" integer PRIMARY KEY,
  "nombre_clase" varchar,
  "descripcion" text,
  "horario" varchar,
  "ambiente" varchar
);

CREATE TABLE "Inscripcion" (
  "cod_aprendiz" integer,
  "cod_clase" integer
);

CREATE TABLE "Asistencia" (
  "cod_clase" integer,
  "cod_aprendiz" integer,
  "estado" bool,
  "asistio" char,
  "fecha" timestamp
);

ALTER TABLE "Sena" ADD FOREIGN KEY ("cod_departamento") REFERENCES "Departamento" ("id_departamento");

ALTER TABLE "ProgramasFormacion" ADD FOREIGN KEY ("cod_sena") REFERENCES "Sena" ("id_sena");

ALTER TABLE "Aprendiz" ADD FOREIGN KEY ("cod_programa_formacion") REFERENCES "ProgramasFormacion" ("id_programa");

ALTER TABLE "Aprendiz" ADD FOREIGN KEY ("id_aprendiz") REFERENCES "Inscripcion" ("cod_aprendiz");

ALTER TABLE "Clase" ADD FOREIGN KEY ("id_clase") REFERENCES "Inscripcion" ("cod_clase");

ALTER TABLE "Asistencia" ADD FOREIGN KEY ("cod_clase") REFERENCES "Clase" ("id_clase");

ALTER TABLE "Asistencia" ADD FOREIGN KEY ("cod_aprendiz") REFERENCES "Aprendiz" ("id_aprendiz");
