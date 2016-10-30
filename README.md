## Inspiration
Who has not installed AdBlock extensions? Ads are synonymous to annoyance and irrelevance. Most companies' sole income is through advertisements for example blogs, google news. Ads are a big deal for the survival of many companies and at the same time if right Ads are sent to right people at the right time they can be a real benefit to customers.

We propose a solution which:
1. Provides useful ads to users without annoying them.
2. proposes very less or minimal detour from their regular activities.
3. Enterprise - Providing customized offers to keep loyal customers happy.

Smart Ads are crucial for customers - enterprise ecosystem.

## What it does
Presenting Smart Ads - which provides advertisement to the customers based on

***Bills OCR Analysis*** - User scans and uploads bills via phone app and analysis is done on it to gain insights into user preferences for potential offers.
Google Calendar Sync - Uses Calendar events to decide ad notifications. For ex: If the user is going to a birthday party for the weekend, ads related to offers on wine or gifts can be shown on the route.
***Location based:*** Uses the current location of the user and calendar event to notify ads to users.

## How I built it

1. *Android app* - Used for scan and upload of purchase recipts, and periodically sends location to our cloud endpoint.
2. *AWS Server* - All OCR analysis done here, from getting text from scanned image, to categorizing purchases, and learning user preferences. Calendar events for the user are synced to get upcoming event details. REST endpoint is provided using Flask, to get potential offers from partner enterprises based on location. Matched result offers are pushed by SMS to user via Twilio.
3. *JS Application* - Hosted on AWS to provide Map Visualization to demonstrate the backend application features.


###APIs Used
1. ESRI - Mapping Location Name to (lat,long) co-ordinates (geo-coding).
2. Amazon SQS: To queue the location data and process at regular intervals.
3. TWILIO - Sending SMS to user for pushing offers.
4. PYTESSER - Tesseract OCR Python lib.
5. OpenCV - Crop and perspective transformation for image manipulation.
6. GOOGLE MAPS - Google Maps to visualize the JS Application.

##Team Members and Responsibilities
1. Aniket Dhuri - Android App and Flask REST API
2. Chethan NT - Flask REST API and JS Application
3. Saurabh Sakpal - ESRI API , JS Application and Calendar
4. Utkarsh Verma  - OCR , Image Transformation and JS Application


## Challenges I ran into
1. Android application crash due to OS terminating location listenerService indeterminately while running in background- resolved using startForeground(). 
2. REST API providing blank output due to result of incorrect POST methods - resolved using debugging various scenarios.
3. Demonstrating the back end code needed some discussions and overhead - resolved using creating a javascript application to depict the backend functionality.

## Accomplishments that I'm proud of
1. Worked on various platforms to have complete exposure to the frameworks and technologies used.
2. Choosing team members who were motivated and provided constructive feedback on the decisions taken during the 24 hours of coding.

## What I learned
1. Perseverance - bugs everywhere, don't give up - fix'em all
2. Android - quick refresher for me after 4 years.
3. Flask - REST endpoints using Flask.
4. Fun - Enjoy while you code , especially pair programming.
5. OCR - Using tesseract OCR.


## What's next for Smart Ads

 We were discussing about how to leverage the  use case for benefiting the enterprise, and came up with various solutions ranging from -

 1. Adding support in Android to add offers based on keywords and/or    
    interfacing with restaurant APIs to provide customized offers to
    each    individual. 
 2. Providing a feature to users  to add list of the items    they purchase frequently ( based on points the user has accumulated    by
    buying more offers ).
