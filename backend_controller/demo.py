import os
from flask import Response,Flask, render_template, request, url_for,jsonify
import json
import datetime
app = Flask(__name__)

def get_offers(user,lat,longi,time1):
    home=[35.775295, -78.685293]
    work=[35.874435, -78.842677]
    gym=[35.783728, -78.672094 ]
    foodlion=[35.786623, -78.692838 ]
    convenient=[35.779573, -78.675055]
    time_hr=int(datetime.datetime.fromtimestamp(int(time1)).strftime('%H'))
    print time_hr

    mydict={}
    print "Given home:",((int(float(home[0])*1000)),int(float(lat)*1000))
    if(((int(float(work[0])*1000))==int(float(lat)*1000)) and (int(float(work[1])*1000)==int(float(longi)*1000))):
            if(time_hr>=7 and time_hr<=11):
                mydict['name']=user
            	mydict['OfferName']="Tuna Offer!"
           	mydict['OfferDetails']="50% off at Foodlion"
            	mydict['lat']= str(foodlion[0])
            	mydict['longi'] = str(foodlion[1])
    elif(((int(float(gym[0])*1000))==int(float(lat)*1000)) and (int(float(gym[1])*1000)==int(float(longi)*1000))):
            if(time_hr>=15 and time_hr<=19):
                mydict['name']=user
            	mydict['OfferName']="Gatorade Offer!"
                mydict['OfferDetails']="Buy one get one Gatorade Free at 6 Twelve Convenient Store"
            	mydict['lat']= str(convenient[0])
            	mydict['longi'] = str(convenient[1])
    return mydict


#Main function that handles the post request
@app.route('/<user>/<lat>/<longi>/<time1>',methods=['POST'])
def func_main(user,lat,longi,time1):
	data=get_offers(user,lat,longi,time1)

	js = json.dumps(data)
    	resp = Response(js, status=200, mimetype='application/json')
    	#resp.headers['Link'] = 'http://luisrei.com'
	print js
	return resp

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
