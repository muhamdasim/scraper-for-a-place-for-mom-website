import requests
import bs4
import re
import json
import pandas as pd


#load urls from the file


#function to push all urls to list
def allUrls():
    df = pd.read_csv('tests.csv')
    all_urls=[]
    for i in df['Address']:
        all_urls.append(i)
    return all_urls

def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))

def pageRequests(url):
    r=requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup

def getPageTitle(soup):
    return soup.title.string.strip()

def getCommunityName(soup):
    return soup.find(class_='community-desc').h1.text

def getMetaDescription(soup):
    meta = soup.find_all('meta')
    return listToString([meta.attrs['content'] for meta in meta if 'name' in meta.attrs and meta.attrs['name'] == 'description'])



def getCommunityStreetAddress(soup):
    return soup.find( class_='community-desc').p.text

def getCommunityCity(soup):
    text = soup.find(class_='js-react-on-rails-component').get_text()
    js = json.loads(text)
    return js['data']['Locality']

def getCommunityState(soup):
    text = soup.find(class_='js-react-on-rails-component').get_text()
    js = json.loads(text)
    return js['data']['RegionCode']

def getCommunityZipCode(soup):
    text = soup.find(class_='js-react-on-rails-component').get_text()
    js = json.loads(text)
    return js['data']['PostalCode']

def getCommunityImages(soup):
    text=soup.find(class_='js-react-on-rails-component').get_text()
    js=json.loads(text)
    image_urls=[]
    final_url=""
    url='https://www.aplaceformom.com/images/'
    for i in js['data']['ImageSet']:
        image_urls.append(url+str(i['LargeImageId']))

    for i in image_urls:
        final_url += i + ","

    return final_url[:-1]


def getCommunityContent(soup):
    content= soup.find('div',class_='community-detail').get_text().strip()
    return content.replace('Now offering virtual tours. Call us now to schedule.','').strip()

def getNumberofReviews(soup):
    return soup.find(class_='reviews-count-container').find("span").text.strip()

def getAverageReviewScore(soup):
    return soup.find(class_='score-container').find("span").text.strip()

def getCommunityAmenities(soup):
    amenities=[]
    str=""
    for i in soup.find(class_='List-order').findAll('li')[1:]:
        amenities.append(i.get_text())

    for i in amenities:
        str+=i+","

    return str[:-1]

def getCareTypesProvided(soup):
    caretype = []
    str = ""
    for i in soup.find_all(class_='on'):
        caretype.append(i.get_text())

    for i in caretype:
        str += i + ","

    return str[:-1]


def test(soup):
    text = soup.find(class_='js-react-on-rails-component').get_text()
    js = json.loads(text)
    for i in js['data']:
        print(i)

    print(js['data']['CommunityRoomPrices'])