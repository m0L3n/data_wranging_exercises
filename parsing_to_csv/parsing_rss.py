from lxml import etree
import csv

# the data used here is an instance of
# http://feeds.bbci.co.uk/news/science_and_environment/rss.xml

source_file= "BBC News - Science & Environment XML Feed"
xml_file = open("data\\"+source_file+".xml","rb")

# parse to etree
xml_doc = etree.parse(xml_file)
#root element
doc_root = xml_doc.getroot()

# doc root well formated
if etree.iselement(xml_doc):
    #create output file
    output_file = open(source_file+"_parse.csv", "w")
    #create writer for output file
    writer = csv.writer(output_file)
    #doc root[0] is channel element
    main_channel = doc_root[0]
    #example of first instance
    articel_example = main_channel.find('item')
    #empty list for column headers
    tag_list = []

    #get header names
    for child in articel_example.iterdescendants():
        #add tag to header list
        tag_list.append(child.tag)
        #if current tag has attributes:
        if child.attrib:
            # loop through attribute keys in the tag
            for attribute_name in child.attrib.keys():
                #append attribute name
                tag_list.append(attribute_name)
    #write header names in output file header
    writer.writerow(tag_list)

    #grab every Item
    for item in main_channel.findall('item'):
        #empty list
        new_row = []

        #get content of each element
        for tag in tag_list:
            #if tag name exist
            if item.findtext(tag):
                #append item to row
                new_row.append(item.findtext(tag))
            elif tag == "isPermaLink":
                #grab value for <guid> element
                new_row.append(item.find('guid').get("isPermaLink"))
        #add row
        writer.writerow(new_row)
    #close file
    output_file.close()