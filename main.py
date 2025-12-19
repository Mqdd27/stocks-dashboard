from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from services.yahoo import get_stock

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/stock")
def stock():
    symbol = request.args.get("symbol", "").upper()
    period = request.args.get("period", "1mo")

    if not symbol:
        return jsonify({"error": "symbol required"}), 400

    data = get_stock(symbol, period)
    if not data:
        return jsonify({"error": "data not found"}), 404

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
