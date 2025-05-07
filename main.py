from operaciones import sumar, restar


def mostrar_menu():
    print("\n--- Seleccione una operación Calculadora Modular ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    
def main():
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")
        
        if opcion == '3':
            print("Saliendo de la calculadora...")
            break
        
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            operaciones = {
                '1': sumar,
                '2': restar
            }
            
            if opcion in operaciones:
                resultado = operaciones[opcion](num1, num2)
                if resultado is not None:
                    print(f"El resultado es: {resultado}")
                else:
                    print("Error en la operación.")
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Error: Por favor, ingrese números válidos.")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()