class Operacion :

    fecha_ini = ""
    fecha_fin = ""
    operacion= ""
    nota = ""
    ruta_img_entrada=""
    ruta_img_salida=""
    gan_perd =0
    # def __init__(self, fecha_ini, fecha_fin, operacion, nota):
    #     self.fecha_ini = fecha_ini
    #     self.fecha_fin= fecha_fin
    #     self.operacion= operacion
    #     self.nota = nota


    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.fecha_ini,self.fecha_fin,self.gan_perd,self.operacion, self.nota,self.ruta_img_salida,self.ruta_img_entrada)

    def set_fecha_ini(self,fecha_ini):
        self.fecha_ini=fecha_ini

    def get_fecha_ini(self):
        return self.fecha_ini

    def set_fecha_fin(self,fecha_fin):
        self.fecha_fin=fecha_fin

    def get_fecha_fin(self):
        return self.fecha_fin

    def set_operacion(self,operacion):
        self.operacion=operacion

    def get_operacion(self):
        return self.operacion

    def set_nota(self,nota):
        self.nota=nota

    def get_nota(self):
        return self.nota

    def set_ruta_img_entrada(self,ruta_img_entrada):
        self.ruta_img_entrada=ruta_img_entrada

    def get_ruta_img_entrada(self):
        return self.ruta_img_entrada

    def set_ruta_img_salida(self,ruta_img_salida):
        self.ruta_img_salida=ruta_img_salida

    def get_ruta_img_salida(self):
        return self.ruta_img_salida

    def set_gan_perd (self,gan_perd):
        self.gan_perd=gan_perd

    def get_gan_perd(self):
        return self.gan_perd


#p= Operacion("21/05/2001","22/05/2021","venta","h olaa")

#print(p.__str__())
