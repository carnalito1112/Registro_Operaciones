import Conexion.db_conexion as db_con

class ControlRegistros:

    obj_conexion=db_con.dbconexion()
    def nuevo_registro(self, nuevo_registro):

        conexion= self.obj_conexion.conexion()
        entidades=nuevo_registro.get_fecha_ini(),nuevo_registro.get_fecha_fin(),nuevo_registro.get_gan_perd(),nuevo_registro.get_operacion(),nuevo_registro.get_nota(),nuevo_registro.get_ruta_img_entrada(),nuevo_registro.get_ruta_img_salida(),1
        print(entidades)
        cursor = conexion.cursor()
        cursor.execute('''INSERT INTO tb_operaciones (op_fecha_entrada,op_fecha_salida,op_gan_per,op_operacion,op_nota,op_ruta_imagen_ent,op_ruta_imagen_sal,us_id) VALUES 
            (?,?,?,?,?,?,?,?)
            ''',entidades)
        conexion.commit()
        conexion.close()


    def editar_registro_obtener(self,id):

        conexion=self.obj_conexion.conexion()
        cursor= conexion.cursor()
        cursor.execute("SELECT op_id_operacion,op_fecha_entrada,op_fecha_salida,op_operacion,op_gan_per,op_nota,op_ruta_imagen_ent,op_ruta_imagen_sal FROM tb_operaciones WHERE op_id_operacion=?",(id,))
        item=cursor.fetchall()
        print(item)
        conexion.commit()
        conexion.close()

        return item

    def editar_registro(self, registro_editado, id):

        print(registro_editado.__str__())
        conexion=self.obj_conexion.conexion()
        cursor= conexion.cursor()
        entidades =registro_editado.get_fecha_ini(),registro_editado.get_fecha_fin(),registro_editado.get_operacion(),registro_editado.get_ruta_img_entrada(),registro_editado.get_ruta_img_salida(),id
        cursor.execute("""UPDATE tb_operaciones SET op_fecha_entrada = ?, op_fecha_salida = ?, op_operacion = ?, op_gan_per = 0, op_ruta_imagen_ent = ?, op_ruta_imagen_sal = ? WHERE op_id_operacion = ?""", entidades)
        #cursor.execute("UPDATE tb_operaciones SET op_fecha_entrada=",registro_editado.get_fecha_ini(),", op_fecha_salida=",registro_editado.get_fecha_fin(),",op_operacion=",registro_editado.get_operacion(),",op_gan_per=0,op_ruta_imagen_ent=",registro_editado.get_ruta_img_entrada(),",op_fecha_salida=",registro_editado.get_ruta_img_salida()," WHERE op_id_operacion=?",(id,))
        conexion.commit()
        conexion.close()
        #"""UPDATE tb_operaciones SET op_fecha_entrada = ?, op_fecha_salida = ?, op_operacion = ?, op_gan_per = 0, op_ruta_imagen_ent = ?, op_fecha_salida = ? WHERE op_id_operacion = ?"""
