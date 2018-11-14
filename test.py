from bs4 import BeautifulSoup 

with open("enwiki-latest-pages-articles.xml") as fp:
        data = fp.read()

soup = BeautifulSoup(data,'html.parser')

for page in soup.find_all('page'):
        #title = page.find('title').string
        #id = page.find('id').string
        text = page.find('text').string
        f = open("demofile.txt","a")
        f.write(text)
        
       
