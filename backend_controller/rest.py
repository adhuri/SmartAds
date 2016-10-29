import os
from flask import Flask, render_template, request, url_for,jsonify

app = Flask(__name__)
#Main function that handles the post request
@app.route('/<user>')
def func_main(user):
	print request.body
	print request.form


if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
