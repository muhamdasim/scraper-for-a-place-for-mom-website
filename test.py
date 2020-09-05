from multiprocessing import Pool
import requests
import time
from bs4 import BeautifulSoup


def f(line):
    d=requests.get(line)
    name=r"C:\Users\muham\PycharmProjects\" '+str(line)+".html"
    f=open(f'  {name.replace("https://www.aplaceformom.com/community/","")}', 'w+',  encoding="utf-8")
    f.write(d.text)


if __name__ == '__main__':
    start=time.time()
    urls = open('data.txt').read().splitlines()
    p = Pool(1)
    p.map(f, urls)
    end=time.time()
    print("Total:",end-start)