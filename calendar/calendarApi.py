
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from Event import *
from Tagger import *
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from geopy.geocoders import Nominatim

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def checkIfKeyPresent(event, key):
    try:
        temp = event[key]
    except:
        return False
    else:
        return True


def getEventsForUser():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    #print(now)
    #print(datetime.datetime.now())
    #print('Getting the upcoming 20 events')
    eventsResult = service.events().list(calendarId='primary', timeMin=now, maxResults=20, singleEvents=True, orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    eventList = []
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        
        geocoordinates = None
        if(checkIfKeyPresent(event, 'location')):
            location = event['location'];
            geolocator = Nominatim()
            coordinates = geolocator.geocode(location)
            geocoordinates = [coordinates.latitude, coordinates.longitude]

        tagList = []

        description = None
        if checkIfKeyPresent(event, 'description'):
            description = event['description']
            tagList +=Tagger.getTags(description)

        summary = event['summary']
        tagList += Tagger.getTags(summary)

        eventObj = Event(start, summary, description, geocoordinates, list(set(tagList)))
        eventList.append(eventObj)
        #event.printContents()
    return eventList

def main():
    getEventsForUser()

if __name__ == '__main__':
    main()  