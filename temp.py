from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from nltk import word_tokenize
import os

my_url = "https://www.systutorials.com/docs/linux/man/"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

container = page_soup.findAll("a")
#print(len(container))
os.chdir('C:\\Users\\mkany\\Desktop\\project code\\man')
#directory = 'man'

for i in range(7,len(container) - 3):
    string1 = str(container[i])
    l1_url = "https:" + string1.split("\"")[1] #all the links in this page
    
    #print(l1_url)
    
    uC1 = uReq(l1_url)
    page_html = uC1.read()
    uC1.close()
    page_soup = soup(page_html, "html.parser")
    container1 = page_soup.findAll("a")
    print(len(container1))           #len -4, loop goes from range 5
    for j in range(5, len(container1) - 3):
        string2 = str(container1[j])
        l2_url = "https:" + string2.split("\"")[1] #all the links in this page
        uC2 = uReq(l2_url)
        page_html = uC2.read()
        uC2.close()
        page_soup = soup(page_html, "html.parser")
        container2 = page_soup.findAll("a")
        print(container2[5])           #len -4, loop goes from range 5
        for k in range(5, len(container2) - 3):
            string3 = str(container2[k])
            l3_url = "https:" + string3.split("\"")[1] #all the links in this page
            
            try:
                filename = l3_url.split('/')[-2]
                file = open(filename, 'wb')
                print(filename)
                uC3 = uReq(l3_url)
                page_html = uC3.read()
                uC3.close()
                page_soup = soup(page_html, "html.parser")
                container3 = page_soup.findAll("div",{"class":"main-content"})
                tempstring = word_tokenize(container3[0].text)
                string = ""
                flag = 0
                for w in tempstring:
                    if(w == "DESCRIPTION"):
                        flag = 1
                        continue
                    if(w == "COPYRIGHT"):
                        break
                    if(flag == 1):
                        string = string+" "+w
                
                
                file.write(string.encode('utf-8'))
                file.close()
                print(i)
            except:
                continue
            
    
    #5-18
#print(container[18]["href"])