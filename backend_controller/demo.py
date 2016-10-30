import os
from flask import Response,Flask, render_template, request, url_for,jsonify
import json

app = Flask(__name__)

def get_offers(user,lat,longi,time,date):

    #[11:04 PM, 10/29/2016] +1 (984) 202-9501: Home: 35.775295, -78.685293                        
[11:05 PM, 10/29/2016] Utkarsh Ncsu: for work : 35.780309, -78.640117                        
[11:06 PM, 10/29/2016] +1 (984) 202-9501: for work: 35.874435, -78.842677                        
[11:07 PM, 10/29/2016] +1 (984) 202-9501: Foodlion: 35.786623, -78.692838                        
[11:08 PM, 10/29/2016] +1 (984) 202-9501: Gym: 35.783728, -78.672094                        
[11:09 PM, 10/29/2016] +1 (984) 202-9501: 6 twelve convenient store for Gatorade: 35.779573, -78.675055
    home=[]
    work=[]
    gym=[]
    foodlion=[]
    convenient=[]
    mydict={}
    if(int(lat)<=80 && int(longi)<=80):
    	mydict['name']=user
    	mydict['OfferName']="Tuna Offer"
   	mydict['OfferDetails']="50% off at Foodlion"
    	mydict['lat']= "80"
    	mydict['longi'] = "90"
	
    return mydict


#Main function that handles the post request
@app.route('/<user>/<lat>/<longi>/<time>/<date>',methods=['POST'])
def func_main(user,lat,longi,time,date):
	data=get_offers(user,lat,longi,time,date)
	js = json.dumps(data)
    	resp = Response(js, status=200, mimetype='application/json')
    	#resp.headers['Link'] = 'http://luisrei.com'
	return resp

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
