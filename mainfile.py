import urllib2
from bs4 import BeautifulSoup

def getRepository(UserName):
    url= urllib2.urlopen("https://github.com/"+UserName+"?tab=repositories")
    soup=BeautifulSoup(url,'html.parser')
    total_repositories=soup.find('span',attrs={'class':'Counter'})
    repositories= total_repositories.text.strip()
    print "Total Number of Repositories : "+repositories

def getName(UserName):
    html_page = urllib2.urlopen("https://github.com/" + UserName)  # Getting the html of the url specified.
    soup = BeautifulSoup(html_page,'html.parser')
    user_name = soup.find('span', attrs={'class': 'p-name vcard-fullname d-block'})
    name = user_name.text.strip()
    print "The Account Holders Username is "+name

def getDesc(UserName):
    html_page = urllib2.urlopen("https://github.com/" + UserName)
    soup = BeautifulSoup(html_page, 'html.parser')
    user_desc = soup.find('div', attrs={'class': 'p-note user-profile-bio'})
    description = user_desc.text.strip()
    print "The User's bio is "+description

def getStars(UserName):
    html_page=urllib2.urlopen("https://github.com/"+UserName+"?tab=stars")
    soup=BeautifulSoup(html_page,'html.parser')
    user_stars=soup.find('a',attrs={'class':'UnderlineNav-item selected'})
    total_stars=user_stars.text.strip()
    total_stars_test= total_stars.split()
    total_stars_test="".join(total_stars_test).split("Stars")
    print "The user has: "+"".join(total_stars_test) + " Stars"

def getUserLocation():
    html_page=urllib2.urlopen("https://github.com/"+UserName)
    soup=BeautifulSoup(html_page,'html.parser')
    location_find=soup.find('span',attrs={'class','p-label'})
    location= location_find.text.strip()
    print "The User's current location is:"+location

UserName= raw_input("Please enter the Github Username: ")
getName(UserName)
try:
    getDesc(UserName)
except:
    print "The User has not set Description! "

getRepository(UserName)
getStars(UserName)
getUserLocation()