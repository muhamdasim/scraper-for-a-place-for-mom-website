import pandas as pd
import apfm_scraper as scraper

#load urls from the file
df=pd.read_csv('apfm-urls.csv')

#function to push all the urls to list
def allUrls():
    all_urls=[]
    for i in df['Address']:
        all_urls.append(i)

    return all_urls




#function_calling
allUrls()
#Requesting Urls
soup=scraper.pageRequests()
#Fetching Data

#Fetching Page Title
print(scraper.getPageTitle(soup))
#Fetching Community Name
print(scraper.getCommunityName(soup))
#Fetching Meta Description
print(scraper.getMetaDescription(soup))
#Fetching Community Street Address
print(scraper.getCommunityStreetAddress(soup))
