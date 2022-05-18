print('بسمه الله الرحمن الرحیم')
print('salam bar mohammadreza dehghan amiri')
import copy
import datetime
import itertools
import json
import re
import time
from collections import OrderedDict
from copy import deepcopy
from curses import COLOR_BLACK

import numpy as np
import pandas as pd
import requests
import schedule
from bs2json import bs2json
from bs4 import BeautifulSoup as b
from iteration_utilities import unique_everseen
from rich import print
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from sqlalchemy import create_engine
#######################
import anardoni_categori_name
import anardoni_get_link
import anardoni_meta
########################

def get_cat_link_name(page_link):
    s = requests.session()
    sg = anardoni_categori_name.GETCATEGORI(page_link, s)
    sgg = sg.get_cat_link_name()
    return(anardoni_categori_name.cat_link_name_list)

def get_link_list(page_link):
    s = requests.session()
    sg = anardoni_get_link.GETLINK(page_link, s)
    sgg = sg.get_content_link()
    return(anardoni_get_link.total_link)

def get_metadata(content_link):
    s = requests.session()
    sg = anardoni_meta.GETMETA(content_link,s)
    sgg = sg.get_meta()
    return(anardoni_meta.meta_data_list)
##################################################################################
date_a=datetime.datetime.now()
engine = create_engine('postgresql://postgres:12344321@10.32.141.17/anardoni',pool_size=20, max_overflow=100,)
con=engine.connect()

cat=get_cat_link_name('https://anardoni.com/ios/categories')
cat_link=cat[0]
cat_name=cat[1]
# print(cat_link)
# print(cat_name)
for i in range(len(cat_link)):
    print(cat_link[i])
    link=get_link_list(cat_link[i])
    print(link)
    for j in range(len(link[0])):
        
        link_meta=get_metadata(link[0][j])
        print(link_meta)
        date_i=datetime.datetime.now()
        link_meta[0]['crawling_date']=str(date_i.date()).replace('-','')+str(date_i.time()).split(':')[0]
        link_meta[0]['categori_name']=cat_name[i]
        if link_meta[0]['categori_name']=='بازی‌ها':
            link_meta[0]['cat']='game'
        else:
            link_meta[0]['cat']='program'

        data_frame =pd.DataFrame(link_meta[0],index=[0])
        data_frame.to_sql('anardoni_meta'+str(date_a.date()).replace('-','')+str(date_a.time()).split(':')[0],con,if_exists='append', index=False)
        # print(link_meta[0])



# get_link_list('https://anardoni.com/ios/featured/magazines and newspapers')
# print(get_link_list('https://anardoni.com/ios/featured/travel'))
# link_meta=get_metadata('https://anardoni.com/ios/app/2Qfg2Jina')
# print(link_meta[0])