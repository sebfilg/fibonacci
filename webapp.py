# webapp.py
from flask import Flask, render_template, request
from fibonacci import fib
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/fib')
def calculate_fib():
    which_number = int(request.args.get('fib_number'))
    return "Fibonacci number #{} is {}".format(
        which_number,
        str(fib(which_number))
    )

if __name__ == '__main__':
    app.run()