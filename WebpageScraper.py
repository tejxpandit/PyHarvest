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
    
    # SCRAPING
    # Single Link Scrape --> str(html)
    def getHTML(self, url):
        html = requests.get(url, headers=self.getHeader())
        if self.log:
            print(html.text)
        if self.wait:
            time.sleep(self.waitperiod)
        if self.save:
            self.data = html.text
            self.data_format = "str(html)"
            self.saveFile()
        return html.text
    
    # Multi-Link Scrape --> [str(html), str(html),....]
    def getHTMLs(self, urls):
        htmls = []
        for url in urls:
            html = requests.get(url, headers=self.getHeader())
            if self.log:
                print(html.text)
            if self.wait:
                time.sleep(self.waitperiod)
            htmls.append(html.text)
        if self.save:
            self.data = htmls
            self.data_format = "list[str(html), str(html),....]"
            self.saveFile()
        return htmls
    
    # Dict Link Scrape --> {"id1" : str(html), "id2" : str(html),....}
    def getHTMLDict(self, url_dict):
        html_dict = {}
        for id, url in url_dict.items():
            html = requests.get(url, headers=self.getHeader())
            if self.log:
                print(html.text)
            if self.wait:
                time.sleep(self.waitperiod)
            html_dict[id] = html.text
        if self.save:
            self.data = html_dict
            self.data_format = 'dict\{"id1" : str(html), "id2" : str(html),....\}'
            self.saveFile()
        return html_dict
    
    # Dict Multi-Link Scrape --> {"id1" : [str(html), str(html),...], "id2" : [str(html), str(html),...], ....}
    def getHTMLsDict(self, urls_dict):
        html_list_dict = {}
        for id, urls in urls_dict.items():
            htmls = []
            for url in urls:
                html = requests.get(url, headers=self.getHeader())
                if self.log:
                    print(html.text)
                if self.wait:
                    time.sleep(self.waitperiod)
                htmls.append(html.text)
            html_list_dict[id] = html
        if self.save:
            self.data = html_list_dict
            self.data_format = 'dict\{"id1" : list[str(html), str(html),....], "id2" : list[str(html), str(html),....], ....\}'
            self.saveFile()
        return html_list_dict
    
    # Write HTML to pickle file (to avoid rescaping)
    def saveFile(self):
        with open(self.savefile, "wb") as fp:
            pickle.dump(self.data, fp)
        print('Webpage Data Saved!\nfile-name : "' + self.savefile + '"\ndata-format: "' + self.data_format + '"')

#########################################

# User Agent Randomizer for HTML Requests

class RandomUserAgent:
    def __init__(self):
        self.users = user_agents

    def getUserAgent(self):
        return random.choice(user_agents)
    
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
    'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
]

#########################################