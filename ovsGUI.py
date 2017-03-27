import subprocess
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def first():
    return render_template("tree.html")


@app.route('/<firstparam>/<secondparam>', methods=['POST'])
def enter(firstparam, secondparam):
    command = request.form.get('input_one')
    pattern = request.form.get('input_two')
    flow = request.form.get('input_three')
    command = firstparam + " " + secondparam + " " + command + " " + pattern + " " + flow
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    out = p.communicate()[0]
    if out == None:
        out = p.communicate()[1]
    context = {'out': out}
    return command


@app.route('/getbridges')
def getbridges():
    return "br0 br1 br3"


if __name__ == '__main__':
    app.run(debug=True)
