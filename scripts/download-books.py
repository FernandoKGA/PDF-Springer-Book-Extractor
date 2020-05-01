import requests, re
from selenium import webdriver

browser = webdriver.Firefox()
springerLinks = open('./files/links.txt','r')

for springerLink in springerLinks.readlines():
    link = springerLink.replace('\n','')
    browser.get(link)

    href = browser.find_element_by_xpath("//a[starts-with(@href, '/content/pdf')]").get_attribute('href')
    
    response = requests.get(href)
    
    if response.status_code == requests.codes.ok:
        con_disp = response.headers.get('content-disposition','empty')
        if con_disp == 'empty':
            print("empty:"+href)
        else:
            filename = con_disp.split('filename=')[1]
        
            book = open('./books/'+filename,'wb')
            book.write(response.content)
            book.close()