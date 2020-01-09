import urllib
from bs4 import BeautifulSoup
from modules import *

UserName= input("Please enter the Github Username: ")
connection_init(UserName)

try:
    getName(UserName)
    getDesc(UserName)
    getRepository(UserName)
    getStars(UserName)
   
except AttributeError :
    print("There was an error fetching data from Github. Some details of the user must be missing. ")

