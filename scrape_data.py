from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import requests

my_url='https://www.flipkart.com/?gclid=CjwKCAjwns_bBRBCEiwA7AVGHshmNCMta4EEJbQdAefeh6xbnYswkgbDFUzqg8fXU8u57ji1db8SSRoCyq0QAvD_BwE&semcmpid=sem_8024046704_brand_eta_goog&s_kwcid=AL!739!3!260637261012!e!!g!!flipkart&ef_id=WUn55gAAAIJMOQ36:20180815161352:s'
uClient=uReq(my_url)
page_html=uClient.read().decode()
uClient.close()

page_soup=soup(page_html,"lxml")
div=page_soup.find_all('div',class_='iUmrbN')
lst=[]
lst1=[]
div1=page_soup.find_all('div',class_='_3BTv9X')
for i in div:
	lst.append(i.text)

div2=page_soup.find_all('div',class_='BXlZdc')
for j in div2:
	lst1.append(j.text)
for k in range(len(lst1)):
	print(k+1)
	print(lst[k])
	print(lst1[k])
for j in range(len(div1)):
	a=div1[j].find('img')
	jpg_title=lst[j]
	f = open('{0}.jpg'.format(jpg_title.replace(':','')),'wb')
	f.write(requests.get(a['src']).content)
	f.close()


