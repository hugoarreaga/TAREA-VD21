from flask import Flask,request
app = Flask(__name__)
@app.route('/',methods=['POST'])
def usuario():
    usuario = request.form.get('usuario')
    contrasena = request.form.get('contrasena')
    if   usuario.lower() == 'hugo arreaga' and contrasena == '201701108':return f'Bienvenido usuario "{usuario}"'
    elif usuario == 'admin' and contrasena == 'admin':return 'Bienvenido Administrador'
    else:return 'Error: usuario no existe'
if __name__ == '__main__':   app.run()
