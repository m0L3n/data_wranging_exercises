from lxml import etree
import csv

xml_filename="U6_FRED_data"
xml_source_file = open("data\\"+xml_filename+".xml","rb")

#pass xml file to the lyml library etreee parse()
xml_doc = etree.parse(xml_source_file)
#get the root element of the document
doc_root = xml_doc.getroot()
print(etree.tostring(doc_root))

#confirm that root is a well formed XML
if etree.iselement(doc_root):
    #create csv file
    output_file = open(xml_filename+"_parsed.csv", "w")
    #create writer
    writer = csv.writer(output_file)

    #write header, using doc_root[0]
    writer.writerow(doc_root[0].attrib.keys())
    #fill doc with each value of xml source file
    for child in doc_root:
        writer.writerow(child.attrib.values())

#close csv
output_file.close()
