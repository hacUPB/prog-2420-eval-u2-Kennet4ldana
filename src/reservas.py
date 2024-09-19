
import random

def sistema_reservas():
    titulo = input("¿Es usted señor o señora?: ").capitalize()
    nombre = input("Introduce tu nombre: ").capitalize()
    apellido = input("Introduce tu apellido: ").capitalize()
    print(f"\n{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!\n")
    
    ciudades = ['Medellin', 'Bogota', 'Cartagena']
    origen = input("Ingresa tu origen (Medellín, Bogotá, Cartagena): ").capitalize()
    while origen not in ciudades:
        origen = input("Por favor, ingresa un origen válido (Medellín, Bogotá, Cartagena): ").capitalize()
    
    destino = input("Ingresa tu destino (Medellín, Bogotá, Cartagena): ").capitalize()
    while destino not in ciudades or destino == origen:
        if destino == origen:
            destino = input("El destino no puede ser el mismo que el origen. Ingresa otro destino: ").capitalize()
        else:
            destino = input("Por favor, ingresa un destino válido (Medellín, Bogotá, Cartagena): ").capitalize()
    
    dia_semana = input("Ingrese el día de la semana (por ejemplo, lunes): ").lower()
    dia_mes = int(input("Introduzca el día del mes (1-30): "))
    
    distancias = {
        ('Medellin', 'Bogotá'): 240,
        ('Medellin', 'Cartagena'): 461,
        ('Bogota', 'Cartagena'): 657
    }
    
    distancia = distancias.get((origen, destino)) or distancias.get((destino, origen))
    
    if distancia < 400:
        if dia_semana in ['lunes', 'martes', 'miércoles', 'jueves']:
            precio = 79900
        else:
            precio = 119900
    else:
        if dia_semana in ['lunes', 'martes', 'miércoles', 'jueves']:
            precio = 156900
        else:
            precio = 213000
    
    preferencia_asiento = input("¿Prefiere asiento en el pasillo, junto a la ventana, o no tiene preferencia?: ").lower()
    if preferencia_asiento == 'pasillo':
        asiento_letra = 'C'
    elif preferencia_asiento == 'ventana':
        asiento_letra = 'A'
    else:
        asiento_letra = 'B'
    
    numero_asiento = random.randint(1, 29)
    
    print(f"\nTu vuelo de {origen} a {destino} del {dia_semana} {dia_mes} está reservado.")
    print(f"Precio del boleto: ${precio:,}")
    print(f"Tu asiento es: {numero_asiento}{asiento_letra}")

if __name__ == "__main__":
    sistema_reservas()
