from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json
from Persona import Persona
from Doctor import Doctor
from Medicamento import Medicamento
from Cita import Cita

Pacientes = []
Enfermeras = []
Doctores = []
Medicamentos = []
Citas = []
Carrito = []
Enfermedades = []

app = Flask(__name__)           
CORS(app)

@app.route('/', methods=['GET'])
def rutaInicial():
    return ('<h1>UHospital - 202004816</h1>')

#ENFERMEDADES
@app.route('/Enfermedades', methods=['GET'])
def getEnfermedades():
    global Enfermedades

    Datos = []

    for enfermedad in Enfermedades:

        objeto = {
            'Nombre': enfermedad
        }

        Datos.append(objeto)
 
    return(jsonify(Datos))

@app.route('/Enfermedades', methods=['POST'])
def AgregarEnfermedad():

    global Enfermedades

    nombre = request.json['nombre']

    Enfermedades.append(nombre)

    return jsonify({'Mensaje':'Se agrego La Enfermedad exitosamente',})
#PACIENTES

@app.route('/Pacientes', methods=['GET'])
def getPacientes():
    global Pacientes

    Datos = []

    for paciente in Pacientes:

        objeto = {
            'Nombre': paciente.getNombre(),
            'Apellido': paciente.getApellido(),
            'Nacimiento': paciente.getNacimiento(),
            'Sexo': paciente.getSexo(),
            'Usuario': paciente.getUsuario(),
            'Contraseña': paciente.getContra(),
            'Teléfono': paciente.getTelefono()
        }

        Datos.append(objeto)
 
    return(jsonify(Datos))

@app.route('/Pacientes', methods=['POST'])
def AgregarPacientes():

    global Pacientes

    nombre = request.json['nombre']
    apellido = request.json['apellido']
    nacimiento = request.json['nacimiento']
    sexo = request.json['sexo']
    usuario = request.json['usuario']
    contra = request.json['contra']
    telefono = request.json['telefono']

    nuevo = Persona(nombre,apellido,nacimiento,sexo,usuario,contra,telefono)

    Pacientes.append(nuevo)

    return jsonify({'Mensaje':'Se agrego el paciente exitosamente',})

@app.route('/Pacientes/<string:nombre>', methods=['DELETE'])
def EliminarPaciente(nombre):
    global Pacientes

    for i in range(len(Pacientes)):
        if nombre == Pacientes[i].getUsuario():
            del Pacientes[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})      
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

@app.route('/Pacientes/<string:nombre>', methods=['GET'])
def ObtenerPaciente(nombre): 

    global Pacientes

    for paciente in Pacientes:

        if paciente.getUsuario() == nombre:
            objeto = {
            'Nombre': paciente.getNombre(),
            'Apellido': paciente.getApellido(),
            'Nacimiento': paciente.getNacimiento(),
            'Sexo': paciente.getSexo(),
            'Usuario': paciente.getUsuario(),
            'Contraseña': paciente.getContra(),
            'Teléfono': paciente.getTelefono()
            }
            return(jsonify(objeto))  

    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Pacientes/<string:nombre>', methods=['PUT'])
