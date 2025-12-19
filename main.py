from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from services.yahoo import get_stock

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/stock")
def api_stock():
    symbol = request.args.get("symbol")
    period = request.args.get("period", "1mo")
    interval = request.args.get("interval", "15m")

    data = get_stock(symbol, period, interval)

    if not data:
        return jsonify({"error": "Data tidak ditemukan"})

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
