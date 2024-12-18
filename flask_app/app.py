from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the transformer model
nlp_model = pipeline('ner', model="dbmdz/bert-large-cased-finetuned-conll03-english")

@app.route('/analyze', methods=['POST'])
def analyze_document():
    document_text = request.json.get('document')
    analysis_result = nlp_model(document_text)
    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)
