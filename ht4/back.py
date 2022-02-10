from flask import Flask,request
from werkzeug.wrappers import response

app = Flask(__name__)

data = []

@app.route('/',methods=['GET'])
def metodo_get():# print list
    print('Metodo GET')
    res ={}
    res['data'] = data
    print(data)
    return res
        
@app.route('/',methods=['POST'])
def metodo_post():
    res ={}
    usuario = request.form.get('file')
    print(f'Metodo Post\n Elemento mandado para guardar: "{usuario}"')
    res['data'] = usuario
    if usuario == None:
        res['existe'] = 0
        return res
    if usuario in data:
        res['repetido'] = 1
        print(f' El elemento: "{usuario}" ya se encuentra guardado')
        return res    
    data.append(usuario)
    res['repetido'] = 0
    return res

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