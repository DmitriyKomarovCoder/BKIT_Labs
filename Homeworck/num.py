from flask import Flask
from fib import fib

app = Flask(__name__)

@app.route('/')
def hello_word():
    return "<p>Returning the Fibonacci numbers!</p>"

@app.route('/num/<int:cnt>')
def get_fib(cnt):
    fib_gen = fib()
    res = [next(fib_gen) for _ in range(cnt)]
    return res