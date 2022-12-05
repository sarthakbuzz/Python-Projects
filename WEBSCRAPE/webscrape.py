from bs4 import BeautifulSoup
import requests

url="https://www.mayfairhotels.com/mayfair-lagoon.php"

response=requests.get(url)
htmlcontent=response.content

#print(response.content)
soup=BeautifulSoup(htmlcontent,"html.parser")
#print(soup.title)
#print(soup.title.string)
#print(soup.p)
#print(soup.a)
#for link in soup.find_all("a"):
    #print(link.get("href"))
    