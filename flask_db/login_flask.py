from flask import Flask, render_template, request
import os
import mysql.connector
from flaskext.mysql import MySQL
#lib de comunicacao entre a aplicacao e o banco de dados

mysql = MySQL()
app = Flask(__name__)

#parametros de comunicacao com o banco
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123' #senha do banco
app.config['MYSQL_DATABASE_DB'] = 'teste' #nome do banco
app.config['MYSQL_DATABASE_HOS'] = 'ip' #colocar o ip do container depois de criado
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('login.html')

@app.route("/gravar", methods=['post', 'get'])
def gravar():
    nome = request.form['name']
    email = request.form['email']
    senha = request.form['password']
    if nome and email and senha:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into (nome da tabela) (user_name, user_username, user_password) VALUES(%s,%s,%s)', (nome, email, senha))
        conn.commit()                ##############                                                                 #requests
    return render_template('login.html')

@app.route("/listar", methods=['post', 'get'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select user_name, user_password from (nome da tabela)')
    data = cursor.fetchall()                                ############
    conn.commit()
    return render_template("dados_db.html", titulo='Name and Email', datas=data)

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host='127.0.0.1', port=port, debug=True) 










# docker
'''
1. Fazer cadastro e logar: https://hub.docker.com
2. Criar instancia no play-labs: https://labs.play-with-docker.com/
3. docker pull mysql:5.7
4. docker run --name mysql5 -e MYSQL_ROOT_PASSWORD=mudar123 -p 3307:3307 -d mysql:5.7
'''
