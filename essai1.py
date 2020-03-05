import xml.etree.cElementTree as ET
import csv


root = ET.Element("sudents")
child = ET.Element("student")



##################################################
nameLastName=[]
S1 = []
S2 = []
credit  =[]
result =[]
moyenne = []


csvFile =open("C:\\Users\\Mon pc\\Desktop\\cours\javascript\\tp2rapport\\test1.csv","r")
csvReader = csv.reader(csvFile)
next(csvReader)
for element in csvReader:
    nameLastName.append(element[0])
    S1.append(element[1])
    S2.append(element[2])
    credit.append(element[3])
    result.append(element[4])
####################################################
#function to calculate
cptFS2=0
if len(S1)==len(S2):
    for s in S1:
        calcul=(float(s)+float(S2[cptFS2]))
        print(calcul,"",s,"",S2[cptFS2],"")
        calcul1=calcul/2
        print(calcul1)
        moyenne.append(str(calcul1))
        cptFS2=cptFS2+1


i=0
for name in nameLastName:
    
    if i <= 4:
          print(i)
          child = ET.Element("student")
          ET.SubElement(child,"nom").text=nameLastName[i]
          ET.SubElement(child,"S1").text=S1[i]
          ET.SubElement(child,"S2").text=S2[i]
          ET.SubElement(child,"credit").text=credit[i]
          ET.SubElement(child,"resultat").text=result[i]
          ET.SubElement(child,"moyenne").text=moyenne[i]
          root.append(child)


          tree =ET.ElementTree(root)
          
          print(S1[i])
          print(nameLastName[i])
          
    i=i+1
    
  
    
    














tree.write("exemple.xml",encoding='utf-8')