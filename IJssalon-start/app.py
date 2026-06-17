from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prijzen')
def prijzen():
    return render_template('prijzen.html')

@app.route('/recepten')
def recepten():
    return render_template('recepten.html')

if __name__ == '__main__':
    app.run(debug=True)