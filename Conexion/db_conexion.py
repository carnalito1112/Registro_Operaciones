import sqlite3


class dbconexion:

    def conexion(self):


        conexion= sqlite3.connect('BD\Trading.db')

        return conexion