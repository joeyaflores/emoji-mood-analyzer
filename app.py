from flask import Flask, render_template, request
from emoji_mood_analyzer import analyze_mood

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mood = None
    if request.method == 'POST':
        text = request.form.get('text')
        mood = analyze_mood(text)
    return render_template('index.html', mood=mood)

if __name__ == '__main__':
    app.run(debug=True)

