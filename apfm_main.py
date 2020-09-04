import apfm_scraper as scraper

# function_calling
scraper.allUrls()


# Fetching Data
soup = scraper.pageRequests()

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

df=scraper.pd.read_csv('apfm-data.csv')