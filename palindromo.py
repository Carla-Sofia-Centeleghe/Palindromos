# Palindromos
# Carla S. Centeleghe

# Funcion que recorre la palabra y compara con su inversa
def palindromo(palabra):
    for i in range(0, int(len(palabra))):
        if palabra[i] != palabra[-i-1]:
            return False
        return True


if __name__ == "__main__":
    palabra = input("Elija una palabra: ")
    print(palindromo(palabra))
