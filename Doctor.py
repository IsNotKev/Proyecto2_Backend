class Doctor:

    def __init__(self,nombre,apellido,nacimiento,sexo,usuario,contra,especialidad,telefono,aceptadas):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.sexo = sexo
        self.usuario = usuario
        self.contra = contra
        self.especialidad = especialidad
        self.telefono = telefono
        self.aceptadas = aceptadas


    #GETTERS

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getNacimiento(self):
        return self.nacimiento

    def getSexo(self):
        return self.sexo
    
    def getUsuario(self):
        return self.usuario

    def getContra(self):
        return self.contra

    def getEspecialidad(self):
        return self.especialidad

    def getTelefono(self):
        return self.telefono

    def getAceptadas(self):
        return self.aceptadas

    #SETTERS

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido

    def setNacimiento(self, nacimiento):
        self.nacimiento = nacimiento

    def setSexo(self, sexo):
        self.sexo = sexo

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setContra(self, contra):
        self.contra = contra

    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setAceptadas(self, aceptadas):
        self.aceptadas = aceptadas