import psycopg2

class Conexion:

    """Metodo constructor
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=Veterinaria_db user=postgres host=localhost password=postgres")

    """getConexion

        retorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con