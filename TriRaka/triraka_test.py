from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def test():
    return render_template('index.html')


@app.route("/rakesh")
def name():
    return "<Rakesh Kumar Gupta"


if __name__ == '__main__':
    app.run(debug=True)
