from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    analysis = TextBlob(text)
    
    sentiment = "positive" if analysis.sentiment.polarity > 0 else "negative"
    if analysis.sentiment.polarity == 0:
        sentiment = "neutral"
    
    return jsonify({
        "text": text,
        "sentiment": sentiment,
        "score": analysis.sentiment.polarity
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

