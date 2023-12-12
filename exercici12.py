# Funciones auxiliares
def menu_principal():
    print("""
    Menú Principal de la Calculadora:
    1. Números enteros
    2. Números reales
    3. Conversiones de base
    0. Salir
    """)
    opcion = input("Seleccione la opción que desee: ")
    return opcion

def menu_enteros():
    print("""
        Menú de la Calculadora de Números Enteros:
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Potencia
        6. Módulo
        7. Cociente
        0. Salir
        """)
    opcion = input("Seleccione la opción que desee: ")
    return opcion

def menu_reales():
    print("""
        Menú de la Calculadora de Números Reales:
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Potencia
        0. Salir
        """)
    opcion = input("Seleccione la opción que desee: ")
    return opcion

def menu_conversiones_base():
    print("""
        Menú de la Calculadora de Conversiones de Base:
        1. Convertir de binario a decimal, octal y hexadecimal
        2. Convertir de octal a binario, decimal y hexadecimal
        3. Convertir de decimal a binario, octal y hexadecimal
        4. Convertir de hexadecimal a binario, octal y decimal
        0. Salir
        """)
    opcion = input("Seleccione la opción que desee: ")
    return opcion

# Funciones para reducir el número de funciones convirtiendo entre bases
# ...

# Programa principal de la calculadora
opcion = "1"
while opcion != "0":
    if opcion != "0":
        opcion = menu_principal()
    match opcion:
        case "1":  # Calculadora de Números Enteros
            sub_opcion = menu_enteros()
            if sub_opcion != "0":
                a = int(input("Ingrese el primer operando: "))
                b = int(input("Ingrese el segundo operando: "))
            match sub_opcion:
                # Operaciones para números enteros
                # ...
                case "0":
                    print("Adiós")
                    opcion = "0"
                case _:
                    print("Opción no válida")
        case "2":  # Calculadora de Números Reales
            sub_opcion = menu_reales()
            if sub_opcion != "0":
                a = float(input("Ingrese el primer operando: "))
                b = float(input("Ingrese el segundo operando: "))
            match sub_opcion:
                # Operaciones para números reales
                # ...
                case "0":
                    print("Adiós")
                    opcion = "0"
                case _:
                    print("Opción no válida")
        case "3":  # Calculadora de Conversiones de Base
            sub_opcion = menu_conversiones_base()
            if sub_opcion != "0":
                a = input("Ingrese el número a convertir: ")
            match sub_opcion:
                # Operaciones para conversiones de base
                # ...
                case "0":
                    print("Adiós")
                    opcion = "0"
                case _:
                    print("Opción no válida")
        case "0":
            print("Adiós")
            opcion = "0"
        case _:
            print("Adiós")
            opcion = "0"
