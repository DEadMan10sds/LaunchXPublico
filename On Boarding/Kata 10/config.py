from msilib.schema import File


def main():
    try:
        configuration = open('config.txt')
    except OSError as err:
        if err.errno == 2:
            print("No se pudo encontrar el archivo")
        else:
            print("Se encontró el archivo pero no se pudo")
    except FileNotFoundError as err: #Al agregar el 'as' asignamos el error a una variable y podemos acceder a el (como en java), así mejoramos los errores y retroalimentación
        print('No se pudo encontrar el archivo: ', err)
    except IsADirectoryError:
        print('El archivo se encontró en una dirección distinta')
    except (BlockingIOError, TimeoutError): #Se pueden incluir más de 1 error en una excepción
        print('Archivo bajo proceso pesado, no se puede leer el archivo')

if __name__ == '__main__':
    main()