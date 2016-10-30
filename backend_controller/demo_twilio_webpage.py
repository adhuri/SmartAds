import os
from flask import Response,Flask, render_template, request, url_for,jsonify
import json
import datetime

from twilio.rest import TwilioRestClient
from jinja2 import Environment, FileSystemLoader
app = Flask(__name__)

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
home=[35.777817, -78.679211]
work=[35.874435, -78.842677]
gym=[35.7831831036184, -78.67090837432124]
foodlion=[35.786623, -78.692838 ]
convenient=[35.779573, -78.675055]

def send_sms(msg):
    account_sid="AC385c4d2e1c41dd5d2848c30cc781589c"
    auth_token="2e30b61a088f9eb07752d7419db5a554"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to="+19199317556",from_="+1919670-0903",body=msg)




def get_offers(user,lat,longi,end_lat,end_longi,time1):
    time_hr=int(datetime.datetime.fromtimestamp(int(time1)).strftime('%H'))
    print time_hr

    mydict={}
    print "Given home:",((int(float(home[0])*1000)),int(float(lat)*1000))
    if(((int(float(home[0])*1000))==int(float(end_lat)*1000)) and (int(float(home[1])*1000)==int(float(end_longi)*1000))):
        if(((int(float(work[0])*1000))==int(float(lat)*1000)) and (int(float(work[1])*1000)==int(float(longi)*1000))):
            if(time_hr>=16 and time_hr<=20):
                mydict['name']=user
            	mydict['OfferName']="Tuna Offer!"
          	mydict['OfferDetails']="50% off at Foodlion"
            	mydict['lat']= str(foodlion[0])
            	mydict['longi'] = str(foodlion[1])
        elif(((int(float(gym[0])*1000))==int(float(lat)*1000)) and (int(float(gym[1])*1000)==int(float(longi)*1000))):
            if((time_hr>=7 and time_hr<=10) or (time_hr>=17 and time_hr<=21)):
                mydict['name']=user
            	mydict['OfferName']="Gatorade Offer!"
                mydict['OfferDetails']="Buy one get one Gatorade Free at 6 Twelve Convenient Store"
            	mydict['lat']= str(convenient[0])
            	mydict['longi'] = str(convenient[1])
    return mydict


@app.route('/')
def func_root():
	j2_env = Environment(loader=FileSystemLoader(THIS_DIR),trim_blocks=True)
	return j2_env.get_template('maps.html').render(title="Context based Advertising")


#Main function that handles the post request
@app.route('/<user>/<lat>/<longi>/<end_lat>/<end_longi>/<time1>',methods=['POST'])
def func_main(user,lat,longi,end_lat,end_longi,time1):
	data=get_offers(user,lat,longi,end_lat,end_longi,time1)

	js = json.dumps(data)
	resp = Response(js, status=200, mimetype='application/json')
        #resp.headers['Link'] = 'http://luisrei.com'
	print js
	msg=''
        if(bool(data)):
            if('Tuna' in data['OfferName']):
        	    start_lat=str(work[0])
        	    start_longi=str(work[1])
             	    end_lat=str(foodlion[0])
        	    end_longi=str(foodlion[1])
                    msg='\n'+'Hi '+user+'\n'+data['OfferName']+'\n'+data['OfferDetails']+'\n'+'http://bit.ly/2enVcQV'

            elif('Gatorade' in data['OfferName']):
	    	    start_lat=str(gym[0])
                    start_longi=str(gym[1])
                    end_lat=str(convenient[0])
                    end_longi=str(convenient[1])
                    msg='\n'+'Hi '+user+'\n'+data['OfferName']+'\n'+data['OfferDetails']+'\n'+'http://bit.ly/2dSGUeR'

	    #https://www.google.com/maps/dir/35.874435,-78.842677/35.775295,-78.685293 == http://bit.ly/2enVcQV
            #https://www.google.com/maps/dir/35.783728,-78.672094/35.775295,-78.685293 == http://bit.ly/2dSGUeR
            send_sms(msg)
	return resp

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
