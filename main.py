def read_file():
    _file_name = input("Ingresa el nombre del archivo .txt a abrir: ")
    with open(_file_name, "r", encoding="utf-8") as _file:
        _final_file = _file.read()
    print(_final_file)


def write_file():
    _file_name = input("Ingresa el nombre del archivo .txt a abrir: ")
    _to_add = input("\n" + "Ingresa lo que quieras añadir: " + "\n")
    with open(_file_name, "a", encoding="utf-8") as _file:
        _final_file = _file.write(_to_add)
    with open(_file_name, "r", encoding="utf-8") as _readed_file:
        _readed_file = _readed_file.read()
    print(_readed_file)


def rewrite_file():
    _file_name = input("Ingresa el nombre del archivo .txt a abrir: ")
    _to_add = input("\n" + "Ingresa lo que quieras añadir: " + "\n")
    with open(_file_name, "w", encoding="utf-8") as _file:
        _file.write(_to_add)
    with open(_file_name, "r", encoding="utf-8") as _readed_file:
        _readed_file = _readed_file.read()
    print(_readed_file)


"""
def _menu():
    print("Hola! ¿Qué desea hacer?" + "\n 1 - Leer un archivo .txt" + "\n 2 - Añadir texto a un archivo .txt" +
          "\n 3 - Reescribir en un archivo .txt")
    _decision = input("Su elección: ")
    if _decision == "1":
        read_file()
    if _decision == "2":
        write_file()
    if _decision == "3":
        rewrite_file()
    else:
        print("¡Esa opción no existe!")
"""

while True:
    print(
        "Hola! ¿Qué desea hacer?"
        + "\n 1 - Leer un archivo .txt"
        + "\n 2 - Añadir texto a un archivo .txt"
        + "\n 3 - Reescribir en un archivo .txt"
    )
    _decision = input("Su elección: ")
    if _decision == "1":
        read_file()
    elif _decision == "2":
        write_file()
    elif _decision == "3":
        rewrite_file()
    else:
        print("¡Esa opción no existe!")
