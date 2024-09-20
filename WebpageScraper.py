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

