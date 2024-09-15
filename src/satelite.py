def simular_desintegracion_orbital():
    altitud_actual = float(input("Ingresa la altitud inicial del satélite (en kilómetros): "))
    coeficiente_arrastre = float(input("Ingresa el coeficiente de arrastre inicial (por ejemplo, 0.01): "))
    altitud_minima_seguridad = float(input("Ingresa la altitud mínima de seguridad (en kilómetros): "))
    
    orbita = 0
    altitud_perdida = 1  


    while altitud_actual > altitud_minima_seguridad and altitud_perdida > 0.01:

        altitud_perdida = coeficiente_arrastre * altitud_actual
        

        altitud_actual -= altitud_perdida
        

        coeficiente_arrastre += 0.0001
        
        orbita += 1

    if altitud_actual <= altitud_minima_seguridad:
        print(f"\nEl satélite ha reingresado en la atmósfera terrestre después de {orbita} órbitas.")
    else:
        print(f"\nEl satélite se ha estabilizado en una órbita a una altitud de {altitud_actual:.2f} km después de {orbita} órbitas.")
        
if __name__ == "__main__":
    simular_desintegracion_orbital()
    