from flask import Flask, jsonify, request, render_template
#Acessar o banco de dados
import MySQLdb
import loading

app = Flask(__name__)

########################################### Login ##################################################################

@app.route('/entrar/<username>/<senha>', methods=['GET', 'POST'])
def verificavalor(username, senha):
    db = MySQLdb.connect(host="muriloceolin.mysql.pythonanywhere-services.com",  # your host
                     user="----",  # username
                     passwd="----",  # password
                     db="----")  # name of the database

    cursor = db.cursor()
    user = '"'+username+'"'
    psw = '"'+senha+'"'
    cursor.execute("SELECT username and senha FROM LoginUsuarios WHERE username = {} and senha = {};".format(user, psw))
    db.commit()
    saida = []
    for linha in cursor.fetchall():
        saida.append(linha)
    cursor.close()
    db.close()
    if saida == []:
        r = dict({'resp':'*Usuario ou Senha incorretos'})
        return jsonify(r)
    else:
        r = dict({'resp':'Entrou'})
        return jsonify(r)



############################# Cadastro ################################################


@app.route('/cadastrar/<username>/<senha>/<senha2>', methods=['GET', 'POST'])
def verificaNome(username, senha, senha2):
    db = MySQLdb.connect(host="muriloceolin.mysql.pythonanywhere-services.com",  # your host
                         user="----",  # username
                         passwd="----",  # password
                         db="----")  # name of the database

    cursor = db.cursor()
    user = '"'+username+'"'
    psw = '"'+senha+'"'
    if senha == senha2:
        cursor.execute("INSERT INTO LoginUsuarios(username, senha) VALUES ({},{});".format(user, psw))#(username = {},senha = {});".format(username, senha))
        db.commit()
        saida = []
        for linha in cursor.fetchall():
            saida.append(linha)
        cursor.close()
        db.close()
        r = dict({'resp':'Cadastro Realizado com Sucesso'})
        return jsonify(r)
    else:
        r = dict({'resp':'*Senhas Diferentes'})
        return jsonify(r)



#Sera realizado esta rota quando o botao de iniciar navegacao for acionado (Já vai ter no banco o username dele#


@app.route('/localizacao/motorista/<usernameApp>/<latitude>/<longitude>/<latiSaida>/<longiSaida>/<latiDestino>/<longiDestino>/<nomeIda>/<nomeVolta>/<nomeAtual>', methods=['GET', 'POST'])
def motorista(usernameApp,latitude, longitude,latiSaida,longiSaida,latiDestino,longiDestino, nomeIda, nomeVolta, nomeAtual):
    db = MySQLdb.connect(host="muriloceolin.mysql.pythonanywhere-services.com",  # your host
                         user="----",  # username
                         passwd="----",  # password
                         db="----")  # name of the database

    usernameApp = '"'+usernameApp+'"'
    latitudeStr= '"'+latitude+'"'
    longitudeStr = '"'+longitude+'"'

    latiSaidaStr = '"'+latiSaida+'"'
    longiSaidaStr = '"'+longiSaida+'"'

    latiDestinoStr = '"'+latiDestino+'"'
    longiDestinoStr = '"'+longiDestino+'"'

    nomeIda = '"'+nomeIda+'"'
    nomeVolta = '"'+nomeVolta+'"'
    nomeAtual = '"'+nomeAtual+'"'


    cursor = db.cursor()
    cursor.execute("UPDATE Geolocalizacao06 SET latitude = {}, longitude = {}, latiSaida = {}, longiSaida = {}, latiDestino = {}, longiDestino = {}, nomeIda = {}, nomeVolta = {}, nomeAtual = {} WHERE username = {};".format(latitudeStr,longitudeStr,latiSaidaStr,longiSaidaStr,latiDestinoStr,longiDestinoStr,nomeIda, nomeVolta, nomeAtual, usernameApp))
    db.commit()



