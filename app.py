from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lines')
def lines():
    return render_template('lines.html')

# Ruta para la versión original (usada, por ejemplo, en "Máquinas" de Línea 1)
@app.route('/machines')
def machines():
    return render_template('machines.html')

# Nueva ruta: para el encabezado "Máquinas"
@app.route('/machine_heading')
def machine_heading():
    return render_template('machine_heading.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/lines/l1/parameters')
def parameters():
    return render_template('parameters.html')

@app.route('/lines/l1/parameters/1')
def parameter_1():
    return render_template('parameter_1.html')

@app.route('/lines/l1/epss')
def epss():
    return render_template('epss.html')

@app.route('/lines/l1/epss/1')
def epss_1():
    return render_template('epss_1.html')

@app.route('/machines/max_muller')
def machine_detail():
    return render_template('machine_detail.html')


if __name__ == '__main__':
    app.run(debug=True)
