
import random

# Listas de títulos válidos
titulos_validos_sr = ["Sr.", "sr.", "Sr", "sr"]
titulos_validos_sra = ["Sra.", "sra.", "Sra", "sra"]

# Pedir el título hasta que sea válido
titulo = input("Ingrese su título (Sr. o Sra.): ")
while titulo not in titulos_validos_sr + titulos_validos_sra:
    print("Título no válido. Por favor, ingrese 'Sr.' o 'Sra.'.")
    titulo = input("Ingrese su título (Sr. o Sra.): ")

# Pedir el nombre y apellido
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Determinar y mostrar el mensaje correcto
if titulo in titulos_validos_sr:
    print(f"Sr. {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!")
else:
    print(f"Sra. {nombre} {apellido}, ¡Bienvenida a FastFast Airlines!")



distancias = { 

    ("Medellín", "Bogotá"): 240, 

    ("Medellín", "Cartagena"): 461, 

    ("Bogotá", "Cartagena"): 657 

} 


origen = input("Seleccione su ciudad de origen (Medellín, Bogotá, Cartagena): ") .lower()
destino = input("Seleccione su ciudad de destino (Medellín, Bogotá, Cartagena): ") 
dia_semana = input("Ingrese el día de la semana en que desea viajar (por ejemplo, lunes): ").lower() 
dia_mes = int(input("Ingrese el día del mes en que desea viajar (1-30): ")) 


distancia = distancias.get((origen, destino)) or distancias.get((destino, origen))
print(distancia)

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
