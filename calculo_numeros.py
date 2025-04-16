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
