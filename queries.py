from conexion import Conexion 

c = Conexion()
conn = c.crear_conexion()

def get_boletos(id_puerta_acceso):
    '''
    Boleto: id_boleto, fecha_hora_compra_boleto
    Ciente: Nombre Cliente = id_cliente, nombre_cliente, apellido_p_cliente, apellido_m_cliente
    Tipo cliente: id_tipo_cliente, nombre_tipo_cliente
    '''
    try:
        with conn.cursor() as cursor:
            sql = f'SELECT b.id_boleto, b.fecha_hora_compra_boleto, b.id_usuario, u.nombre_usuario, u.apellido_p_usuario, u.apellido_m_usuario, u.id_tipo_cliente, tc.nombre_tipo_cliente FROM boletos b, usuarios u, tipos_clientes tc WHERE b.id_usuario=u.id_usuario AND u.id_tipo_cliente=tc.id_tipo_cliente AND b.id_puerta_acceso={id_puerta_acceso} AND b.id_concierto=1 AND b.verificado_boleto=0 ORDER BY tc.nombre_tipo_cliente DESC LIMIT 10'

            cursor.execute(sql)
            res = cursor.fetchall()

            if res:
                boletos = []
                for r in res:
                    boleto = {'id_boleto': r[0], 'fecha_hora_compra_boleto': r[1],'id_usuario': r[2], 'nombre_usuario': r[3], 'apellido_p_usuario': r[4], 'apellido_m_usuario': r[5], 'id_tipo_cliente': r[6], 'nombre_tipo_cliente': r[7]}
                    boletos.append(boleto)

                return boletos
            else:
                return False
    except:
        return False



def get_concierto(id_concierto):
    try:
        with conn.cursor() as cursor:
            sql = f'SELECT nombre_artista FROM boletos b, conciertos c, artistas a WHERE b.id_concierto=c.id_concierto AND c.id_artista=a.id_artista AND b.id_concierto={id_concierto}'

            cursor.execute(sql)
            res = cursor.fetchone()

            if res:
                return res[0]
            else:
                return False
    except:
        return False


def verificar_ingreso(id_boleto):
    try:
        with conn.cursor() as cursor:
            sql = f'SELECT verificado_boleto FROM boletos WHERE id_boleto={id_boleto}'
            cursor.execute(sql)
            res = cursor.fetchone()

            if res:
                return res[0] == 1
            else:
                return False
    except:
        return False

def set_cliente_verificado(id_usuario):
    try:
        with conn.cursor() as cursor:
            sql = f'UPDATE boletos SET verificado_boleto=1 WHERE id_usuario={id_usuario}'
            cursor.execute(sql)
            conn.commit()

            return True
    except:
        return False

def insertar_empleado(empleado):
    try:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO empleados(nombre_empleado, apellido_p_empleado, apellido_m_empleado, fecha_nac_empleado, correo_elec_empleado, password_empleado) VALUES('{empleado['nombre_empleado']}','{empleado['apellido_p_empleado']}','{empleado['apellido_m_empleado']}','{empleado['fecha_nac_empleado']}', '{empleado['correo_elec_empleado']}', '{empleado['password_empleado']}')"
            cursor.execute(sql)
            conn.commit()

            return True
    except:
        return False

def set_empleado_no_disponible(id_empleado):
    try:
        with conn.cursor() as cursor:
            sql = f"UPDATE empleados SET disponible_empleado=0 WHERE id_empleado={id_empleado}"
            cursor.execute(sql)
            conn.commit()

            return True
    except:
        return False

def set_empleado_disponible(id_empleado):
    try:
        with conn.cursor() as cursor:
            sql = f"UPDATE empleados SET disponible_empleado=1 WHERE id_empleado={id_empleado}"
            cursor.execute(sql)
            conn.commit()

            return True
    except:
        return False


