import requests
import json
from bs4 import BeautifulSoup

url="https://in.bookmyshow.com/explore/movies-coimbatore?languages=tamil"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
j=0
tamilmovies=[]
for i in range(13,18):
    tmovies=div_tags_text[i].split('U')
    tamilmovies.append(tmovies[0])

url="https://in.bookmyshow.com/explore/movies-coimbatore?languages=english"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
j=0
englishmovies=[]
for i in range(13,16):
    emovies=div_tags_text[i].split('U')
    englishmovies.append(emovies[0])
    
url="https://in.bookmyshow.com/explore/movies-coimbatore?languages=hindi"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
j=0
hindimovies=[]
for i in range(13,14):
    hmovies=div_tags_text[i].split('U')
    hindimovies.append(hmovies[0])

url="https://in.bookmyshow.com/explore/movies-coimbatore?languages=telugu"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
j=0
telugumovies=[]
for i in range(13,15):
    tlmovies=div_tags_text[i].split('U')
    telugumovies.append(tlmovies[0])
    

languages=['Tamil','English','Hindi','Telugu']
moviesDict={}
moviesDict[languages[0]]=tamilmovies
moviesDict[languages[1]]=englishmovies
moviesDict[languages[2]]=hindimovies
moviesDict[languages[3]]=telugumovies
with open('movies.json','w') as file:
    json.dump(moviesDict,file)
    

url="https://in.bookmyshow.com/buytickets/vikram-coimbatore/movie-coim-ET00138591-MT/20220613"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
vikram=div_tags_text[1738:1759]
time=[]
theatres=[]
for i in vikram:
    if(i.startswith('0') or i.startswith('1')):
        time.append(i)
    else:
        theatres.append(i)
vikram={}
vikram[theatres[0]]=time[0:4]
vikram[theatres[1]]=time[4:8]
vikram[theatres[2]]=time[8:16]
vikram[theatres[3]]=time[16:]
with open('vikram.json','w') as file:
    json.dump(vikram,file)
    
url="https://in.bookmyshow.com/buytickets/jurassic-world-dominion-coimbatore/movie-coim-ET00328195-MT/20220611"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
jurassic=div_tags_text[1741:1749]    
time=[]
theatres=[]
for i in jurassic:
    if(i.startswith('0') or i.startswith('1')):
        time.append(i)
    else:
        theatres.append(i)
jurassic={}
jurassic[theatres[0]]=time[0:2]
jurassic[theatres[1]]=time[2:4]
jurassic[theatres[2]]=time[4:5]
with open('jurassic.json','w') as file:
    json.dump(jurassic,file)
    
url="https://in.bookmyshow.com/buytickets/777-charlie-coimbatore/movie-coim-ET00135205-MT/20220611"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
charlie=div_tags_text[1731:1742]
time=[]
theatres=[]
for i in charlie:
    if(i.startswith('0') or i.startswith('1')):
        time.append(i)
    else:
        theatres.append(i)
charlie={}
charlie[theatres[0]]=time[0:1]
charlie[theatres[1]]=time[1:3]
charlie[theatres[3]]=time[4:]
with open('charlie.json','w') as file:
    json.dump(charlie,file)
    

url="https://in.bookmyshow.com/buytickets/don-2022-coimbatore/movie-coim-ET00321832-MT/20220612"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
don=div_tags_text[1737:1750]
time=[]
theatres=[]
for i in don:
    if(i.startswith('0') or i.startswith('1')):
        time.append(i)
    else:
        theatres.append(i)
don={}
don[theatres[0]]=time[0:1]
don[theatres[1]]=time[1:3]
don[theatres[2]]=time[3:4]
don[theatres[4]]=time[6:]
with open('don.json','w') as file:
    json.dump(don,file)


url="https://in.bookmyshow.com/buytickets/adade-sundara-coimbatore/movie-coim-ET00330042-MT/20220612"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
ad=div_tags_text[1737:1746]
time=[]
theatres=[]
for i in ad:
    if(i.startswith('0') or i.startswith('1')):
        time.append(i)
    else:
        theatres.append(i)
ad={}
ad[theatres[0]]=time[0:1]
ad[theatres[1]]=time[1:2]
ad[theatres[3]]=time[3:]
with open('adade.json','w') as file:
    json.dump(ad,file)
    

