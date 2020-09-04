import pandas as pd
import apfm_scraper as scraper

#load urls from the file
df=pd.read_csv('apfm-urls-final.csv')


#function to push all urls to list
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
#Fetching Community City
print(scraper.getCommunityCity(scraper.getCommunityStreetAddress(soup)))
#Fetching Community State
print(scraper.getCommunityState(scraper.getCommunityStreetAddress(soup)))
#Fetching Community Zip Code
print(scraper.getCommunityZipCode(scraper.getCommunityStreetAddress(soup)))
#Fetching Images Urls
print(scraper.getCommunityImages(soup))
#Fetching Community Detail
print(scraper.getCommunityContent(soup))
#Fetching No OF Reviews
print(scraper.getNumberofReviews(soup))
#Fetching Average Review Score
print(scraper.getAverageReviewScore(soup))
#Fetching Care Types
print(scraper.getCareTypesProvided(soup))
#Fetching Community Amenities
print(scraper.getCommunityAmenities(soup))