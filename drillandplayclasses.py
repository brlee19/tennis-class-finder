#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:50:56 2017

@author: brianlee
"""

import requests, os, bs4, re, selenium

def getSignupPage():
    #pull the password from a file so that this can be shared
    #should return a webpage that soup can use
    from selenium import webdriver
    browser = webdriver.Chrome('/Users/brianlee/chromedriver')
    browser.get('https://clients.mindbodyonline.com/classic/home?studioid=35181')
    emailElem = browser.find_element_by_id('requiredtxtUserName')
    emailElem.send_keys('blee@nyu.edu')
    passwordElem = browser.find_element_by_id('requiredtxtPassword')
    passwordElem.send_keys('5HrR2@K9%R')
    loginElem = browser.find_element_by_id('btnLogin')
    loginElem.click()
    
    classesTab = browser.find_element_by_id('tabA7') 
    classesTab.click()
    #should get both this week's sign up page and next week's too (right now only looks at next wk)
    #nextWeekBtn = browser.find_element_by_id('week-arrow-r')
    #nextWeekBtn.click()
    return browser.page_source
    

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

signupPage = getSignupPage()
soup = bs4.BeautifulSoup(signupPage, 'lxml')
drillAndPlays = getDrillAndPlays(soup)
openDrills = getOpenDrills(drillAndPlays) 
openDrillInfo = getSignUpInfo(openDrills)
print(openDrillInfo)