# webapp.py
import os
from flask import Flask, render_template, request
from fibonacci import fib
app = Flask(__name__)

from playsound import playsound

def playsound():
      return playsound('/filepath.mp3')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/fib')
def calculate_fib():
    which_number = int(request.args.get('fib_number'))
    return "Fibonacci number #{} is {}".format(
        which_number,
        fib(which_number)
    )

@app.route('/dogs')
def dogs():
    return render_template('doggos.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
