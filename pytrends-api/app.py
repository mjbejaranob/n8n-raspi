from flask import Flask, request, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)
pytrends = TrendReq(hl='en-US', tz=360)

@app.route('/trends', methods=['GET'])
def get_trends():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({'error': 'Keyword required'}), 400
    pytrends.build_payload([keyword])
    data = pytrends.interest_over_time()
    if data.empty:
        return jsonify({'error': 'No data found'}), 404
    return jsonify(data.reset_index().to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