def ActualizarPaciente(nombre):
    global Pacientes

    for i in range(len(Pacientes)):

        if nombre == Pacientes[i].getUsuario():

            Pacientes[i].setNombre(request.json['nombre'])
            Pacientes[i].setApellido(request.json['apellido'])
            Pacientes[i].setNacimiento(request.json['nacimiento'])
            Pacientes[i].setSexo(request.json['sexo'])
            Pacientes[i].setUsuario(request.json['usuario'])
            Pacientes[i].setContra(request.json['contra'])
            Pacientes[i].setTelefono(request.json['telefono'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

#DOCTORES

@app.route('/Doctores', methods=['GET'])
def getDoctores():
    global Doctores

    Datos = []

    for doctor in Doctores:

        objeto = {
            'Nombre': doctor.getNombre(),
            'Apellido': doctor.getApellido(),
            'Nacimiento': doctor.getNacimiento(),
            'Sexo': doctor.getSexo(),
            'Usuario': doctor.getUsuario(),
            'Contraseña': doctor.getContra(),
            'Especialidad': doctor.getEspecialidad(),
            'Teléfono': doctor.getTelefono(),
            'Aceptadas': doctor.getAceptadas()
        }

        Datos.append(objeto)
 
    return(jsonify(Datos))

@app.route('/Doctores', methods=['POST'])
def AgregarDoctor():

    global Doctores

    nombre = request.json['nombre']
    apellido = request.json['apellido']
    nacimiento = request.json['nacimiento']
    sexo = request.json['sexo']
    usuario = request.json['usuario']
    contra = request.json['contra']
    telefono = request.json['telefono']
    especialidad = request.json['especialidad']
    aceptadas = request.json['aceptadas']

    nuevo = Doctor(nombre,apellido,nacimiento,sexo,usuario,contra,especialidad,telefono,aceptadas)

    Doctores.append(nuevo)

    return jsonify({'Mensaje':'Se agrego el Doctor exitosamente',})

@app.route('/Doctores/<string:nombre>', methods=['DELETE'])
def EliminarDoctor(nombre):
    global Doctores

    for i in range(len(Doctores)):
        if nombre == Doctores[i].getUsuario():
            del Doctores[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})      
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

@app.route('/Doctores/<string:nombre>', methods=['GET'])
def ObtenerDoctor(nombre): 

    global Doctores

    for doctor in Doctores:

        if doctor.getUsuario() == nombre:
            objeto = {
            'Nombre': doctor.getNombre(),
            'Apellido': doctor.getApellido(),
            'Nacimiento': doctor.getNacimiento(),
            'Sexo': doctor.getSexo(),
            'Usuario': doctor.getUsuario(),
            'Contraseña': doctor.getContra(),
            'Especialidad': doctor.getEspecialidad(),
            'Teléfono': doctor.getTelefono(),
            'Aceptadas': doctor.getAceptadas()
            }
            return(jsonify(objeto))  

    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Doctores/<string:nombre>', methods=['PUT'])
def ActualizarDoctor(nombre):
    global Doctores

    for i in range(len(Doctores)):

        if nombre == Doctores[i].getUsuario():

            Doctores[i].setNombre(request.json['nombre'])
            Doctores[i].setApellido(request.json['apellido'])
            Doctores[i].setNacimiento(request.json['nacimiento'])
            Doctores[i].setSexo(request.json['sexo'])
            Doctores[i].setUsuario(request.json['usuario'])
            Doctores[i].setContra(request.json['contra'])
            Doctores[i].setTelefono(request.json['telefono'])
            Doctores[i].setEspecialidad(request.json['especialidad'])
            Doctores[i].setAceptadas(request.json['aceptadas'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

#ENFERMERAS

@app.route('/Enfermeras', methods=['GET'])
def getEnfermeras():
    global Enfermeras

    Datos = []

    for enfermera in Enfermeras:

        objeto = {
            'Nombre': enfermera.getNombre(),
            'Apellido': enfermera.getApellido(),
            'Nacimiento': enfermera.getNacimiento(),
            'Sexo': enfermera.getSexo(),
            'Usuario': enfermera.getUsuario(),
            'Contraseña': enfermera.getContra(),
            'Teléfono': enfermera.getTelefono()
        }

        Datos.append(objeto)
 
    return(jsonify(Datos))

@app.route('/Enfermeras', methods=['POST'])
def AgregarEnfermeras():

    global Enfermeras

    nombre = request.json['nombre']
    apellido = request.json['apellido']
    nacimiento = request.json['nacimiento']
    sexo = request.json['sexo']
    usuario = request.json['usuario']
    contra = request.json['contra']
    telefono = request.json['telefono']

    nuevo = Persona(nombre,apellido,nacimiento,sexo,usuario,contra,telefono)

    Enfermeras.append(nuevo)

    return jsonify({'Mensaje':'Se agrego la Enfermera exitosamente',})

@app.route('/Enfermeras/<string:nombre>', methods=['DELETE'])
def EliminarEnfermera(nombre):
    global Enfermeras

    for i in range(len(Enfermeras)):
        if nombre == Enfermeras[i].getUsuario():
            del Enfermeras[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})      
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

@app.route('/Enfermeras/<string:nombre>', methods=['GET'])
def ObtenerEnfermera(nombre): 

    global Enfermeras

    for enfermera in Enfermeras:

        if enfermera.getUsuario() == nombre:
            objeto = {
            'Nombre': enfermera.getNombre(),
            'Apellido': enfermera.getApellido(),
            'Nacimiento': enfermera.getNacimiento(),
            'Sexo': enfermera.getSexo(),
            'Usuario': enfermera.getUsuario(),
            'Contraseña': enfermera.getContra(),
            'Teléfono': enfermera.getTelefono()
            }
            return(jsonify(objeto))  

    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Enfermeras/<string:nombre>', methods=['PUT'])
def ActualizarEnfermera(nombre):
    global Enfermeras

    for i in range(len(Enfermeras)):

        if nombre == Enfermeras[i].getUsuario():

            Enfermeras[i].setNombre(request.json['nombre'])
            Enfermeras[i].setApellido(request.json['apellido'])
            Enfermeras[i].setNacimiento(request.json['nacimiento'])
            Enfermeras[i].setSexo(request.json['sexo'])
            Enfermeras[i].setUsuario(request.json['usuario'])
            Enfermeras[i].setContra(request.json['contra'])
            Enfermeras[i].setTelefono(request.json['telefono'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

#MEDICAMENTOS

@app.route('/Medicamentos', methods=['GET'])
def getMedicamentos():
    global Medicamentos

    Datos = []

    for medicamento in Medicamentos:

        objeto = {
            'Id': medicamento.getId(),
            'Nombre': medicamento.getNombre(),
            'Precio': medicamento.getPrecio(),
            'Descripcion': medicamento.getDescripcion(),
            'Cantidad': medicamento.getCant(),
            'Vendidos': medicamento.getVendidos()
        }

        Datos.append(objeto)
 
    return(jsonify(Datos))

@app.route('/Medicamentos', methods=['POST'])
def AgregarMedicamentos():

    global Medicamentos

    ID = request.json['id']
    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['descripcion']
    cant = request.json['cant']
    vendidos = request.json['vendidos']

    nuevo = Medicamento(ID,nombre,precio,descripcion,cant,vendidos)

    Medicamentos.append(nuevo)

    return jsonify({'Mensaje':'Se agrego el Medicamento exitosamente',})

@app.route('/Medicamentos/<int:nombre>', methods=['DELETE'])
def EliminarMedicamento(nombre):
    global Medicamentos

    for i in range(len(Medicamentos)):
        if nombre == Medicamentos[i].getId():
            del Medicamentos[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})      
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

@app.route('/Medicamentos/<int:nombre>', methods=['GET'])
def ObtenerMedicamento(nombre): 

    global Medicamentos

    for medicamento in Medicamentos:

        if medicamento.getId() == nombre:
            objeto = {
            'Id': medicamento.getId(),
            'Nombre': medicamento.getNombre(),
            'Precio': medicamento.getPrecio(),
            'Descripcion': medicamento.getDescripcion(),
            'Cantidad': medicamento.getCant(),
            'Vendidos': medicamento.getVendidos()
        }
            return(jsonify(objeto))  

    salida = { "Mensaje": "No existe el medicina con ese nombre"}
    return(jsonify(salida))

@app.route('/Medicamentos/<int:nombre>', methods=['PUT'])
def ActualizarMedicamento(nombre):
    global Medicamentos

    for i in range(len(Medicamentos)):

        if nombre == Medicamentos[i].getId():

            Medicamentos[i].setNombre(request.json['nombre'])
            Medicamentos[i].setPrecio(request.json['precio'])
            Medicamentos[i].setDescripcion(request.json['descripcion'])
            Medicamentos[i].setCant(request.json['cant'])
            Medicamentos[i].setVendidos(request.json['vendidos'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})


#CARRITO
@app.route('/Carrito', methods=['POST'])
def AgregarMedicina():

    global Carrito

    ID = request.json['id']
    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['descripcion']
    cant = request.json['cant']
    vendidos = request.json['vendidos']

    nuevo = Medicamento(ID,nombre,precio,descripcion,cant,vendidos)

    Carrito.append(nuevo)

    return jsonify({'Mensaje':'Se agrego la medicina exitosamente',})

@app.route('/Carrito', methods=['GET'])
def getMedicina():
    global Carrito

    Datos = []

    for medicamento in Carrito:

        objeto = {
            'Id': medicamento.getId(),
            'Nombre': medicamento.getNombre(),
            'Precio': medicamento.getPrecio(),
            'Descripcion': medicamento.getDescripcion(),
            'Cantidad': medicamento.getCant(),
            'Vendidos': medicamento.getVendidos()
        }

        Datos.append(objeto)
 
    return(jsonify(Datos))

@app.route('/Carrito/<int:nombre>', methods=['PUT'])
def ActualizarMedicina(nombre):
    global Carrito

    for i in range(len(Carrito)):

        if nombre == Carrito[i].getId():
            Carrito[i].setCant(request.json['cant'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

@app.route('/Carrito/<int:nombre>', methods=['DELETE'])
def EliminarMedicina(nombre):
    global Carrito

    for i in range(len(Carrito)):
        if nombre == Carrito[i].getId():
            del Carrito[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})      
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

@app.route('/Carrito', methods=['DELETE'])
def EliminarCarrito():
    global Carrito

    for i in range(len(Carrito)):
        del Carrito[i-1]
            
    return jsonify({'Mensaje':'Se elimino el Carrito exitosamente'})  

@app.route('/Carrito/<int:nombre>', methods=['GET'])
def ObtenerMedicina(nombre): 

    global Carrito

    for medicamento in Carrito:

        if medicamento.getId() == nombre:
            objeto = {
            'Id': medicamento.getId(),
            'Nombre': medicamento.getNombre(),
            'Precio': medicamento.getPrecio(),
            'Descripcion': medicamento.getDescripcion(),
            'Cantidad': medicamento.getCant(),
            'Vendidos': medicamento.getVendidos()
        }
            return(jsonify(objeto))  

    salida = { "Mensaje": "No existe"}
    return(jsonify(salida))

#CITAS

@app.route('/Citas', methods=['POST'])
def AgregarCita():

    global Cita

    paciente = request.json['paciente']
    doctor = request.json['doctor']
    fecha = request.json['fecha']
    hora = request.json['hora']
    motivo = request.json['motivo']
    estado = request.json['estado']

    nueva = Cita(paciente,doctor,fecha,hora,motivo,estado)

    Citas.append(nueva)

    return jsonify({'Mensaje':'Se solicito la cita exitosamente',})

@app.route('/Citas', methods=['GET'])
def getCitas():
    global Citas

    Datos = []

    for cita in Citas:

        objeto = {
            'Paciente': cita.getPaciente(),
            'Doctor': cita.getDoctor(),
            'Fecha': cita.getFecha(),
            'Hora': cita.getHora(),
            'Motivo': cita.getMotivo(),
            'Estado': cita.getEstado()
        }

        Datos.append(objeto)
 
    return(jsonify(Datos))

@app.route('/Citas/<string:nombre>', methods=['GET'])
def ObtenerCita(nombre): 

    global Citas

    for cita in Citas:

        if cita.getPaciente() == nombre:
            objeto = {
            'Paciente': cita.getPaciente(),
            'Doctor': cita.getDoctor(),
            'Fecha': cita.getFecha(),
            'Hora': cita.getHora(),
            'Motivo': cita.getMotivo(),
            'Estado': cita.getEstado()
            }
            return(jsonify(objeto))
              

    salida = { "Mensaje": "No Tiene Cita"}
    return(jsonify(salida))

@app.route('/Citas/<string:nombre>', methods=['PUT'])
def ActualizarCita(nombre):
    global Citas

    for i in range(len(Citas)):

        if nombre == Citas[i].getPaciente():

            Citas[i].setDoctor(request.json['doctor'])
            Citas[i].setFecha(request.json['fecha'])
            Citas[i].setHora(request.json['hora'])
            Citas[i].setMotivo(request.json['motivo'])
            Citas[i].setEstado(request.json['estado'])
            return jsonify({'Mensaje':'Se actualizo la cita exitosamente'})

    return jsonify({'Mensaje':'No se encontro la cita para actualizar'})


#EXISTENCIA DE USUARIO
@app.route('/<string:nombre>', methods=['GET'])
def ObtenerPersona(nombre): 

    global Pacientes
    global Doctores
    global Enfermeras

    for paciente in Pacientes:

        if paciente.getUsuario() == nombre:
            
            salida = { "Existe": True,
                        "Tipo" : "Paciente"}

            return(jsonify(salida))
    
    for doctor in Doctores:

        if doctor.getUsuario() == nombre:
            
            salida = { "Existe": True,
                        "Tipo" : "Doctor"}

            return(jsonify(salida))
      
    for enfermera in Enfermeras:

        if enfermera.getUsuario() == nombre:
            
            salida = { "Existe": True,
                        "Tipo" : "Enfermera"}

            return(jsonify(salida))

    salida = { "Existe": False}
    return(jsonify(salida))



if __name__ == "__main__":
    app.run(debug=True)