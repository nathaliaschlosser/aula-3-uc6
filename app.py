from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/contatos')
def contatos():
    return "whatsapp: (11) 99999-9999"

if __name__ == '__main__':
    app.run(debug=True)
