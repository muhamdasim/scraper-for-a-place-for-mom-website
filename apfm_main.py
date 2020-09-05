import apfm_scraper as scraper
import  csv


# function_calling

l=[]
l.append('https://www.aplaceformom.com/community/merrill-gardens-at-first-hill-71358')
l.append('https://www.aplaceformom.com/community/aegis-living-of-queen-anne-on-galer-1388600')

pageTitle=[]

for i in l:
    # Fetching Data
    print("Fetching:",i)
    soup = scraper.pageRequests(i)
    # Fetching Page Title
    pageTitle.append(scraper.getPageTitle(soup))
    # Fetching Community Name
    communityName = list(scraper.getCommunityName(soup))
    # Fetching Meta Description
    metaDescription = list(scraper.getMetaDescription(soup))
    # Fetching Community Street Address
    communityStreetAddress = list(scraper.getCommunityStreetAddress(soup))
    # Fetching Community City
    communityCity = list(scraper.getCommunityCity(soup))
    # Fetching Community State
    communityState = list(scraper.getCommunityState(soup))
    # Fetching Community Zip Code
    communityZipCode = list(scraper.getCommunityZipCode(soup))
    # Fetching Images Urls
    communityImages = list(scraper.getCommunityImages(soup))
    # Fetching Community Detail
    communityContent = list(scraper.getCommunityContent(soup))
    # Fetching No OF Reviews
    noOfReviews = list(scraper.getNumberofReviews(soup))
    # Fetching Average Review Score
    averageReviewScore = list(scraper.getAverageReviewScore(soup))
    # Fetching Care Types
    careTypeProvided = list(scraper.getCareTypesProvided(soup))
    # Fetching Community Amenities
    communityAmenities = list(scraper.getCommunityAmenities(soup))


for i in pageTitle:
    print(i)