from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prijzen')
def prijzen():
    items = [
        {
            "product": "vanille-ijs 1 liter",
            "prijs": "2 euro"
        },
        {
            "product": "chocolade-ijs 1 liter",
            "prijs": "2 euro"
        }
    ]
    return render_template('prijzen.html', items=items)

@app.route('/recepten')
def recepten():
    items = [
        {
            "recept": "Tiramisu di nona",
            "img": "tiramisu.png"
        },
        {
            "recept": "IJstaart met chocolade",
            "img": "ijstaart.png"
        }
    ]
    return render_template('recepten.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)