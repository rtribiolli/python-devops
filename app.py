#!/home/daniel/python-devops/venv/bin/python3
from flask import Flask, render_template
from pdocker.bdocker import docker
from pjenkins.bjenkins import jenkins

app = Flask(__name__)
app.register_blueprint(docker)
app.register_blueprint(jenkins)

@app.route("/")
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True, port=5050)