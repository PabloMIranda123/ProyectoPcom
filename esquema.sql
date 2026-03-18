BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Enfoque" (
	"id_enfoque"	INTEGER NOT NULL,
	"dias"	INTEGER NOT NULL,
	"duración"	INTEGER NOT NULL,
	"nombre"	TEXT
);
CREATE TABLE IF NOT EXISTS "Persona" (
	"id"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"id_entrenam"	INTEGER NOT NULL,
	"id_enfoque"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Ejercicios" (
	"id_ejercicio"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"id_enfoque"	INTEGER NOT NULL,
	PRIMARY KEY("id_ejercicio")
);
COMMIT;
