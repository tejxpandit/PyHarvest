# File : Web Scraper Library
# Project : PyHarvest
# Author : Tej Pandit
# Date : Sept 2024

# Inbuilt Requirements : random, time, pickle
# External Requirements : requests

import time
import pickle
import requests
import random

class WebpageScraper:
    def __init__(self):
        self.save = False
        self.log = False
        self.wait = False
        self.waitperiod = 1
        self.savefile = "webpage.scrape"
        self.user = RandomUserAgent()
        self.data = None
        self.data_format = None
    
    # SAVING
    def enableSave(self):
        self.save = True

    def disableSave(self):
        self.save = False

    def setSaveFilename(self, filename):
        self.save = True
        self.savefile = filename

    # LOGGING
    def enableLog(self):
        self.log = True

    def disableLog(self):
        self.log = False

    # WAITING between scrapes
    def enableWait(self):
        self.wait = True

    def disableWait(self):
        self.wait = False

    def setWaitTime(self, sleeptime):
        self.wait = True
        self.waitperiod = sleeptime

    def setWaitTimeRange(self, min_sleeptime, max_sleeptime):
        self.wait = True
        self.waitperiod = random.randrange(min_sleeptime, max_sleeptime)

    # Header Formatting 
    def getHeader(self):
        header = {'User-Agent': self.user.getUserAgent(),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
        return header