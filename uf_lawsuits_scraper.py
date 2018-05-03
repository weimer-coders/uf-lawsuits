from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
import csv
# import sleep
import pytesseract
import sys
import argparse
import os

def getResults():
    global driver
    company = driver.find_element_by_name("CompanyName").send_keys("University of Florida")
    startdate = driver.find_element_by_name("StartFileDate").send_keys("01/01/2012")
    enddate = driver.find_element_by_name("EndFileDate").send_keys("12/31/2017")
    button = driver.find_element_by_xpath("//input[@value='Search']")
    button.click()

# function to get the links for the first page that uses html
def getLinks(pageVals):
    global driver
    # viewAll = driver.find_element_by_xpath("//*[@id='contents']/table[2]/tbody/tr[54]/td/table/tbody/tr/td[3]").click()
    #go down the page to the section with this class
    time.sleep(4)
    pageSection = driver.find_element_by_xpath("//*[@id='contents']/table")
    print("What a lovely table")
    time.sleep(4)
    # find the a tags within a specific table
    pageNav = pageSection.find_elements_by_xpath("/html/body/div/div/table/tbody/tr/td/a[contains(@href,'section=summary')]")
    for pageLink in pageNav:
        pageVals.append(pageLink.get_attribute('href'))
        print ("Hey look, some links")
        print (pageVals)

def getDetails(pageVals):
    global driver
    global data
    #for each link in the list you have stored in pageVals
    for value in pageVals:
        #open each link
        driver.get(value)
        time.sleep(4)
        dockets = driver.find_element_by_xpath("//*[@id='primary']/li[4]/a")
        dockets.click()
        time.sleep(4)
        documents = driver.find_elements_by_xpath("/html/body/div/div/table/tbody/tr/td[@align='center']/a")
        for document in documents:
            time.sleep(2)
            document.click()
            time.sleep(2)

            # html = driver.find_element_by_xpath("//*[@id='download']")
            # if html:
            #     print("HTML!")




# def getDocuments(docVals):
#     global driver
#     global data
#     for docVal in docVals:
#         driver.get(docVal)
#         time.sleep(4)
#         button = driver.find_element_by_id("download")
#         button.click()
#         time.sleep(4)
#         print ("Did I work? Who the fuck knows.")

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
profile.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
profile.set_preference("pdfjs.disabled", True)
driver = webdriver.Firefox(profile)
driver.get("https://www.alachuaclerk.org/court_records/gis/index.cfm")
# profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
#                "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}

time.sleep(10)
#your lists where info will be stored
pageVals = []
docVals = []
# inmates = []
#run the functions, using the values (links) of the lists we created

getResults()
getLinks(pageVals)
#
getDetails(pageVals)
# getDocuments(docVals)
driver.close() # close the driver
