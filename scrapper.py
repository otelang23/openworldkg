from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from nltk import word_tokenize
my_url = "https://www.systutorials.com/docs/linux/man/0p-arpa_inet/"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

container = page_soup.findAll("div",{"class":"main-content"})
#print(soup.prettify(container[5]))

tempstring = word_tokenize(container[0].text)
string = ""
flag = 0
for w in tempstring:
    if(w == "DESCRIPTION"):
        flag = 1
    if(w == "COPYRIGHT"):
        break
    if(flag == 1):
        string = string+" "+w
    
print(string)


#print(container[0].text)

#5-18
#print(container[18]["href"])