#----------------------->

    #Seleciona Latitude
    cursor.execute("SELECT latitude FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
    db.commit()
    result = cursor.fetchall()
    for resultLati in result:
        latiAtual = resultLati[0]
    cursor.execute("SELECT latiDestino FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
    db.commit()
    result = cursor.fetchall()
    for linha in result:
        latiUsu = linha[0]
        difLatMoto = ((latiAtual * (-1)) - (latiUsu*(-1)))*(10000)


#----------------------->

    #Seleciona Longitude
    cursor.execute("SELECT longitude FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
    db.commit()
    result = cursor.fetchall()
    for res in result:
        longi = res[0]
    cursor.execute("SELECT longiDestino FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
    db.commit()
    resultadoLong = cursor.fetchall()
    for linhaLong in resultadoLong:
        Lng = linhaLong[0]
        difLongMoto = ((longi * (-1)) - (Lng*(-1)))*(10000)


# ----------------------->

    xm = (difLatMoto/60)*1852
    ym = (difLongMoto/60)*1852
    dist = ((xm ** 2) + (ym ** 2))**(1/2) #distancia em metros


# ----------------------->

    if dist <= 100:
        # # return jsonify({"resp":dist})

        cursor = db.cursor()
        cursor.execute("UPDATE Geolocalizacao06 SET nomeAtual = nomeVolta WHERE username = {};".format(usernameApp))
        db.commit()

        return jsonify({"result": 'nomeAtual = nomeVolta'})


    else:

        #Seleciona Latitude
        cursor.execute("SELECT latitude FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
        db.commit()
        result = cursor.fetchall()
        for resultLati in result:
            latiAtual = resultLati[0]
        cursor.execute("SELECT latiSaida FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
        db.commit()
        result = cursor.fetchall()
        for linha in result:
            latiUsu = linha[0]
            difLatMoto = ((latiAtual * (-1)) - (latiUsu*(-1)))*(10000)

    #----------------------->

        #Seleciona Longitude
        cursor.execute("SELECT longitude FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
        db.commit()
        result = cursor.fetchall()
        for res in result:
            longi = res[0]

        cursor.execute("SELECT longiSaida FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
        db.commit()
        resultadoLong = cursor.fetchall()
        for linhaLong in resultadoLong:
            Lng = linhaLong[0]
            difLongMoto = ((longi * (-1)) - (Lng*(-1)))*(10000)



    # ----------------------->
        xm = (difLatMoto/60)*1852
        ym = (difLongMoto/60)*1852
        dist = ((xm ** 2) + (ym ** 2))**(1/2) #distancia em metros

        if(dist <= 100):

            cursor = db.cursor()
            cursor.execute("UPDATE Geolocalizacao06 SET nomeAtual = nomeIda WHERE username = {};".format(usernameApp))
            db.commit()
            return jsonify({"result": 'nomeAtual = nomeIda'})

        else:
            return jsonify({"result": "onibus no trajeto"})



# @app.route('/localizacao/motorista/<usernameApp>/<latitude>/<longitude>', methods=['GET', 'POST'])
# def geolocalizacao(usernameApp,latitude, longitude):
#     db = MySQLdb.connect(host="muriloceolin.mysql.pythonanywhere-services.com",  # your host
#                      user="muriloceolin",  # username
#                      passwd="teste159",  # password
#                      db="muriloceolin$tcc")  # name of the database

#     usernameApp = '"'+usernameApp+'"'
#     latitudeStr= '"'+latitude+'"'
#     longitude = '"'+longitude+'"'



#     cursor = db.cursor()
#     cursor.execute("UPDATE Geolocalizacao02 SET latitude = {}, longitude = {} WHERE username = {};".format(latitudeStr,longitude,usernameApp))
#     db.commit()

#     #Seleciona Latitude
#     cursor.execute("SELECT latitude FROM Geolocalizacao02 WHERE username = {};".format(usernameApp))
#     db.commit()
#     result = cursor.fetchall()
#     for re in result:
#         lati = re[0]

#     cursor.execute("SELECT latitude FROM Geolocalizacao02 WHERE descricao = 'usuario';")
#     db.commit()
#     resultado = cursor.fetchall()
#     for linha in resultado:
#         latiUsu = linha[0]
#         difLat = ((lati * (-1)) - (latiUsu*(-1)))*(10000)



#     #Seleciona Longitude
#     cursor.execute("SELECT longitude FROM Geolocalizacao02 WHERE username = {};".format(usernameApp))
#     db.commit()
#     result = cursor.fetchall()
#     for res in result:
#         lati = res[0]

#     cursor.execute("SELECT longitude FROM Geolocalizacao02 WHERE descricao = 'usuario';")
#     db.commit()
#     resultadoLong = cursor.fetchall()
#     for linhaLong in resultadoLong:
#         Lng = linhaLong[0]
#         difLong = ((lati * (-1)) - (Lng*(-1)))*(10000)

#     xmetros = (difLat/60)*1852
#     ymetros = (difLong/60)*1852

#     dist = ((xmetros ** 2) + (ymetros ** 2))**(1/2) #distancia em metros

#     # return jsonify(dist)

#     if dist <= 2000:
#         # resposta = 'Usuario aguardando no ponto'
#         # r = dict({usernameApp:'Usuario aguardando no ponto'})
#         r = dict({'result':'Usuario aguardando no ponto'})
#         return jsonify(r)
#         # return jsonify(r[usernameApp])

#     else:
#         # r = dict({usernameApp:'Monitoriando...'})
#         r = dict({'result':'Monitoriando...'})
#         return jsonify(r)


########################################### SITE ########################################################


@app.route('/adicionarlocal/<descricao>/<username>/<endereco>', methods=['GET', 'POST'])
def sitemain(descricao,username,endereco):
    db = MySQLdb.connect(host="muriloceolin.mysql.pythonanywhere-services.com",  # your host
                         user="----",  # username
                         passwd="----",  # password
                         db="----")  # name of the database

    cursor = db.cursor()
    user = '"'+username+'"'
    descri = '"'+descricao+'"'

    cursor.execute(" INSERT INTO Geolocalizacao06(descricao,username, latitude,longitude,latiSaida,longiSaida,latiDestino,longiDestino,nomeIda,nomeVolta,nomeAtual) VALUES ({},{},25,25,0,0,0,0,'-','-','-');".format(descri,user))#.format(descri,user))
    db.commit()
    return 'Cadastro realizado com Sucesso !!'















############################# Usuário ################################################



@app.route('/localizacao/usuario/<usernameApp>/<latitude>/<longitude>/<onibus>', methods=['GET', 'POST'])
def geolocalizacaousuario(usernameApp,latitude, longitude, onibus):
    db = MySQLdb.connect(host="muriloceolin.mysql.pythonanywhere-services.com",  # your host
                         user="----",  # username
                         passwd="----",  # password
                         db="----")  # name of the database

    usernameApp = '"'+usernameApp+'"'
    latitudeStr= '"'+latitude+'"'
    longitudeStr = '"'+longitude+'"'
    onibus = '"'+onibus+'"'



    cursor = db.cursor()
    cursor.execute("UPDATE Geolocalizacao06 SET latitude = {}, longitude = {} WHERE username = {};".format(latitudeStr,longitudeStr,usernameApp))
    db.commit()

    #----------------------->

    #Seleciona Latitude
    cursor.execute("SELECT latitude FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
    db.commit()
    result = cursor.fetchall()
    for resultLati in result:
        latiAtual = resultLati[0]

    cursor.execute("SELECT latitude FROM Geolocalizacao06 WHERE descricao = 'estacao';")
    db.commit()
    result = cursor.fetchall()

    for linha in result:
        latiUsu = linha[0]
        difLatMoto = ((latiAtual * (-1)) - (latiUsu*(-1)))*(10000)

    #Seleciona Longitude
    cursor.execute("SELECT longitude FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
    db.commit()
    result = cursor.fetchall()
    for res in result:
        longi = res[0]

    cursor.execute("SELECT longitude FROM Geolocalizacao06 WHERE descricao = 'estacao';")
    db.commit()
    resultadoLong = cursor.fetchall()
    for linhaLong in resultadoLong:
        Lng = linhaLong[0]
        difLongMoto = ((longi * (-1)) - (Lng*(-1)))*(10000)


# ----------------------->

    xm = (difLatMoto/60)*1852
    ym = (difLongMoto/60)*1852
    dist = ((xm ** 2) + (ym ** 2))**(1/2) #distancia em metros


    if (dist <= 300):
        return jsonify({"resp": "Nome da Estacao - Usuario entrando... "})



    else:

        #----------------------->

        #Seleciona Latitude
        cursor.execute("SELECT latitude FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
        db.commit()
        result = cursor.fetchall()
        for resultLati in result:
            latiAtual = resultLati[0]

        cursor.execute("SELECT latitude FROM Geolocalizacao06 WHERE descricao = 'ponto';")
        db.commit()
        result = cursor.fetchall()
        for linha in result:
            latiUsu = linha[0]
            difLatPont = ((latiAtual * (-1)) - (latiUsu*(-1)))*(10000)


        #Seleciona Longitude
        cursor.execute("SELECT longitude FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
        db.commit()
        result = cursor.fetchall()
        for res in result:
            longi = res[0]

        cursor.execute("SELECT longitude FROM Geolocalizacao06 WHERE descricao = 'ponto';")
        db.commit()
        resultadoLong = cursor.fetchall()
        for linhaLong in resultadoLong:
            Lng = linhaLong[0]
            difLongPont = ((longi * (-1)) - (Lng*(-1)))*(10000)


    # ----------------------->

        xmpnt = (difLatPont/60)*1852
        ympnt = (difLongPont/60)*1852
        dist = ((xmpnt ** 2) + (ympnt ** 2))**(1/2) #distancia em metros


        if (dist <= 50):
    # ----------------------->

            #Seleciona Latitude
            cursor.execute("SELECT latitude FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
            db.commit()
            resultUserMotoLat = cursor.fetchall()
            for resultLati in resultUserMotoLat:
                latiUserMotoLat = resultLati[0]
            cursor.execute("SELECT latitude FROM Geolocalizacao06 WHERE nomeAtual = {};".format(onibus))
            db.commit()
            resultMoto = cursor.fetchall()
            for linhaMoto in resultMoto:
                latiMotorista = linhaMoto[0]


                difLatMoto = ((latiUserMotoLat * (-1)) - (latiMotorista*(-1)))*(10000)


            #Seleciona Longitude
            cursor.execute("SELECT longitude FROM Geolocalizacao06 WHERE username = {};".format(usernameApp))
            db.commit()
            resultUserMotoLng = cursor.fetchall()
            for res in resultUserMotoLng:
                longiMoto = res[0]
            cursor.execute("SELECT longitude FROM Geolocalizacao06 WHERE nomeAtual = {};".format(onibus))
            db.commit()
            resultadoMoto = cursor.fetchall()
            for linhaMoto in resultadoMoto:
                LngMoto = linhaLong[0]
                difLongMoto = ((longiMoto * (-1)) - (LngMoto*(-1)))*(10000)


        # ----------------------->

            xmmoto = (difLatMoto/60)*1852
            ymmoto = (difLongMoto/60)*1852
            dist = ((xmmoto ** 2) + (ymmoto ** 2))**(1/2) #distancia em metros



            if (dist <= 15):
                # Contagem += 1
                # if (Contagem > 9):
                #     cursor.execute("UPDATE Geolocalizacao06 SET latitude = 0, longitude = 0 WHERE username = 0;".format(usernameApp))
                #     db.commit()
                # cursor.execute("UPDATE Geolocalizacao06 SET latitude = 0, longitude = 0 WHERE username = {};".format(usernameApp))
                # db.commit()
                return jsonify({"resp": 'Você está no onibus em direcao ao seu destino'})

            elif (dist <= 2000):
                return jsonify({"resp": "Seu onibus está chegando até você", "result": "Usuario esperando no ponto"})
            else:
                return jsonify({"resp":'nenhum onibus perto...'})


        else:
            return jsonify({"resp":"Você está longe do ponto"})





############################# Estação de metro e Trem ################################################

@app.route('/localizacao/estacao/<usernameApp>/<latitude>/<longitude>', methods=['GET', 'POST'])
def geolocalizacaoestacao(usernameApp,latitude, longitude):
    db = MySQLdb.connect(host="muriloceolin.mysql.pythonanywhere-services.com",  # your host
                         user="----",  # username
                         passwd="----",  # password
                         db="----")  # name of the database
    cursor = db.cursor()

    usernameApp = '"'+usernameApp+'"'
    latitudeStr= '"'+latitude+'"'
    longitudeStr = '"'+longitude+'"'

    cursor.execute("INSERT INTO Geolocalizacao06(descricao,username,latitude,longitude,latiSaida,longiSaida,latiDestino,longiDestino,nomeIda,nomeVolta,nomeAtual) VALUES('estacao',{},{},{},0,0,0,0,'-','-','-');".format(usernameApp,latitudeStr,longitudeStr))
    db.commit()