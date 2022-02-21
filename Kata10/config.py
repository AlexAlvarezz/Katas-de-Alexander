def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt!")
    except IsADirectoryError:
        print("Se encontro el archivo config.txt pero es un directorio, así que no se pudo leer")
    
if __name__ == '__main__':
    main()