import json
import csv

# An example of reading data from a .json file with Python, by using the built-in "json" library.
# The data used here is an instance of :
# https://api.stlouisfed.org/fred/series/observations?series_id=U6RATE& \ file_type=json&api_key=YOUR_API_KEY_HERE

filename = "U6_FRED_data"
source_file = open("data\\"+filename+".json","r")

#pass source file to json load method
json_data = json.load(source_file)
#create output file
output_file = open("data\\"+filename+"-parsed_from_json.csv","w")
#create csv writer
writer = csv.writer(output_file)
#get header
writer.writerow(list(json_data["observations"][0].keys()))

#loop throw the rows and write the data in output file
for obj in json_data["observations"]:
    #create list for each object value
    obj_values = []
    #every 'key' is going to become a column
    for key, value in obj.items():
        #see that we have the correct values
        print(key,value)
        obj_values.append(value)
    #write the row data to output file
    writer.writerow(obj_values)
#close output file
output_file.close()



