#Python code to illustrate parsing of XML files 
# importing the required modules 
import csv
from errno import EDEADLK 
import requests 
import xml.etree.ElementTree as ET 


def loadRSS(url_cnc_xml): 
  
    # url of rss feed 
    url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
  
    # creating HTTP response object from given url 
    resp = requests.get(url) 
  
    # saving the xml file 
    with open(url_cnc_url, 'wb') as f: 
        f.write(resp.content) 