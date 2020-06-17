from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title='Home')


app.run(debug=True, host='25.51.130.154')