url="https://in.bookmyshow.com/buytickets/jurassic-world-dominion-coimbatore/movie-coim-ET00328099-MT/20220612"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
ejurassic=div_tags_text[1741:1753]
time=[]
theatres=[]
for i in ejurassic:
    if(i.startswith('0') or i.startswith('1')):
        time.append(i)
    else:
        theatres.append(i)
ejurassic={}
ejurassic[theatres[0]]=time[0:3]
ejurassic[theatres[1]]=time[3:8]
ejurassic[theatres[2]]=time[8:]
with open('ejurassic.json','w') as file:
    json.dump(ejurassic,file)


url="https://in.bookmyshow.com/buytickets/top-gun-maverick-bengaluru/movie-bang-ET00076943-MT/20220612"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
topgun=div_tags_text[1734:1745]
time=[]
theatres=[]
for i in topgun:
    if(i.startswith('0') or i.startswith('1')):
        time.append(i)
    else:
        theatres.append(i)
topgun={}
topgun[theatres[0]]=time[0:1]
topgun[theatres[1]]=time[1:3]
topgun[theatres[2]]=time[3:4]
topgun[theatres[3]]=time[4:5]
topgun[theatres[4]]=time[5:]

with open('topgun.json','w') as file:
    json.dump(topgun,file)
    

url="https://in.bookmyshow.com/buytickets/doctor-strange-in-the-multiverse-of-madness-bengaluru/movie-bang-ET00326386-MT/20220612"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
dr=div_tags_text[1734:1745]
time=[]
theatres=[]
for i in dr:
    if(i.startswith('0') or i.startswith('1')):
        a=i.split('\t')
        time.append(a[0])
    else:
        theatres.append(i)
dr={}
dr[theatres[0]]=time[0:2]
dr[theatres[1]]=time[2:3]
dr[theatres[2]]=time[3:4]
dr[theatres[3]]=time[4:]
with open('dr.json','w') as file:
    json.dump(dr,file)
    
url="https://in.bookmyshow.com/buytickets/samrat-prithviraj-bengaluru/movie-bang-ET00081064-MT/20220612"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
samrat=div_tags_text[1734:1744]
time=[]
theatres=[]
for i in samrat:
    if(i.startswith('0') or i.startswith('1')):
        time.append(i)
    else:
        theatres.append(i)
samrat={}
samrat[theatres[0]]=time[0:2]
samrat[theatres[1]]=time[2:4]
samrat[theatres[2]]=time[4:5]
samrat[theatres[3]]=time[5:]
with open('samrat.json','w') as file:
    json.dump(samrat,file)

url="https://in.bookmyshow.com/buytickets/janhit-mein-jaari-bengaluru/movie-bang-ET00327101-MT/20220612"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
janhit=div_tags_text[1734:1744]
time=[]
theatres=[]
for i in janhit:
    if(i.startswith('0') or i.startswith('1')):
        time.append(i)
    else:
        theatres.append(i)
janhit={}
janhit[theatres[0]]=time[0:2]
janhit[theatres[1]]=time[2:4]
janhit[theatres[2]]=time[4:5]
janhit[theatres[3]]=time[5:]
with open('janhit.json','w') as file:
    json.dump(janhit,file)
    
url="https://in.bookmyshow.com/buytickets/ante-sundaraniki-bengaluru/movie-bang-ET00323425-MT/20220613"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
ante=div_tags_text[1738:1751]
time=[]
theatres=[]
for i in ante:
    if(i.startswith('0') or i.startswith('1')):
        time.append(i)
    else:
        theatres.append(i)
ante={}
ante[theatres[0]]=time[0:2]
ante[theatres[1]]=time[2:5]
ante[theatres[2]]=time[5:]
with open('ante.json','w') as file:
    json.dump(ante,file)
    
url="https://in.bookmyshow.com/buytickets/major-bengaluru/movie-bang-ET00097589-MT/20220612"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")
headline=soup.find('a').get_text()
div_tags=soup.find_all('a')
div_tags_text=[tag.get_text().strip() for tag in div_tags]
major=div_tags_text[1738:1750]
time=[]
theatres=[]
for i in major:
    if(i.startswith('0') or i.startswith('1')):
        time.append(i)
    else:
        theatres.append(i)
major={}
major[theatres[0]]=time[0:2]
major[theatres[1]]=time[2:4]
major[theatres[2]]=time[4:6]
major[theatres[3]]=time[6:]
with open('major.json','w') as file:
    json.dump(major,file)

