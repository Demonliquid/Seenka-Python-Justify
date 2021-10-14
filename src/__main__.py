from string_justify import Justify

if __name__ == "__main__":
    string = input("Pegar texto largo")
    maximo = int(input("Columna maxima"))
    print(Justify(string, maximo))
