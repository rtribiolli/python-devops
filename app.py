#!/home/daniel/python-devops/venv/bin/python3
from flask import Flask, render_template, request, session
from pdocker.bdocker import docker
from pjenkins.bjenkins import jenkins
from git_routes.git import git
from ldap3 import Connection, Server
from os import urandom
import logging 

server = Server('ldap://127.0.0.1:389')
app = Flask(__name__)
app.register_blueprint(docker)
app.register_blueprint(jenkins)
app.register_blueprint(git)

login.basicConfig(
    filename="app.log",
    level= logging.DEBUG,
    format="%(asctime)s [%(levelname)s ] %(name)s\n" +
    "[ %(funcName)s ] [%(filename)s, %(lineno)s] %(message)s",
    datafmt= "[%d/%m/%Y %H:%M:%S ]"
)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == "POST":    
        auth = request.form
        dn = f"uid={auth['email']},dc=dexter,dc=com,dc=br"
        con = Coonection(
            server, user=dn,password=auth['password'])
        if con.bind():
            session['auth'] = con.bind()
            if session['auth']:
                return redirect('/docker')
            logging.warning("Login ou senha invalida")
            return redirect('/')
        
        #     return render_template('index.html')
        # elif request.method == "POST":

        # dn = "uid=daniel.ouro@4linux.com.br, dc=dexter,dc=com,dc=br"
        # con = Connection(
        #     server, 
        #     user=dn,password='4linux'
        #     )
        # return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = urandon(12)
    app.run(debug=True, port=5050)