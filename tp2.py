import csv
import webbrowser
import xml.etree.cElementTree as ET

nameFile="student.xml"
webbrowser.open_new_tab(nameFile) 
#########################
messageXml="""

<?xml version="1.0" encoding="UTF-8"?>
    <student>
      
    </student>
"""
ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
tree = ET.ElementTree(root)
tree.write("filename.xml")

##open file 

with open("C:\\Users\\Mon pc\\Desktop\\cours\\javascript\\tp2rapport\\test1.csv","r") as csvFile:
    csvFileOpen = csv.reader(csvFile)


#####################################################
with open("student.xml","w") as xmlFile:
    xmlFile.write(messageXml)
    