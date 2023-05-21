from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main/index.html')


if __name__ == '__main__':
    app.run(debug=True)