#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:50:56 2017

@author: brianlee
"""

import requests, os, bs4, re, selenium, shelve

def getSignupPages():
    #pull the password from a file so that this can be shared
    #should return a webpage that soup can use
    from selenium import webdriver
    browser = webdriver.Chrome('/Users/brianlee/chromedriver')
    browser.get('https://clients.mindbodyonline.com/classic/home?studioid=35181')
    
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

    nextWeekBtn = browser.find_element_by_id('week-arrow-r')
    nextWeekBtn.click()
    nextWeekPage = browser.page_source
    
    return (currentWeekPage, nextWeekPage)
    

def getDrillAndPlays(soup):
    tableRows = soup.select('tr')
    drillAndPlays = [rows for rows in tableRows if "Drill & Play" in rows.getText()][1:]
    return drillAndPlays

def getOpenDrills(drillAndPlays):
    futureDrills = [drills for drills in drillAndPlays if 'Reserved' in drills.getText()]
    openRegex = re.compile(r'(\d{1,2})Open')
    openDrills = []
    for drill in futureDrills:
        drillText = drill.getText().replace('\xa0', '')
        regexMatch = openRegex.search(drillText)
        if regexMatch == None or 'Private' in drillText:
            pass
        else:
            openSpots = int(regexMatch.group(1))
            if openSpots > 0:
                openDrills.append(drill)
    return openDrills

def getSignUpInfo(openDrills):
    drillInfo = [] #list of tuples (date, court)
    dateRegex = re.compile('classDate\=(\d{1,2}/\d{1,2}/\d{4})')
    for drill in openDrills:
        drillHTML = str(drill)
        dateRegexMatch = dateRegex.search(drillHTML)
        if dateRegexMatch == None:
            pass
        else:
            drillDate = dateRegexMatch.group(1)
            #add day of week
            time = drill.select('td')[0].getText().replace('\xa0', '')
            if 'SUTTON EAST' in drillHTML:
                drillInfo.append((drillDate, time, 'Sutton East'))
            else:
                drillInfo.append((drillDate, time, 'Yorkville'))
    return drillInfo

def getOpenDrillInfo(signupPage):
    soup = bs4.BeautifulSoup(signupPage, 'lxml')
    drillAndPlays = getDrillAndPlays(soup)
    openDrills = getOpenDrills(drillAndPlays) 
    openDrillInfo = getSignUpInfo(openDrills)
    return openDrillInfo

(currentWeekPage, nextWeekPage) = getSignupPages()
openDrills = getOpenDrillInfo(currentWeekPage) + getOpenDrillInfo(nextWeekPage)
print(openDrills)
