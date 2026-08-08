from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')


@app.route('/pagina2', methods=['GET', 'POST'])
def pagina2():

    if request.method == 'POST':

        nombre = request.form['nombre']
        correo = request.form['correo']

        mensaje = 'Registro realizado correctamente'

        return render_template(
            'pagina2.html',
            mensaje=mensaje,
            nombre=nombre,
            correo=correo
        )

    return render_template('pagina2.html')


@app.route('/pagina3')
def pagina3():
    return render_template('pagina3.html')


@app.route('/pagina4')
def pagina4():
    return render_template('pagina4.html', nombre='Estudiante')


@app.route('/estudiante/<nombre>')
def estudiante(nombre):
    return render_template('pagina4.html', nombre=nombre)


if __name__ == '__main__':
    app.run(debug=True)