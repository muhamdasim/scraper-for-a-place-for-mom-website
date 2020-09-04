import apfm_scraper as scraper
import  csv


# function_calling

scraper.allUrls()


# Fetching Data
soup = scraper.pageRequests()
url='https://www.aplaceformom.com/community/merrill-gardens-at-first-hill-71358'
# Fetching Page Title
pageTitle = scraper.getPageTitle(soup)
# Fetching Community Name
communityName = scraper.getCommunityName(soup)
# Fetching Meta Description
metaDescription = scraper.getMetaDescription(soup)
# Fetching Community Street Address
communityStreetAddress = scraper.getCommunityStreetAddress(soup)
# Fetching Community City
communityCity = scraper.getCommunityCity(scraper.getCommunityStreetAddress(soup))
# Fetching Community State
communityState = scraper.getCommunityState(scraper.getCommunityStreetAddress(soup))
# Fetching Community Zip Code
communityZipCode = scraper.getCommunityZipCode(scraper.getCommunityStreetAddress(soup))
# Fetching Images Urls
communityImages = scraper.getCommunityImages(soup)
# Fetching Community Detail
communityContent = scraper.getCommunityContent(soup)
# Fetching No OF Reviews
noOfReviews = scraper.getNumberofReviews(soup)
# Fetching Average Review Score
averageReviewScore = scraper.getAverageReviewScore(soup)
# Fetching Care Types
careTypeProvided = scraper.getCareTypesProvided(soup)
# Fetching Community Amenities
communityAmenities = scraper.getCommunityAmenities(soup)

with open("apfm-data.csv", "w",newline='',encoding="utf-8") as csvFile:
    fieldnames = ['url','pageTitle','metaDescription','communityName','communityStreetAddress','communityCity','communityState','communityZipCode','CommunityImages','communityContent','noOfReviews','averageProfileScore','careTypesProvided','communityAmenities']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    for u,pt,md,cn,csa,cc,cs,czc,ci,ccontent,nor,ars,ctp,ca in zip(url,pageTitle, metaDescription,communityName,communityStreetAddress,communityCity,communityState,communityZipCode,communityImages,communityContent,noOfReviews,averageReviewScore,careTypeProvided,communityAmenities):
        writer.writerow({'url': u, 'pageTitle': pt,'metaDescription': md,'communityName':cn,'communityStreetAddress':csa,'communityCity':cc,'communityState':cs,'communityZipCode':czc,'CommunityImages':ci,'communityContent':ccontent,'noOfReviews':nor,'averageProfileScore':ars,'careTypesProvided':ctp,'communityAmenities':ca})