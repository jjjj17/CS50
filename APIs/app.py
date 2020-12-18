from flask import Flask, render_template, request, jsonify
from math import sqrt, log

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to my math API</h1><h2>To get the square, square root, natural logarithm(base e), base 10 logarithm and base 2 logarithm, just send a GET request to the url /api/&ltyournumber&gt where your number is the name you want to get the data from.</h2>"

@app.route("/api/<int:number_requested>")
def api_call(number_requested):
    return jsonify({
        "number_requested": number_requested,
        "squared_number": number_requested**2,
        "square_root": sqrt(number_requested),
        "natural_logarithm": log(number_requested),
        "base10logarithm": log(number_requested, 10),
        "base2logarithm": log(number_requested, 2)
    })