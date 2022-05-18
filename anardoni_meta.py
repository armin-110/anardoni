from curses import meta
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
meta_data_list=[]

class GETMETA():
    def __init__ (self,content_link,s):
        self.content_link =content_link
        self.s=s
        ##################################################################################

    def get_meta(self):
        meta_data_list.clear()
        meta_dic = {'cat':'','categori_name':'','content_name': '','content_link':self.content_link,'rate':'0','ratings':'0','Size':'','Download':'0','Current Version':'','Last Update':'','Creator':'','age range':'','Cost':'','crawling_date':''}
        # try:
        response = self.s.get(self.content_link, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"})
        page_html=response.text
        page_html_soup = b(page_html, 'html.parser')
        converter = bs2json()

        class_find_name= page_html_soup.findAll('h1') 
        json_class_find_name = converter.convertAll(class_find_name)
        print(json_class_find_name[0]['text'])
        meta_dic['content_name']=json_class_find_name[0]['text']#title

        class_find_name= page_html_soup.findAll('dl', {'class': 'css-1qi1ur8'}) 
        json_class_find_name = converter.convertAll(class_find_name)
        # print(json_class_find_name[0]['div'][5])
        # print(len(json_class_find_name[0]['div']))
        for i in range(len(json_class_find_name[0]['div'])):
            # print(json_class_find_name[0]['div'][i]['dt']['text'])
            if json_class_find_name[0]['div'][i]['dt']['text']=='فروشنده':
                print(json_class_find_name[0]['div'][i]['dt']['text'])
                try:
                    print(json_class_find_name[0]['div'][i]['dd']['a']['text'])
                    meta_dic['Creator']=json_class_find_name[0]['div'][i]['dd']['a']['text']
                except:
                    meta_dic['Creator']=json_class_find_name[0]['div'][i]['dd']['text']
            
            if json_class_find_name[0]['div'][i]['dt']['text']=='سایز':
                print(json_class_find_name[0]['div'][i]['dt']['text'])
                meta_dic['Size']=json_class_find_name[0]['div'][i]['dd']['text']
            
            if json_class_find_name[0]['div'][i]['dt']['text']=='دسته‌بندی':
                print(json_class_find_name[0]['div'][i]['dt']['text'])
                try:
                    meta_dic['categori_name']=json_class_find_name[0]['div'][i]['dd']['text']    
                except:
                    pass
            if json_class_find_name[0]['div'][i]['dt']['text']=='محدوده سنی':
                print(json_class_find_name[0]['div'][i]['dt']['text'])
                meta_dic['age range']=json_class_find_name[0]['div'][i]['dd']['text'] 

            if json_class_find_name[0]['div'][i]['dt']['text']=='نسخه':
                print(json_class_find_name[0]['div'][i]['dt']['text'])
                meta_dic['Current Version']=json_class_find_name[0]['div'][i]['dd']['text']     
            
            if json_class_find_name[0]['div'][i]['dt']['text']=='قیمت':
                print(json_class_find_name[0]['div'][i]['dt']['text'])
                meta_dic['Cost']=json_class_find_name[0]['div'][i]['dd']['text']  
        
        meta_data_list.append(meta_dic)
        # print(meta_data_list)
        # print(json_class_find_name[0]['div'][3]['dt']['text'])
        # print(json_class_find_name[0]['div'][3]['dd']['text'])