#Python code to illustrate parsing of XML files 
# importing the required modules 
# import csv
# import requests
import xml.etree.ElementTree as ET 
import schedule
import time
import pandas as pd
from lxml import etree

url_current = '../data/Trace_current.xml'

def remove_namespace(tree):
    for elem in tree.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]  # remove the namespace
    return tree

def xml_to_dataframe(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Remove namespaces
    root = remove_namespace(root)
    
    # Convert XML to DataFrame
    item_list = []
    for item in root.findall('.//'):
        # Extract the data you need based on your XML structure
        itam_dict = {}
    
        for child_elem in item:
            itam_dict[child_elem.tag] = child_elem.text

        item_list.append(itam_dict)
        
    df = pd.DataFrame(item_list)
    return df

# Replace 'your_xml_file.xml' with the actual path to your XML file
df = xml_to_dataframe(url_current)

# Now you have your XML data in a Pandas DataFrame
print(df)
print(df.columns)
print(df["PathPosition"].dropna())
