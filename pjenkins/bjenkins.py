from flask import Blueprint, render_template, redirect, request
from jenkins import Jenkins
from time import sleep

jenkins = Blueprint('jenkins', __name__, url_prefix='/jenkins')


con = Jenkins('http://127.0.0.1:8080',
                username='rtribiolli',
                password='4linux')

@jenkins.route('')
def index():
    
    #print(dir(con.get_all_jobs()[0]))
    return render_template('jenkins.html', jobs=con.get_all_jobs())

@jenkins.route('/build/<string:name>')
def build_job(name):
    con.build_job(name)
    sleep(10)
    return redirect('/jenkins')

@jenkins.route('/update/<string:name>', methods=[ "GET", "POST"])
def update_job(name):
    if request.method == "GET":    
        xml = con.get_job_config(name)
        return render_template('/jenkins_update.html', job_name=name, xml=xml)
    
    elif request.method == "POST":
        xml = request.form['xml']
        con.reconfig_job(name, xml)
        return redirect("/jenkins")