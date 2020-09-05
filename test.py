from multiprocessing import Pool
import requests
import time

def f(line):
    print(requests.get(line))


if __name__ == '__main__':
    start=time.time()
    urls = open('data.txt').read().splitlines()
    p = Pool(1)
    p.map(f, urls)
    end=time.time()
    print("Total:",end-start)