def set_aceptado_boleto(id_boleto):
    try:
        with conn.cursor() as cursor:
            sql = f"UPDATE boletos SET aceptado_boleto=1 WHERE id_boleto={id_boleto}"
            cursor.execute(sql)
            conn.commit()

            return True
    except:
        return False

def get_nombre_empleado(id_empleado):
    try:
        with conn.cursor() as cursor:
            sql = f"SELECT nombre_empleado, apellido_p_empleado, apellido_m_empleado FROM empleados WHERE id_empleado={id_empleado}"
            cursor.execute(sql)
            res = cursor.fetchone()
            
            return f'{res[0]} {res[1]} {res[2]}' if res else False

    except:
        return False


def login(correo_elec_empleado, password_empleado):
    try:
        with conn.cursor() as cursor:
            sql = f"SELECT id_empleado FROM empleados WHERE correo_elec_empleado='{correo_elec_empleado}' AND password_empleado='{password_empleado}'"
            cursor.execute(sql)
            res = cursor.fetchone()
            return res[0] if res else False
            
    except:
        return False


def datos_concierto(id_concierto, n_aceptados_p1, n_aceptados_p2, n_aceptados_p3, n_total, n_rechazados, n_duplicados):
    try:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO datos_concierto VALUES({id_concierto}, {n_aceptados_p1}, {n_aceptados_p2}, {n_aceptados_p3}, {n_total}, {n_rechazados}, {n_duplicados})"
            cursor.execute(sql)
            conn.commit()

            return True
    except:
        return False


def get_boletos_puerta_cerrada():
    try:
        with conn.cursor() as cursor:
            sql = f"SELECT b.id_boleto, b.fecha_hora_compra_boleto, b.id_usuario, u.nombre_usuario, u.apellido_p_usuario, u.apellido_m_usuario, u.id_tipo_cliente, tc.nombre_tipo_cliente FROM boletos b, usuarios u, tipos_clientes tc WHERE b.id_usuario=u.id_usuario AND u.id_tipo_cliente=tc.id_tipo_cliente AND b.id_concierto=1 AND b.verificado_boleto=0 ORDER BY tc.nombre_tipo_cliente DESC LIMIT 10"
            cursor.execute(sql)
            res = cursor.fetchall()

            if res:
                boletos = []
                for r in res:
                    boleto = {'id_boleto': r[0], 'fecha_hora_compra_boleto': r[1],'id_usuario': r[2], 'nombre_usuario': r[3], 'apellido_p_usuario': r[4], 'apellido_m_usuario': r[5], 'id_tipo_cliente': r[6], 'nombre_tipo_cliente': r[7]}
                    boletos.append(boleto)

                return boletos
            else:
                return False
    except:
        return False

def get_total_boletos_por_concierto(id_concierto):
    try:
        with conn.cursor() as cursor:
            sql = f"SELECT COUNT(*) FROM boletos WHERE id_concierto={id_concierto} AND verificado_boleto=0"
            cursor.execute(sql)
            res = cursor.fetchone()

            if res:
                return res[0]
            else:
                return False
    except:
        return False

def get_total_boletos_por_puerta(id_concierto):
    try:
        with conn.cursor() as cursor:
            sql = f"SELECT COUNT(*) FROM boletos WHERE id_puerta_acceso=1 AND id_concierto={id_concierto}"
            cursor.execute(sql)
            res = cursor.fetchone()
            puerta1 = res[0] if res else 0
            sql = f"SELECT COUNT(*) FROM boletos WHERE id_puerta_acceso=2 AND id_concierto={id_concierto}"
            cursor.execute(sql)
            res = cursor.fetchone()
            puerta2 = res[0] if res else 0
            sql = f"SELECT COUNT(*) FROM boletos WHERE id_puerta_acceso=1 AND id_concierto={id_concierto}"
            cursor.execute(sql)
            res = cursor.fetchone()
            puerta3 = res[0] if res else 0

            return {'puerta1':puerta1, 'puerta2': puerta2,'puerta3':puerta3}
    except:
        return False

