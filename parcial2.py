from flask import Flask,request
from datetime import datetime

app = Flask( __name__)

@app.route('/',methods=['POST'])
def login():
    nombre = request.form.get('nombre')
    edad = request.form.get('date')
    
    for x in nombre:
        if x.isdigit():
            return 'Error en el nombre'
    
    fecha = ''
    try:
        fecha = datetime.strptime(edad, '%d/%m/%Y')
    except ValueError:
        return 'Error en el formato de fecha "DD/MM/YY"'

    if datetime.now() < fecha:
        return 'Fecha mayor a la actual'
    elif (int(fecha.year) +18) > int(datetime.now().year):
        return 'No es mayor de edad'

    return 'Bienvenido de nuevo'

if __name__=="__main__":
    app.run(debug=True)