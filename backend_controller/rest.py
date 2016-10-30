import os
from flask import Flask, render_template, request, url_for,jsonify

app = Flask(__name__)
#Main function that handles the post request
@app.route('/<user>',methods=['POST'])
def func_main(user):
	print str(request)
	file = request.files['uploadedfile']
     	print file
	if file:
       		file.save("/home/ubuntu/HackNC_ContextAds/backend_controller/temp.png")
        

	return "<p>cool</p>"

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
