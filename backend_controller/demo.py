import os
from flask import Flask, render_template, request, url_for,jsonify

app = Flask(__name__)

def get_offers(user,lat,longi,time,date):
    mydict={}
    string1="Tuna offer, 50% off at Foodlion"
    string2="80, 90"

    mydict['name']=user
    mydict['OfferName']="Tuna Offer"
    mydict['OfferDetails']="50% off at Foodlion"
    mydict['lat']= "80"
    mydict['longi'] = "90"
    return mydict


#Main function that handles the post request
@app.route('/<user>/<lat>/<longi>/<time>/<date>',methods=['POST'])
def func_main(user,lat,longi,time,date):

	return get_offers(lat,longi,time,date)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
