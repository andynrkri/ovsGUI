import subprocess
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def first():
    return render_template("tree.html")


@app.route('/enter', methods=['POST'])
def enter():
    command = request.form.get('command_box')
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    out = p.communicate()[0]
    context = {'out': out}
    return render_template('home.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
