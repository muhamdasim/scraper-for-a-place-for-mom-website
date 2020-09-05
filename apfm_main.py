import apfm_scraper as scraper
import  csv
from bs4 import BeautifulSoup
import time



# function_calling
l=urls = open('data.txt').read().splitlines()
url=[]
pageTitle=[]
metaDescription=[]
communityReviews=[]
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
licenseNo=[]


start=time.time()
for idx, i in enumerate(l):
    try:
        print("Fetching No:",idx," ",i)
        soup = scraper.pageRequests(i)
        ln=scraper.getLicenseNo(soup)
        licenseNo.append(ln)
        url.append(i)
        #Fetching Data
        # Fetching Page Title
        pageTitle.append(scraper.getPageTitle(soup))
        # Fetching Community Name
        communityReviews.append(scraper.getCommunityName(soup))
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

    except:
        continue


end=time.time()
print("Total Time:",end-start)


with open("apfm-data.csv", "w",newline='',encoding="utf-8") as csvFile:
    fieldnames = ['url','pageTitle','metaDescription','communityReviews','communityStreetAddress','communityCity','communityState','communityZipCode','communityImages','communityContent','noOfReviews','averageProfileScore','careTypesProvided','communityAmenities','licenseNo']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    for link,pTitle,mDescription,cReviews,cStreetAddress,cCity,cState,cCode,cImages,cContent,nReviews,aScore,cProvided,cAmenities,lNo in zip(url,pageTitle,communityReviews,metaDescription,communityStreetAddress,communityCity,communityState,communityZipCode,communityImages,communityContent,noOfReviews,averageProfileScore,careTypesProvided,communityAmenities,licenseNo):
        writer.writerow({'url':link,'pageTitle':pTitle,'metaDescription':mDescription,'communityReviews':cReviews,'communityStreetAddress':cStreetAddress,'communityCity':cCity,'communityState':cState,'communityZipCode':cCode,'communityImages':cImages,'communityContent':cContent,'noOfReviews':nReviews,'averageProfileScore':aScore,'careTypesProvided':cProvided,'communityAmenities':cAmenities,'licenseNo':lNo})
