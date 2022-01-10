from datetime import datetime

def data_op(func):
    def decorator(*args, **kwargs):
        print(datetime.now())

        return func(*args, **kwargs)

    return decorator

@data_op
def soma_legal(num1 : int, num2 : int) -> datetime:
    """Esta função faz a seguinte operação: num1 + num2 * 2"""
    return num1 + num2 * 2

print(soma_legal(2, 3))