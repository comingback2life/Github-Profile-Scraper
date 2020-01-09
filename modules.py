#Module containing all the functions required to fetch a user's details from Github
import urllib
from urllib import *
from bs4 import BeautifulSoup


def connection_init(userName):
    global url, soup
    url= urllib.request.urlopen("https://github.com/"+userName)
    newrl=url.read()
    soup=BeautifulSoup(newrl,'html.parser')

def getRepository(userName):
    total_repositories=soup.find('span',attrs={'class':'Counter hide-lg hide-md hide-sm'})
    repositories= total_repositories.text.strip()
    print ("Total Number of Repositories : "+repositories)
def getName(UserName):
    user_name = soup.find('span', attrs={'class': 'p-name vcard-fullname d-block overflow-hidden'})
    name = user_name.text.strip()
    print ("The Account Holders Username is "+name)

def getDesc(UserName):
    user_desc = soup.find('div', attrs={'class': 'p-note user-profile-bio js-user-profile-bio'})
    description = user_desc.text.strip()
    print ("The User's bio is "+description)

def getStars(UserName):
    user_stars=soup.find('a',attrs={'class':'UnderlineNav-item mr-0 mr-md-1 mr-lg-3 selected '})
    total_stars=user_stars.text.strip()
    total_stars_test= total_stars.split()
    total_stars_test="".join(total_stars_test).split("Stars")
    total_stars_test="".join(total_stars_test).split("Repositories")
    total_stars_test="".join(total_stars_test).split("Overview")
    print ("The user has: "+"".join(total_stars_test) + " Stars")

def getUserLocation(UserName):
    location_find=soup.find('span',attrs={'class','p-label'})
    location= location_find.text.strip()
    print ("The User's current location is: "+location)