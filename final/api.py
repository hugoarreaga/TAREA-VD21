from flask import Flask,request,jsonify

app = Flask(__name__)

pedidos = []
@app.route('/get',methods=['GET'])
def apiget():
    res ={}

    res['nopedido' ]= 'nopeadfafdssdido'
    res['fechapedido' ]= 'fdchadfsapedido'
    res['cliente' ]= 'cliendsfaadfste'
    res['descripcion' ]= 'desadfscripcion'
    #pedidos.append(res)
    #pedidos.append(res)
    #pedidos.append(res)
    #pedidos.append(res)
    #pedidos.append(res)

    print(pedidos)

    return jsonify(pedidos)





@app.route('/post',methods=['POST'])
def apipost():
    
    new_user = {
        "nopedido": request.json['nopedido'],
        "fechapedido": request.json['fechapedido'],
        "cliente": request.json['cliente'],
        "descripcion": request.json['descripcion']
    }
    pedidos.append(new_user)            
    print("Metodo POST: ",new_user)
    return jsonify({'ok':True, "Usuario": "Usuario agreado satisfactoriamente"})



@app.route('/put',methods=['PUT'])
def apiput():
    return




@app.route('/delete',methods=['DELETE'])
def apidelete():
    nopedido = request.form.get('nopedido_d')
    for a in range(len( pedidos)):
        if pedidos[a]['nopedido'] == nopedido:
            del pedidos[a]
            return f'eliminado pedido {nopedido}'
    
    

    return f'no se encontro el pedido {nopedido}'


if __name__ == '__main__':
    app.run(debug=1)