from flask import Flask,request

app = Flask(__name__)

@app.route('/login',methods=['GET'])
def inicio():
    print('aaaaa')
    usuario = ''
    contrasena =''
    try:
        usuario = request.args.get('usuario')
        contrasena = request.args.get('contrasena')
        if   usuario.lower() == 'hugo arreaga' and contrasena == '201701108':
            return usuario
        elif usuario == 'admin' and contrasena == 'admin':
            print('paso admins')
            return usuario 
        else:
            return 'None'
    except:
        return 'None'

    
    


if __name__ == '__main__':
    app.run(debug=True)
