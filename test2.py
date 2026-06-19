from flask import Flask, request, jsonify, send_from_directory
from groq import Groq

app = Flask(__name__)
client = Groq(api_key="YOUR_API_KEY_HERE")

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.json['topic']
    
    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=8000,
        messages=[
            {"role": "user", "content": f"Make detailed Class 12 NEET notes on {topic}. Use proper HTML with headings, subheadings, tables, bullet points, colored backgrounds and good styling. Make it comprehensive and exam focused. Return ONLY the HTML code, nothing else."}
        ]
    )
    
    return jsonify({"html": chat.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True)