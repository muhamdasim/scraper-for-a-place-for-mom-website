import pandas as pd
import requests
import bs4

#load urls from the file
df=pd.read_csv('apfm-urls.csv')

#load all urls in the list for future use
all_urls=[]
for i in df['Address']:
    all_urls.append(i)


r=requests.get(all_urls[0])

