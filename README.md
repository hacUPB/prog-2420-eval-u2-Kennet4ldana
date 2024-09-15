[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/e28MnG35)
# Documentación del proyecto
## Unidad 2

Estudiante:  Jhon Kennet Aldana Oviedo
ID:  000462009


*PROBLEMA 1*

Sistema de reservas de aerolineas  

_Ingresa usuario:_

Nombre, apellido y señor u señora 

Ciudad de origen 

Ciudad de destino 

Dia de viaje  

Pregunta de asiento (preferencia) 

_Variable:_

 Destino (medellin, bogota, cartagena) 

Dia de viaje 

Asiento (1-29) y (A, B, C) 

_Constantes:_ 

Distancia entre ciudades  

Distancia <400 y >400 con él día del viaje 

Asientos (1 a 29) 

_Entrada:_

Calculo del precio del tiquete según la distancia 

Asiento según la preferencia 

Día del vuelo 

_Salida:_

Nombre, apellido y señor u señora 

Precio según la distancia y el día  

Asignación de asiento 

Fecha de vuelo 

Origen y destino 

Resumen de la reserva 

 

*Paso a paso* 

_Paso 1_

Se le pide la información personal al usuario (nombre, apellido y señor u señora), luego se muestra su saludo respectivamente personalizado  

_Paso 2_

Se define las variables distancia con sus respectivas opciones y parametros del ejercicio. Luego se le pide al usuario su lugar de origen y su destino  

_Paso 3_

Se pide la fecha del día que desear viajar la persona y se organizan sus parametros según los precios de los días  

_Paso 4_

Se calcula la distancia entre el origen y el destino del usuario  

_Paso 5_ 

Se calcula el precio del tiquete según el día que selecciono la persona, la distancia entre el origen y el destino  

Acaba este bucle 

*Para la asignación del asiento:* 

_Paso 1_

Se le pregunta al usuario si tiene preferencias, cual y también si no tiene  

_Paso 2_ 

Se le asigna el asiento según sus preferencias y disponibilidad en el vuelo dandole valores a estas preferencias a letras para luego seleccionar un numero de asiento aleatorio entre 1 y 29 

_Paso 3_

Mostrar su respectivo resumen con datos personales y del vuelo 

*DIAGRAMA DE FLUJO*

https://lucid.app/lucidchart/2e5553fe-346c-4ab2-9abf-0f1e294bce3e/edit?viewport_loc=-3274%2C610%2C4576%2C2041%2C0_0&invitationId=inv_175d6989-8ed5-49b2-a744-3d936135c23a 

Rubrica de evaluación: 

 

Insuficiente [1-2,9) 

Basico (3-3,5) 

Bueno [3,5-4) 

Muy bueno [4-4.5) 

Excelente [4,5-5) 

Autoevaluación  

Asistencia y participación 

Faltar a bastantes clases o al ir no participar adecuadamente  

Participar muy poco y/o va a algunas clases llegando de manera puntual a estas  

Participa en clase y asiste de manera puntual a dichas clases 

Participa activamente en las clases y asiste a todas las clases 

Particpa en clase acertivamente, asiste a clases y aparte fuera de las clases pregunta y avanza en dicha entrega 

1.5 

Evidencias 

No presenta los implementos pedidos completos o no todos 

Presenta las evidencias incompletas o de manera desordenada 

Presenta evidencias de manera sosa y sin mucha coherencia  

Presenta la información con algunas incongrenecias con el codigo  

Presenta rubricas, paso a paso, explicación del codigo y demás de manera completa 

3.8 

Codigo 

Codigo incompleto y desorganizado  

Codigo con algunas incongruencias o no cumple con algún parametro 

Codigo completo pero no muy claro en la información pedida  

Codigo completo pero con algunas funciones no muy necesarias o de las vistas 

Codigo completo y organizado con la información clara  

3.8 

Presentación  

Desorganizado el codigo y el repositorio donde la información no es muy clara y concisa  

Desorganizado el codigo o el repositorio de manera que no es muy clara la información  

Organizado el repositorio pero no muy clara la información  

Codigo y repositorio organizados pero no muy claros o con algunas cosas no muy claras 

Presenta el codigo y el repositorio completo de manera ordenada y clara  

3.6 

 

Explicación del código: 

Este código toma los datos del usuario (nombre, origen, destino, preferencia de asiento, etc.), calcula el precio del vuelo en función de la distancia y el día de la semana, asigna un asiento aleatorio y luego imprime un resumen completo de la reserva. 

Pidiendo datos, variables, parametros y demás como lo son: 

Import random que se encarga de importar de la librería la función random que nos da números aleatorios para funciones de aleatoriedad 

Se piden datos para dar la bienvenida (nombre, apellido, titulo) 

Se definen los parámetros de distancias y las diferencias (medellin, bogota, cartagena) 

Se solicita la ciudad de destino y el origen, también el día de la semana y del mes que se desea viajar 

Se calcula de la diferencia de distancias, ya que de esta variable depende el precio del tiquete, como también la variable según el día de la semana que la persona desea viajar 

Se piden preferencias de asiento según los gustos del usuario y se le asignan parametros a la variable asiento (A, B, Y C) 

Se asigna el asiento según la disponibilidad del vuelo y las preferencias del usuario 

Por último, se imprime un resumen de la reserva del usuario según todo lo pedido y asignado anteriormente (nombre, apellido, titulo, origen, destino, día del vuelo, precio del asiento y asiento asignado) 

---
