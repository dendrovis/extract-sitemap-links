import xml.etree.ElementTree as ElementTree
import re as RegularExpression
import sys
import json
import time
import os

def getXMLNS(rootValue):
    xmlns = RegularExpression.search('{.*}', rootValue)
    xmlns = xmlns[0] if xmlns else ''
    return xmlns

def getLinks(xmlFile): 
    tree = ElementTree.parse(xmlFile)
    root = tree.getroot() 
    xmlns = getXMLNS(root.tag)
    links = [elem.text for elem in root.iter(f'{xmlns}loc')]
    return links 

def checkArgs():
    if len(sys.argv) != 2:
        print("Please provide 1 argument only, which is your xml file path. Example: python readSitemap.py ./samples/source.xml")
        sys.exit(1)

def checkLinks(links):
    if len(links) < 1:
        print("No link found, please try again")
        sys.exit(1) 

def checkOutputFolder():
    folder_path = 'output'
    if os.path.exists(folder_path):
        print(f"folder '{folder_path}' already exists.")
    else:
        os.mkdir(folder_path)
        print(f"folder '{folder_path}' created.")
        

def main():
    checkArgs()
    path = sys.argv[1]
    links = getLinks(path)
    checkLinks(links)
    checkOutputFolder()    
    timestamp = time.time_ns() 
    jsonData = {"links": links}
    with open(f'output/{timestamp}.json', 'w') as f:
        json.dump(jsonData, f)
        print('done')


if __name__ == "__main__": 
    main() 