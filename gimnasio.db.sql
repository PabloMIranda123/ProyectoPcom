BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Ejercicios" (
    "id_ejercicio"    INTEGER NOT NULL,
    "nombre"    TEXT NOT NULL,
    "id_enfoque"    INTEGER NOT NULL,
    PRIMARY KEY("id_ejercicio")
);
CREATE TABLE IF NOT EXISTS "Enfoque" (
    "id_enfoque"    INTEGER NOT NULL,
    "dias"    INTEGER NOT NULL,
    "duración"    INTEGER NOT NULL,
    "nombre"    TEXT,
    PRIMARY KEY("id_enfoque" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Persona" (
    "id"    INTEGER NOT NULL,
    "nombre"    TEXT NOT NULL,
    "id_entrenam"    INTEGER NOT NULL,
    "id_enfoque"    INTEGER NOT NULL,
    FOREIGN KEY("id_enfoque") REFERENCES "Enfoque",
    PRIMARY KEY("id")
);
INSERT INTO "Ejercicios" VALUES (1,'Press Banca',1);
INSERT INTO "Ejercicios" VALUES (2,'cardio en cinta',2);
INSERT INTO "Ejercicios" VALUES (3,'hiit',3);
INSERT INTO "Enfoque" VALUES (1,5,'90min','ganar musculo');
INSERT INTO "Enfoque" VALUES (2,6,'45 min','perder peso');
INSERT INTO "Enfoque" VALUES (3,4,'60min','mantenimiento');
INSERT INTO "Persona" VALUES (1,'Michel',1,2);
INSERT INTO "Persona" VALUES (2,'Juan','',1);
INSERT INTO "Persona" VALUES (3,'Cristina',2,1);
COMMIT;
