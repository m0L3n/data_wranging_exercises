import csv
#Description: Parsing a fixed width file into a csv file.
#Source file:
    # https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt
    # the metadata for the file can be found here:
    # https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt

filename = "ghcnd-stations"

#store the source file:
source_file = open("data\\"+filename+".txt")
#create a list of lines with .readlines()
source_list = source_file.readlines()
#create an output .csv file
output_file = open(filename+"_parsed.csv",'w')
#create a csv writer object
writer = csv.writer(output_file, delimiter='\t')
#creat a header list
header = ["ID","LATITUDE","LONGITUDE","ELEVATION","STATE","NAME","GSN_FLAG","HCNCRN_FLAG","WMO_ID"]
#add header to output file
writer.writerow(header)

#loop throught each line
for line in source_list:
    #creat an empty list, to which we append the rows
    new_row=[]
    # ID: positions 1-11
    new_row.append(line[0:11])
    # LATITUDE: positions 13-20
    new_row.append(line[12:20])
    # LONGITUDE: positions 22-30
    new_row.append(line[21:30])
    # ELEVATION: positions 32-37
    new_row.append(line[31:37])
    # STATE: positions 39-40
    new_row.append(line[38:40])
    # NAME: positions 42-71
    new_row.append(line[41:71])
    # GSN_FLAG: positions 73-75
    new_row.append(line[72:75])
    # HCNCRN_FLAG: positions 77-79
    new_row.append(line[76:79])
    # WMO_ID: positions 81-85
    new_row.append(line[80:85])
    writer.writerow(new_row)

#close csv
output_file.close()