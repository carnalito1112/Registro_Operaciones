class Operacion :

    def __init__(self, fecha_ini, fecha_fin, operacion, nota):
        self.fecha_ini = fecha_ini
        self.fecha_fin= fecha_fin
        self.operacion= operacion
        self.nota = nota


    def __str__(self):
        return "{},{},{},{}".format(self.fecha_ini,self.fecha_fin,self.operacion, self.nota)




#p= Operacion("21/05/2001","22/05/2021","venta","holaaa como estas culitoo")

#print(p.__str__())