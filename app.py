from flask import Flask, request, render_template
from exercises import Exercises
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main/index.html')


@app.route('/ex_1', methods=['POST', 'GET'])
def ex_1_answer():
    return render_template('main/exercise_1_answer.html', sort=Exercises.ex_1(request.form['sort_ex_1']))


@app.route('/ex_2', methods=['POST', 'GET'])
def ex_2_answer():
    sort = Exercises.ex_2(request.form['sort_ex_2'])
    print(sort)
    return render_template('main/exercise_2_answer.html', sort=Exercises.ex_2(request.form['sort_ex_2']))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return render_template('errors/bad_request.html'), 400


if __name__ == '__main__':
    app.run(debug=True)
