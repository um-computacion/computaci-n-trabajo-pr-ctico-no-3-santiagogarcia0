from exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    entrada = input("Ingrese un número: ")
    try:
        numero = int(entrada)
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")
    
    if numero < 0:
        raise NumeroDebeSerPositivo("El número debe ser positivo")
    
    return numero

if __name__ == "__main__":
    try:
        numero = ingrese_numero()
        print(f"Número válido: {numero}")
    except ValueError:
        print("Error: La entrada debe ser un número válido")
    except NumeroDebeSerPositivo:
        print("Error: El número debe ser positivo")

