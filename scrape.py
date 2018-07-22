import webbrowser, requests, re, urllib
from bs4 import BeautifulSoup

print('Input a google images url to grab the top 20 images.')
url = input()
url = re.search(r"(\bhttps\S+=)\b", url).group()

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

searchTerm = soup.find_all('input')
searchTerm = image = re.search(r"\bvalue=\"(.*?)\"", str(searchTerm[0])).group(1)

imgs = soup.find_all('img')

i=0
for x in imgs:
    image = re.search(r"\bsrc=\"(\S+)\b", str(imgs[i])).group(1)
    print(image)
    f = open(searchTerm+str(i)+'.jpg','wb')
    f.write(requests.get(image).content)
    f.close()
    i += 1
