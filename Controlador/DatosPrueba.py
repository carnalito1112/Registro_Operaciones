

import Conexion.db_conexion as conn


class ConEntrada:



    def datos_tabla(self):
        #lista = [("1", "11/05/21", "00/00/0000", "compra", "50", "holaaa esto es una notaa", "link", "link"),
        #         ("2",  "11/05/21", "00/00/0000", "compra", "50", "holaaa esto es una notaa", "link", "link"),
        #         ("3",  "11/05/21", "00/00/0000", "compra", "50", "holaaa esto es una notaa", "link", "link")]
        obj_conexion = conn.dbconexion()
        conexion = obj_conexion.conexion()

        cursor = conexion.cursor()
        cursor.execute("SELECT op_id_operacion,op_fecha_entrada,op_fecha_salida,op_operacion,op_gan_per,op_nota,op_ruta_imagen_ent,op_ruta_imagen_sal FROM tb_operaciones ORDER BY op_id_operacion DESC ;")
        lista = cursor.fetchall()

        #print(lista)

        conexion.commit()
        conexion.close()

        return lista

