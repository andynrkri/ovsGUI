import subprocess, sqlite3
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
    command = [firstparam, secondparam, command, pattern, flow]
    out = get_output(command)
    context = {'out': out}
    return render_template("output.html", command=" ".join(command))  # need to pass in out after deploying on linux


def get_output(command):
    p = subprocess.Popen(" ".join(command), stdout=subprocess.PIPE, shell=True)
    out = p.communicate()[0]
    if out is None:
        out = p.communicate()[1]
    return out


# need to return out after deployment on linux
@app.route('/getbridges')
def getbridges():
    p = subprocess.Popen("ovs-vsctl list-br", stdout=subprocess.PIPE, shell=True)
    out = p.communicate()[0]
    if out is None:
        out = p.communicate()[1]
    return "ovs-vsctl list-br"


if __name__ == '__main__':
    app.run(debug=True)
