import requests
import bs4
import apfm_main as ap

r=requests.get('https://www.aplaceformom.com/community/merrill-gardens-at-first-hill-71358')
soup=bs4.BeautifulSoup(r.text,'lxml')

metas = soup.find_all('meta')
print ([ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ])
