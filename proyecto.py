import sqlite3
 
DB_PATH = "gimnasio.db"
 
 
def mostrar_enfoques():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
 
    cursor.execute("SELECT id_enfoque, nombre, dias, duración FROM Enfoque")
    resultados = cursor.fetchall()
 
    for fila in resultados:
        print(f"[{fila[0]}] {fila[1]} — {fila[2]} dias, {fila[3]}")
 
    conexion.close()

def borrar_persona():
    ver_todo()
    id_borrar = input("Introduce el ID de la persona que quieres borrar: ")
 
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
 
    cursor.execute("DELETE FROM Persona WHERE id = ?", (id_borrar,))
 
    conexion.commit()
    print(f"Persona con ID {id_borrar} eliminada.")
    conexion.close()
 
 
def agregar_persona():
    print("AGREGAR NUEVA PERSONA")
    nombre = input("Nombre: ")
    id_entrenam = input("ID de entrenamiento: ")
    print("Enfoques disponibles:")
    mostrar_enfoques()
    id_enfoque = input("ID de enfoque: ")
 
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
 
    cursor.execute(
        "INSERT INTO Persona (nombre, id_entrenam, id_enfoque) VALUES (?, ?, ?)",
        (nombre, id_entrenam, id_enfoque)
    )
 
    conexion.commit()
    print(f"Persona '{nombre}' añadida con ID {cursor.lastrowid}.")
    conexion.close()
 
 
def ver_personas():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
 
    cursor.execute("SELECT nombre, id_entrenam FROM Persona")
    resultados = cursor.fetchall()
 
    for fila in resultados:
        print(f"Nombre: {fila[0]} | Entrenamiento: {fila[1]}")
 
    conexion.close()
 
 
def ver_todo():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
 
    cursor.execute("SELECT id, nombre, id_entrenam, id_enfoque FROM Persona")
    resultados = cursor.fetchall()
 
    for fila in resultados:
        print(f"ID: {fila[0]} | Nombre: {fila[1]} | Entrenamiento: {fila[2]} | Enfoque: {fila[3]}")
 
    conexion.close()
 
def actualizar_persona():
    ver_todo()
    id_actualizar = input("Introduce el ID de la persona que quieres actualizar: ")
 
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
 
    cursor.execute("SELECT id, nombre, id_entrenam, id_enfoque FROM Persona WHERE id = ?", (id_actualizar,))
    persona = cursor.fetchone()
 
    if not persona:
        print(f"No se encontró ninguna persona con ID {id_actualizar}.")
        conexion.close()
        return
 
    print(f"Editando: {persona[1]} | Entrenamiento: {persona[2]} | Enfoque: {persona[3]}")
    print("(Deja en blanco para no cambiar el campo)")
 
    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_entrenam = input("Nuevo ID de entrenamiento: ")
    print("Enfoques disponibles:")
    mostrar_enfoques()
    nuevo_enfoque = input("Nuevo ID de enfoque: ")
 
    nuevo_nombre = nuevo_nombre if nuevo_nombre else persona[1]
    nuevo_entrenam = nuevo_entrenam if nuevo_entrenam else persona[2]
    nuevo_enfoque = nuevo_enfoque if nuevo_enfoque else persona[3]
 
    cursor.execute(
        "UPDATE Persona SET nombre = ?, id_entrenam = ?, id_enfoque = ? WHERE id = ?",
        (nuevo_nombre, nuevo_entrenam, nuevo_enfoque, id_actualizar)
    )
 
    conexion.commit()
    print(f"Persona con ID {id_actualizar} actualizada correctamente.")
    conexion.close()
 
 
def menu():
    while True:
        print("Bienvenido al programa de entrenamiento Tr3mb0, seleccione lo que desea hacer:")
        print("1. Agregar persona")
        print("2. Ver personas")
        print("3. Ver todo")
        print("4. Borrar persona")
        print("5. Actualizar persona")
        print("6. Salir")
        opcion = input("Elige una opción: ")
 
        if opcion == "1":
            agregar_persona()
        elif opcion == "2":
            ver_personas()
        elif opcion == "3":
            ver_todo()
        elif opcion == "4":
            borrar_persona()
        elif opcion == "5":
            actualizar_persona()
        elif opcion == "6":
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida.")
 
 
if __name__ == "__main__":
    menu()
