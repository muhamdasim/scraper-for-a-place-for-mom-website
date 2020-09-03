import pandas as pd


#load urls from the file
df=pd.read_csv('apfm-urls.csv')

def all_urls:
    all_urls=[]
    for i in df['Address']:
        all_urls.append(i)



