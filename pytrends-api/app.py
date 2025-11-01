from flask import Flask, jsonify
from pytrends.request import TrendReq
import json

app = Flask(__name__)

@app.route('/trending', methods=['GET'])
def trending_searches():
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        trending = pytrends.trending_searches(pn='australia')
        data = [{"keyword": kw} for kw in trending[0].tolist()]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
