import apfm_scraper as scraper
import  csv
from bs4 import BeautifulSoup

# function_calling

l=[]
l.append('https://www.aplaceformom.com/community/merrill-gardens-at-first-hill-71358')
l.append('https://www.aplaceformom.com/community/aegis-living-of-queen-anne-on-galer-1388600')

url=[]
pageTitle=[]
metaDescription=[]
communityName=[]
communityStreetAddress=[]
communityCity=[]
communityState=[]
communityZipCode=[]
communityImages=[]
communityContent=[]
noOfReviews=[]
averageProfileScore=[]
careTypesProvided=[]
communityAmenities=[]

fl=[]

with open("merrill-gardens-at-first-hill-71358.html",encoding='utf-8') as f:
  fl.append(BeautifulSoup(f,'lxml'))

s

for i in fl:
    soup=i
    # Fetching Data
    #print("Fetching:",i)
    #soup = scraper.pageRequests(i)
    # Fetching Page Title
    pageTitle.append(scraper.getPageTitle(soup))
    # Fetching Community Name
    communityName.append(scraper.getCommunityName(soup))
    # Fetching Meta Description
    metaDescription.append(scraper.getMetaDescription(soup))
    # Fetching Community Street Address
    communityStreetAddress.append(scraper.getCommunityStreetAddress(soup))
    # Fetching Community City
    communityCity.append(scraper.getCommunityCity(soup))
    # Fetching Community State
    communityState.append(scraper.getCommunityState(soup))
    # Fetching Community Zip Code
    communityZipCode.append(scraper.getCommunityZipCode(soup))
    # Fetching Images Urls
    communityImages.append(scraper.getCommunityImages(soup))
    # Fetching Community Detail
    communityContent.append(scraper.getCommunityContent(soup))
    # Fetching No OF Reviews
    noOfReviews.append(scraper.getNumberofReviews(soup))
    # Fetching Average Review Score
    averageProfileScore.append(scraper.getAverageReviewScore(soup))
    # Fetching Care Types
    careTypesProvided.append(scraper.getCareTypesProvided(soup))
    # Fetching Community Amenities
    communityAmenities.append(scraper.getCommunityAmenities(soup))


