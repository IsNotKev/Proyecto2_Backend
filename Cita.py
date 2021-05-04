class Cita:
    def __init__(self,paciente,doctor,fecha,hora,motivo,estado):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado
    
    #Getter

    def getPaciente(self):
        return self.paciente

    def getDoctor(self):
        return self.doctor

    def getFecha(self):
        return self.fecha
    
    def getHora(self):
        return self.hora

    def getMotivo(self):
        return self.motivo

    def getEstado(self):
        return self.estado
    
    #Setter

    def setDoctor(self, doctor):
        self.doctor = doctor
    
    def setFecha(self, fecha):
        self.fecha = fecha
    
    def setHora(self, hora):
        self.hora = hora
    
    def setMotivo(self, motivo):
        self.motivo = motivo

    def setEstado(self, estado):
        self.estado = estado
    