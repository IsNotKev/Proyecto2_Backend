class Medicamento:
    def __init__(self,id,nombre,precio,descripcion,cant,vendidos):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cant = cant
        self.vendidos = vendidos

    #GETTERS
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio

    def getDescripcion(self):
        return self.descripcion
    
    def getCant(self):
        return self.cant

    def getVendidos(self):
        return self.vendidos
    
    #SETTERS
    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrecio(self, precio):
        self.precio = precio

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def setCant(self, cant):
        self.cant = cant

    def setVendidos(self, vendidos):
        self.vendidos = vendidos