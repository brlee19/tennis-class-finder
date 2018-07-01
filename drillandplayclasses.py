#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:50:56 2017

@author: brianlee
"""
#TODO: Call itself at some sort of set times and log the results
#TODO: Sign up for the classes based on user text input
#TODO: Analyze which time of day have the most openings
#TODO: Find a better way to import the right directories so this can be run from Terminal
#TODO: Add a way to filter classes by time
#TODO: Refactor so that global params (ie. venue) are in some sort of master wrapper function

#Below adds the right dirs when running from Terminal
import sys
dirs = ('/anaconda/lib/python36.zip',
'/anaconda/lib/python3.6',
'/anaconda/lib/python3.6/lib-dynload',
'/Users/brianlee/.local/lib/python3.6/site-packages',
'/anaconda/lib/python3.6/site-packages',
'/anaconda/lib/python3.6/site-packages/Sphinx-1.5.1-py3.6.egg',
'/anaconda/lib/python3.6/site-packages/aeosa',
'/anaconda/lib/python3.6/site-packages/IPython/extensions',
'/Users/brianlee/.ipython')
for folder in dirs:
    sys.path.append(folder)
    
import os, bs4, re, shelve, datetime

os.chdir('/users/brianlee/documents/python/drill_and_plays')

def getSignupPages():
    from selenium import webdriver
    browser = webdriver.Chrome('/Users/brianlee/chromedriver')
    browser.get('https://clients.mindbodyonline.com/classic/home?studioid=35181')
    browser.implicitly_wait(20)
    
    #get and then input user info
    emailElem = browser.find_element_by_id('requiredtxtUserName')
    userData = shelve.open('userData')
    emailElem.send_keys(userData['email'])
    passwordElem = browser.find_element_by_id('requiredtxtPassword')
    passwordElem.send_keys(userData['password'])
    userData.close()
    loginElem = browser.find_element_by_id('btnLogin')
    loginElem.click()
    
    classesTab = browser.find_element_by_id('tabA7') 
    classesTab.click()
    currentWeekPage = browser.page_source
    signup_pages = [currentWeekPage]

    for i in range(20):
        nextWeekBtn = browser.find_element_by_id('week-arrow-r')
        nextWeekBtn.click()
        nextWeekPage = browser.page_source
        signup_pages.append(nextWeekPage)
    
    return signup_pages
    
def getDrillAndPlays(soup):
    tableRows = soup.select('tr')
    drillAndPlays = [rows for rows in tableRows if "Drill & Play" in rows.getText()][1:]
    return drillAndPlays

def getOpenDrills(drillAndPlays, venue=None):
    if venue:
        #if specifying one venue
        futureDrills = [drills for drills in drillAndPlays if 'Reserved' in drills.getText() and venue.upper() in drills.getText()]
    else:
        futureDrills = [drills for drills in drillAndPlays if 'Reserved' in drills.getText()]
    openRegex = re.compile(r'(\d{1,2})Open')
    openDrills = []
    for drill in futureDrills:
        drillText = drill.getText().replace('\xa0', '')
        regexMatch = openRegex.search(drillText)
        if regexMatch and 'Private' not in drillText:
            openSpots = int(regexMatch.group(1))
            if openSpots > 0:
                openDrills.append(drill)
    return openDrills

def getSignUpInfo(openDrills):
    # venue is "Sutton East" or "Yorkville"
    drillInfo = ''
    dateRegex = re.compile('classDate\=(\d{1,2}/\d{1,2}/\d{4})')
    for drill in openDrills:
        drillHTML = str(drill)
        dateRegexMatch = dateRegex.search(drillHTML)
        if dateRegexMatch:
            drillDate = dateRegexMatch.group(1)
            drillDateTime = datetime.datetime.strptime(drillDate, '%m/%d/%Y')
            formattedDate = drillDateTime.strftime('%b-%d (%a) ')
            time = drill.select('td')[0].getText().replace('\xa0', '')
            drillInfo += formattedDate + time + ' '
            if 'SUTTON EAST' in drillHTML:
                drillInfo += 'Sutton East\n'
            else:
                drillInfo += 'Yorkville\n'
    return drillInfo

def getOpenDrillInfo(signupPage):

    soup = bs4.BeautifulSoup(signupPage, 'lxml')
    drillAndPlays = getDrillAndPlays(soup)
    openDrills = getOpenDrills(drillAndPlays, 'Yorkville') #specify venue here
    openDrillInfo = getSignUpInfo(openDrills)
    return openDrillInfo

def textOpenDrillInfo(openDrills):
    from twilio.rest import Client
    userData = shelve.open('userData')
    twilioData = userData['twilio']
    twilioCli = Client(twilioData['accountSID'], twilioData['authToken'])
    twilioNumber = twilioData['twilioNumber']
    cellPhone = twilioData['cellPhone']
    
    twilioCli.messages.create(cellPhone, body=str(openDrills), from_=twilioNumber)

def testRun():
    '''analyzes a saved version of the website and prints the result to console
    instead of texting it'''
    
    testHTML = open('./test_examples/tennis2.htm')
    testOpenDrills = getOpenDrillInfo(testHTML)
    print(testOpenDrills)

if len(sys.argv) == 2 and sys.argv[1].lower() == 'test':
    testRun()
else:
    signup_pages = getSignupPages()
    openDrills = ''
    for page in signup_pages:
        if len(openDrills) < 1500:
            openDrills += getOpenDrillInfo(page)
            print(openDrills)
        else:
            break
    textOpenDrillInfo(openDrills)
