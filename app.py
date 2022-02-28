from flask import Flask
from flask import abort, request
import json

app = Flask(__name__)
with open('validation.json') as f:
    validation = json.load(f)

parameters = {
     "symbol": 'ETHUSDT',
     "interval": '15m',
     "startTime": 1523577700000,
     "endTime": 1523664000000
}
# response = requests.get("https://www.binance.com/api/v3/klines",parameters)


@app.route("/")
def get_request():
    symbol = parameters["symbol"]#request.arg.get("symbol")
    # if a symbol isn't supplied in the request, return a 400 bad request
    if symbol is None:
        abort(400)
    elif symbol not in validation['symbols']:
        abort(404)

    interval = parameters["interval"]#request.arg.get("interval")
    # if interval isn't supplied in the request, return a 400 bad request
    if interval is None:
        abort(400)
    elif interval not in validation['intervals']:
        abort(404)

    start_time = parameters["startTime"]#request.arg.get("startTime")
    end_time = parameters["endTime"]#request.arg.get("endTime")
    if start_time is None:
        abort(400)
    elif end_time < start_time:
        abort(404)
