# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:56:16 2021

@author: prajj
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
query = 'comprehensive guide to machine learning in python'
title = [] 
page_url = [] 
description = [] 
page_number = [] 
search_page = [] 
n_pages = 10
for page in range(1, n_pages):
    
    url = "http://www.google.com/search?q="+query+"&start="+str((page - 1) * 10)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    url_div = soup.find_all('div', class_ = "yuRUbf")
    title_div = soup.find_all('h3',class_ = "LC20lb DKV0Md")
    disc_div = soup.find_all('div', class_ = "IsZvec")
    for i in url_div:
        page_url.append(i.a.get('href'))
    for i in title_div:
        title.append(i.text)
    for i in disc_div:
        description.append(i.select_one("span").get_text(strip = True))
    k = 1
    for i in url_div:
        page_number.append(page)
        search_page.append(k)
        k+=1
final_dict ={'Page_Number':page_number,'Search_Result':search_page,'Search_Result_Title':title,'Search_Result_URL':page_url,'Search_Result_Description':description}
df=pd.DataFrame(final_dict)
df.to_csv('Final_output.csv',index=False)
        
        
    
    

