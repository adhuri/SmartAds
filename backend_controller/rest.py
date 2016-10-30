import os
from flask import Flask, render_template, request, url_for,jsonify

app = Flask(__name__)
#Main function that handles the post request
@app.route('/<user>',methods=['POST'])
def func_main(user):
	print str(request)
	#print request.description
	print request.files
	file = request.files['uploadedfile']
	file.read() 
     	if file:
        	filename = file.filename
       		file.save(os.path.join("/home/ubuntu/HackNC_ContextAds/backend_controller",filename))
        

#	print request.form
	return "<p>cool</p>"

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
