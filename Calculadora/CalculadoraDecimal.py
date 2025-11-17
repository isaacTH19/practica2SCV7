print("╔══════════════════════════════════════╗")
print("║      CONVERSOR DECIMAL → BINARIO     ║")
print("╠══════════════════════════════════════╣")


while True:
    numero = int(input("\nIngresa un número decimal: "))
    binario = ""

    if numero == 0:
        binario = "0"
    else:
        while numero > 0:
            residuo = numero % 2
            binario = str(residuo) + binario
            numero = numero // 2

    print("Número en binario:", binario)

    opcion = input("\n¿Deseas convertir otro número? (s/n): ").lower()

    if opcion != "s":
        print("\nGracias por usar el convertidor  ¡Hasta pronto! ")
        break  
