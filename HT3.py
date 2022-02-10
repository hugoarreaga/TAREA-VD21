from flask import Flask,request

app = Flask(__name__)

data = []

@app.route('/',methods=['GET'])
def metodo_get():# print list
    print('Metodo GET')
    print(data)
    return f'metodo get'
        
@app.route('/',methods=['POST'])
def metodo_post():
    usuario = request.form.get('file')
    print(f'Metodo Post\n Elemento mandado para guardar: "{usuario}"')
    if usuario == None:
        return f'no se envio ningun parametro'
    if usuario in data:
        print(f' El elemento: "{usuario}" ya se encuentra guardado')
        return f' El elemento: "{usuario}" ya se encuentra guardado'
    data.append(usuario)
    return f'Se agrego el elemento: "{usuario}"'


@app.route('/',methods=['PUT'])
def metodo_put():
    usuario = request.args.get('file')

    print(f'Metodo Put\n Elemento mandado para editar: "{usuario}"')
    if usuario == None:
        return f'no se envio ningun parametro'
    for a in range(len(data)):
        if data[a] == usuario:
            data[a] = data[a] +'-editado'
            print(data)
            return f'Se edito el elemento: "{usuario}"'   
    print(data)         
    return f'No existe el elemento: "{usuario}"'

@app.route('/',methods=['DELETE'])
def metodo_delete():
    usuario = request.args.get('file')
    print('Metodo Delete')
    if usuario == None: return f'no se envio ningun parametro'
    for a in range(len(data)):
        if data[a] == usuario:
            del data[a]
            print (data)
            return f'Se a eliminado el elemento "{usuario}"'
    
    print (data)
    return f'El elemento "{usuario}" no existe'



if __name__ == '__main__':
    app.run(debug=True)