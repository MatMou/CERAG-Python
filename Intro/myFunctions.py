# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:51:41 2020

@author: Camilo
"""

def fibonacci(n):
    a, b = 0, 1
    fib = []
    while a<n:
        fib.append(a)
        a, b = b, a+b
    return fib

def classer(classifier, number):
    if number>0:
        classifier['positive'].append(number)
    else:
        classifier['negative'].append(number)
    return classifier

def get_SP500tickers():
    import urllib.request
    from bs4 import BeautifulSoup as soup

    fp = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()

    page_soup = soup(mystr,"html.parser")

    container = page_soup.findAll("a",{"class":"external text"})
    pre_tickers = []
    for i in container: 
        pre_tickers.append(i.text)
    tickers = pre_tickers[::2]
    return tickers