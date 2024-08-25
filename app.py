from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def get_exchange_rates():
    response = requests.get(API_URL)
    data = response.json()
    return data['rates']

@app.route('/')
def index():
    rates = get_exchange_rates()
    return render_template('index.html', rates=rates)

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    rates = get_exchange_rates()
    
    if from_currency != 'USD':
        amount /= rates[from_currency]
    converted_amount = amount * rates[to_currency]
    
    return render_template('index.html', rates=rates, converted_amount=converted_amount, from_currency=from_currency, to_currency=to_currency)

@app.route('/rates')
def rates():
    rates = get_exchange_rates()
    return render_template('rates.html', rates=rates)

if __name__ == '__main__':
    app.run(debug=True)
