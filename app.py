from flask import Flask, render_template, request, redirect, url_for,flash
from dao.NacionalidadesDao import NacionalidadesDao

app = Flask(__name__)

# flash requiere esta sentencia
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/nacionalidad-index')
def nacionalidad_index():
    # Creacion de la instancia de Nacionalidaddao
    nacionalidadDao = NacionalidadesDao()
    lista_nacionalidades = nacionalidadDao.getNacionalidad()
    return render_template('nacionalidad-index.html', lista_nacionalidades=lista_nacionalidades)

@app.route('/nacionalidad')
def nacionalidad():
    return render_template('nacionalidad.html')

@app.route('/guardar-nacionalidad', methods=['POST'])
def guardarNacionalidad():
    nacionalidad = request.form.get('txtNacionalidad').strip()
    if nacionalidad == None or len(nacionalidad) < 1:
        # mostrar un mensaje al usuario
        flash('Debe escribir algo en la descripcion', 'warning')

        # redireccionar a la vista nacionalidad
        return redirect(url_for('nacionalidad'))

    nacionalidaddao = NacionalidadesDao()
    nacionalidaddao.guardarNacionalidad(nacionalidad.upper())

    # mostrar un mensaje al usuario
    flash('Guardado exitoso', 'success') 

    # redireccionar a la vista nacionalidad
    return redirect(url_for('nacionalidad_index'))

@app.route('/nacionalidad-editar/<id>')
def nacionalidadEditar(id):
    nacionalidaddao = NacionalidadesDao() #.getNacionalidad
    nacionalidad = nacionalidaddao.getNacionalidadById(id)
    return render_template('nacionalidad-editar.html', nacionalidad=nacionalidad)

@app.route('/actualizar-Nacionalidad', methods=['POST'])
def actualizarNacionalidad():
    id = request.form.get('txtId')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
        flash('No debe estar vacia la descripcion')
        return redirect(url_for('nacionalidadEditar', id=id))

    # actualizar
    Nacionalidaddao = NacionalidadesDao()
    Nacionalidaddao.updateNacionalidad(id, descripcion.upper())

    return redirect(url_for('nacionalidad_index'))

@app.route('/Nacionalidad-eliminar/<id>')
def nacionalidadEliminar(id):
    Nacionalidad = NacionalidadesDao()
    Nacionalidad.deleteNacionalidad(id)
    return redirect(url_for('nacionalidad_index'))

# se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)