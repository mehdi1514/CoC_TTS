from flask import Flask, render_template, request
from flask_gtts import gtts
app = Flask(__name__)
gtts(app)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', mytext='Hello from CoC')

if __name__ == "__main__":
    app.run(debug=True)