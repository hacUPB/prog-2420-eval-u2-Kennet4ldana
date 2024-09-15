
def main():
      #Tu código va aquí"
    pass # borra esta línea cuando con inicies tu código"


if __name__ == "__main__":
    main()

### Paso 1: Importar las bibliotecas necesarias 

import random

titulo = input("Ingrese su título (Sr. o Sra.): ") 

nombre = input("Ingrese su nombre: ") 

apellido = input("Ingrese su apellido: ") 

#Fecha = input("Ingrese fecha actual(Ej:12/03/24):")



  

print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!") 


distancias = { 

    ("Medellín", "Bogotá"): 240, 

    ("Medellín", "Cartagena"): 461, 

    ("Bogotá", "Cartagena"): 657 

} 


origen = input("Seleccione su ciudad de origen (Medellín, Bogotá, Cartagena): ") 

destino = input("Seleccione su ciudad de destino (Medellín, Bogotá, Cartagena): ") 

dia_semana = input("Ingrese el día de la semana en que desea viajar (por ejemplo, lunes): ").lower() 

dia_mes = int(input("Ingrese el día del mes en que desea viajar (1-30): ")) 

#while True:
    #try:
        #dia_mes = int(input("Ingrese el día del mes en que desea viajar (1-30): "))
        #if 1 <= dia_mes <= 30:
        #    break
        #else:
        #    print("Por favor, ingrese un número entre 1 y 30.")
    #except ValueError:
        #print("Por favor, ingrese un número válido.")

distancia = distancias.get((origen, destino)) or distancias.get((destino, origen)) 


if distancia < 400: 

    if dia_semana in ["lunes", "martes", "miércoles", "jueves"]: 

        precio = 79900 

    else: 

        precio = 119900 

else: 

    if dia_semana in ["lunes", "martes", "miércoles", "jueves"]: 

        precio = 156900 

    else: 

        precio = 213000


preferencia_asiento = input("¿Prefiere un asiento en el pasillo, junto a la ventana o sin preferencia? ").lower() 
  

if preferencia_asiento == "pasillo": 

    letra_asiento = "C" 

elif preferencia_asiento == "ventana": 

    letra_asiento = "A" 

else: 

    letra_asiento = "B" 


numero_asiento = random.randint(1, 29) 

asiento = f"{numero_asiento}{letra_asiento}" 

print("\nResumen de su reserva:") 

print(f"Nombre: {titulo} {nombre} {apellido}") 

print(f"Origen: {origen}") 

print(f"Destino: {destino}") 

print(f"Fecha de vuelo: {dia_semana.capitalize()}, {dia_mes}") 

print(f"Precio del boleto: ${precio:,}") 

print(f"Asiento asignado: {asiento}") 


import random 


titulo = input("Ingrese su título (Sr. o Sra.): ") 

nombre = input("Ingrese su nombre: ") 

apellido = input("Ingrese su apellido: ") 

print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!") 

distancias = { 

    ("Medellín", "Bogotá"): 240, 

    ("Medellín", "Cartagena"): 461, 

    ("Bogotá", "Cartagena"): 657 

} 

  

origen = input("Seleccione su ciudad de origen (Medellín, Bogotá, Cartagena): ") 

destino = input("Seleccione su ciudad de destino (Medellín, Bogotá, Cartagena): ") 

dia_semana = input("Ingrese el día de la semana en que desea viajar (por ejemplo, lunes): ").lower() 

dia_mes = int(input("Ingrese el día del mes en que desea viajar (1-30): ")) 

  
distancia = distancias.get((origen, destino)) or distancias.get((destino, origen)) 

  

if distancia < 400: 

    if dia_semana in ["lunes", "martes", "miércoles", "jueves"]: 

        precio = 79900 

    else: 

        precio = 119900 

else: 

    if dia_semana in ["lunes", "martes", "miércoles", "jueves"]: 

        precio = 156900 

    else: 

        precio = 213000 



preferencia_asiento = input("¿Prefiere un asiento en el pasillo, junto a la ventana o sin preferencia? ").lower() 


if preferencia_asiento == "pasillo": 

    letra_asiento = "C" 

elif preferencia_asiento == "ventana": 

    letra_asiento = "A" 

else: 

    letra_asiento = "B" 

  

numero_asiento = random.randint(1, 29) 

asiento = f"{numero_asiento}{letra_asiento}" 

print("\nResumen de su reserva:") 

print(f"Nombre: {titulo} {nombre} {apellido}") 

print(f"Origen: {origen}") 

print(f"Destino: {destino}") 

print(f"Fecha de vuelo: {dia_semana.capitalize()}, {dia_mes}") 

print(f"Precio del boleto: ${precio:,}") 

print(f"Asiento asignado: {asiento}") 
