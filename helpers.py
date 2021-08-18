from concurrent.futures import ThreadPoolExecutor
import queries


def ingresar(id_boleto):
    try:
        executor = ThreadPoolExecutor(max_workers=3)
        acceso_correcto = executor.submit(queries.set_cliente_verificado, id_boleto)
        return acceso_correcto.result()       

    except:
        return False

