#Python code to illustrate parsing of XML files 
# importing the required modules 
# import csv
# import requests
import xml.etree.ElementTree as ET 
import schedule
import time
import pandas as pd

url_current = '../data/Trace_current.xml'
tree = ET.parse(url_current)
root = tree.getroot()
##### test #####
element = root.findall(".//")
#print("Elements of .//")
#print(element)
print('Test start')
for element in root.findall(".//"):
    print("Next Element")
    print(element.tag, element.text)
##### test end#####

# Create a list to store dictionaries representing each position info
Samples_list = []
# Iterate through each <WorkOffsetk> element
print('start running')
#print(root.findall(".//Samples"))
## ./Streams/DeviceStream/ComponentStream/Samples
for Samples_elem in root.findall('.//'):
    Samples_dict = {}
    
    for child_elem in Samples_elem:
        Samples_dict[child_elem.tag] = child_elem.text
    Samples_list.append(Samples_dict)

df_Samples = pd.DataFrame(Samples_list)
print("resulting Samples:")
#print(df_Samples)
#def job():
#    #response = requests.get(url)
#    xml_data = url #response.text

#    tree = ET.ElementTree(ET.fromstring(xml_data))
#    root = tree.getroot()

    # Now you can process or extract data from the XML using 'root' variable.

# Schedule the job to run every minute
#schedule.every(1).minutes.do(job)

#while True:
#    schedule.run_pending()
#    time.sleep(1)