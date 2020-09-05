from multiprocessing import Pool
import requests
import time
from bs4 import BeautifulSoup
import apfm_scraper as scraper
import  csv
import sys

url = []
global pageTitle
pageTitle=[]
metaDescription = []
communityReviews = []
communityStreetAddress = []
communityCity = []
communityState = []
communityZipCode = []
communityImages = []
communityContent = []
noOfReviews = []
averageProfileScore = []
careTypesProvided = []
communityAmenities = []
licenseNo = []


def f(i):
    url.append(i)
    # Fetching Data
    print("Fetching:", i)
    soup = scraper.pageRequests(i)
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
    # Fetching License No
    licenseNo.append(scraper.getLicenseNo(soup))

    with open("apfm-data.csv", "w", newline='', encoding="utf-8") as csvFile:
        fieldnames = ['url', 'pageTitle', 'metaDescription', 'communityReviews', 'communityStreetAddress', 'communityCity','communityState', 'communityZipCode', 'communityImages', 'communityContent', 'noOfReviews','averageProfileScore', 'careTypesProvided', 'communityAmenities', 'licenseNo']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        for link, pTitle, mDescription, cReviews, cStreetAddress, cCity, cState, cCode, cImages, cContent, nReviews, aScore, cProvided, cAmenities, lNo in zip(url, pageTitle, communityReviews, metaDescription, communityStreetAddress, communityCity, communityState,communityZipCode, communityImages, communityContent, noOfReviews, averageProfileScore, careTypesProvided,communityAmenities, licenseNo):
            writer.writerow({'url': link, 'pageTitle': pTitle, 'metaDescription': mDescription, 'communityReviews': cReviews,'communityStreetAddress': cStreetAddress, 'communityCity': cCity, 'communityState': cState,'communityZipCode': cCode, 'communityImages': cImages, 'communityContent': cContent,'noOfReviews': nReviews, 'averageProfileScore': aScore, 'careTypesProvided': cProvided,'communityAmenities': cAmenities, 'licenseNo': lNo})

        csvFile.close()



# function_calling
if __name__ == '__main__':


    l = urls = open('data.txt').read().splitlines()
    start=time.time()
    urls = open('xx.txt').read().splitlines()
    p = Pool(5)
    p.map(f, urls)
    for i in pageTitle:
        print(i)

    end=time.time()
    print("Total:",end-start)

    sys.exit()

