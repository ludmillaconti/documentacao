import mechanize
from bs4 import BeautifulSoup
#import urllib2
import http.cookiejar ## http.cookiejar in python3
from time import sleep

cj = http.cookiejar.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://cetesb.sp.gov.br/qualar/home.do")
sleep(3)

br.select_form(nr=0)
br.form['username'] = 'ludmillaconti@outlook.com'
br.form['password'] = 'cinamo'
br.submit()

print('Process Complete.')
#print br.response().read()
