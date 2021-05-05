import Modelo.Mod_operacion as Mop

class Registros:

    def Nueva_operacion(self,fecha_ini,fecha_fin,operacion,nota):

        nuevo_registro=Mop.Operacion(fecha_ini,fecha_fin,operacion,nota)
        print(nuevo_registro.__str__())


