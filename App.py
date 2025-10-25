from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(open("index.html").read())

@app.route('/generate', methods=['POST'])
def generate():
    story = request.form['story']
    return f"<h3>Story received:</h3><p>{story}</p><p>(AI video generation will happen here)</p>"

if __name__ == '__main__':
    app.run(debug=True)