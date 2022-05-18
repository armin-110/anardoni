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

cat_link_name_list=[]
class GETCATEGORI():
    def __init__ (self,page_link,s):
        self.page_link =page_link
        self.s=s
        ##################################################################################
    def get_cat_link_name(self):
        cat_link_name_list.clear()
        response = self.s.get(self.page_link, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"})
        page_html=response.text
        page_html_soup = b(page_html, 'html.parser')

        converter = bs2json()
        class_find_name= page_html_soup.findAll('div', {'class': 'col-6 col-md-4 col-lg-3 category-box-desktop'}) 
        # class_find_name= page_html_soup.findAll('div', {'class': 'tab-pane fade in active show padding-top-20'}) 
        json_class_find_name = converter.convertAll(class_find_name)
        categori_link_list=[]
        categori_name_list=[]
        # print(json_class_find_name[0]['a']['attributes']['href'])#link
        # print(json_class_find_name[0]['a']['h2']['text'])#name
        for i in range(len(json_class_find_name)):
            # try:
            categori_link_list.append('https://anardoni.com'+json_class_find_name[i]['a']['attributes']['href'])
            categori_name_list.append(json_class_find_name[i]['a']['h2']['text'])
            # except:
                    # pass
        cat_link_name_list.append(categori_link_list)
        cat_link_name_list.append(categori_name_list)