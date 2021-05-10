class Operacion :

    fecha_ini = ""
    fecha_fin = ""
    operacion= ""
    nota = ""
    # def __init__(self, fecha_ini, fecha_fin, operacion, nota):
    #     self.fecha_ini = fecha_ini
    #     self.fecha_fin= fecha_fin
    #     self.operacion= operacion
    #     self.nota = nota


    def __str__(self):
        return "{},{},{},{}".format(self.fecha_ini,self.fecha_fin,self.operacion, self.nota)

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

#p= Operacion("21/05/2001","22/05/2021","venta","holaaa como estas culitoo")

#print(p.__str__())