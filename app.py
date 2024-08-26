from flask import Flask, render_template, request
import requests
#import os
from datetime import datetime

app = Flask(__name__)
API_KEY = 'deffc8e0f02d5e8a05e0d2e6'
BASE_URL = 'https://v6.exchangerate-api.com/v6/'

def fetch_exchange_rate(from_currency, to_currency):
    """Obtiene la tasa de cambio de la API."""
    url = f'{BASE_URL}{API_KEY}/latest/{from_currency}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'conversion_rates' in data:
            return data['conversion_rates'].get(to_currency), data.get('time_last_updated_utc')
    except requests.RequestException as e:
        print(f'Error al hacer la solicitud a la API: {e}')
    return None, None

def format_conversion_result(amount, rate):
    """Calcula y formatea el resultado de la conversión."""
    return f"{amount * rate:.2f}"

@app.route('/', methods=['GET', 'POST'])
def index():
    conversion_result = None
    last_updated = None
    amount = None
    from_currency = None
    to_currency = None

    if request.method == 'POST':
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        try:
            amount = float(request.form.get('amount', 0))
        except ValueError:
            return render_template('index.html', error_message='Cantidad inválida', conversion_result=None)

        rate, api_last_updated = fetch_exchange_rate(from_currency, to_currency)
        if rate:
            conversion_result = format_conversion_result(amount, rate)
            if api_last_updated:
                last_updated = datetime.strptime(api_last_updated, '%Y-%m-%dT%H:%M:%S+00:00').strftime('%d-%m-%Y %H:%M:%S')
            else:
                last_updated = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        else:
            conversion_result = 'Error al obtener la tasa de cambio'

    return render_template(
        'index.html',
        conversion_result=conversion_result,
        last_updated=last_updated,
        amount=amount,
        from_currency=from_currency,
        to_currency=to_currency
    )
# @app.route('/divisas')
# def divisas():
#     response = requests.get(url)
#     data = response.json()

#     if response.status_code == 200 and 'conversion_rates' in data:
#         rates = data['conversion_rates']
#         return render_template('divisas.html', rates=rates)
#     else:
#         error_message = 'Error al obtener la lista de divisas'
#         return render_template('divisas.html', error_message=error_message)

@app.route('/divisas')
def divisas():
    url = f'{BASE_URL}{API_KEY}/latest/USD'  # Esta variable no se estaba usando aqui
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and 'conversion_rates' in data:
        rates = data['conversion_rates']
        return render_template('divisas.html', rates=rates)
    else:
        error_message = 'Error al obtener la lista de divisas'
        return render_template('divisas.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)

