import subprocess
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def first():
    return render_template("tree.html")


@app.route('/<firstparam>/<secondparam>', methods=['POST'])
def enter(firstparam, secondparam):
    command = request.form.get('input_one')
    flow = request.form.get('input_two')
    command =firstparam+" "+secondparam+" "+ command + " " + flow
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    out = p.communicate()[0]
    if out == None:
        out = p.communicate()[1]
    context = {'out': out}
    return command

@app.route('/getbridges')
def getbridges():
    return "here are the bridges"


if __name__ == '__main__':
    app.run(debug=True)
