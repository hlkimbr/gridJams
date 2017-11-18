from flask import Flask, render_template, json, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/jam/', methods=['POST','GET'])
def jam():
    sound = request.form.get('sound')
    return render_template('jam.html',**locals())

if __name__ == "__main__":
    app.run(debug = True)
