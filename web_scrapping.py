import mechanize
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
import http.cookiejar as cookielib
from time import sleep

#base_url = "https://cetesb.sp.gov.br"
#url_site = f'{base_url}/qualar/home.do'

#ff = webdriver.Firefox()
#ff.get(url_site)
#sleep(3)
#bs_obj = bs(ff.page_source, 'htlm.parser')



cookies = cookielib.CookieJar()
browser = mechanize.Browser()
browser.set_cookiejar(cookies)
sleep(3)

browser.open('https://cetesb.sp.gov.br/qualar/home.do')
sleep(3)
browser.select_form(td=0)      # o formulário de senha é o primeiro
browser.form['cetesb_login'] = 'ludmillaconti@outlook.com'     # substitua 'seu_email' pelo seu e-mail
browser.form['cetesb_passward'] = 'cinamo'  # substitua 'senha' pela sua senha
browser.submit()               # submissão dos dados

pagina = browser.response().read()  # essa é a página que você queria

# Beautiful Soup aqui
#soup = bs(pagina,'html.parser')
#codigo = soup.find("pre",{"id":"code"}).text

#print(codigo) # o dado que você buscava
