from datetime import datetime

# desta forma definimos um decorador
def data_op(func):
    def decorator(*args, **kwargs):
        # aqui vao inseridas as funcionalidades do decorador

        print(datetime.now())

        # permite que a funcao consiga retornar apropriadamente qualquer valor 
        return func(*args, **kwargs)

    return decorator

# como instanciamos o decorador
@data_op
def soma_legal(num1 : int, num2 : int) -> datetime:
    """Esta função faz a seguinte operação: num1 + num2 * 2"""
    return num1 + num2 * 2

# testando
#print(soma_legal(2, 3))