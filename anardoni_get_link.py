from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import pandas as pd
import numpy as np
from bs2json import bs2json
import re
import json
import copy
from copy import deepcopy
import requests
from collections import OrderedDict
from iteration_utilities import unique_everseen
import time
import itertools
total_link=[]

class GETLINK():
    def __init__ (self,page_link,s):
        self.page_link =page_link
        self.s=s
        ##################################################################################
    def get_content_link(self):
        total_link.clear()
        response = self.s.get(self.page_link, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"})
        page_html=response.text
        page_html_soup = b(page_html, 'html.parser')
        converter = bs2json()
        
        link_list=[]
        more_link_list=[]
        for a in page_html_soup.find_all('a', href=True):
            
            # link_list.append(a['href'])
            if 'pack' in a['href']:
                more_link_list.append('https://anardoni.com'+a['href'])
            
            x = a['href'].split("/")
            # link_list.append(x)
            if len(x)==5:
                y=('https://anardoni.com'+a['href']).rsplit('/', 1)[0]
                link_list.append(y)

        # print(link_list)  
        # print(more_link_list) 
        # link_list0=[]
        for i in range(len(more_link_list)):
            response = self.s.get(more_link_list[i], headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"})
            page_html=response.text
            page_html_soup = b(page_html, 'html.parser')
            converter = bs2json()
            for a in page_html_soup.find_all('a', href=True):
                # link_list0.append(a['href'])
                # x = a['href'].split("/")
                if 'app' in a['href']:
                    if 'apps' not in a['href']:
                        link_list.append('https://anardoni.com'+a['href'])
        link_list= list(dict.fromkeys(link_list))
        # print(link_list)
        # print(len(link_list))
        total_link.append(link_list)






