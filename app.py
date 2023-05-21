from flask import Flask, request, render_template
from exercises import Exercises

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main/index.html')


@app.route('/ex_1', methods=['POST', 'GET'])
def ex_1_answer():
    return render_template('main/exercise_1_answer.html', sort=Exercises.ex_1(request.form['sort_ex_1']))


if __name__ == '__main__':
    app.run(debug=True)
