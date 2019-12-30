#!/usr/bin/python
# #-*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from pandas import Series,DataFrame
import pandas as pd
import numpy as np 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
import re
import csv

df = pd.DataFrame() #創建空間
headerlist = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
           "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"]


def lemon():
    lista = ['2','7','13','14','8','5','16','11','15']
    for cate in lista:
        print(cate)
        time.sleep(1)
        for page in range(1,2):

            url = requests.get('https://www.ettoday.net/dalemon/collection/'+str(cate)+'/'+str(page)).text
            soup = BeautifulSoup(url, 'html.parser')
            #cate1 = soup.find('div', 'subject_topic clearfix').find('h3').text
            

            for ele in soup.find('div', 'part_pictxt_1 topic-page').find_all('div','piece clearfix'):
                
                
                datelist = re.findall('(\d+)',ele.find(itemprop='datePublished').get('content')) #利用re正規式找出時間
                
                del datelist[3] #刪除時分秒
                del datelist[3]
                del datelist[3]
                del datelist[3]
                
                datestr = datelist[0] + datelist[1] + datelist[2] #接成字符串
                
                if datestr == time.strftime("%Y%m%d"): #如果為當日就存入
            
                    a = pd.Series({"category":soup.find('div', 'subject_topic clearfix').find('h3').text,"title":ele.find('h3').text.strip(),"href":ele.find('a')['href']})
                    global df
                    df = df.append(a,ignore_index = True)
    print('鍵盤酸檸檬 Done')



if __name__ == '__main__':


    lemon()

    print(df) # 看看資料框的外觀

    df.to_csv('Result.txt')

	