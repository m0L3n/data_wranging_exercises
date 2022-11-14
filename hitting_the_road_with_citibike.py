import csv

source_csv = open("C:\\Users\\lenzm\\Documents\\repository\\data_wranging_exercises\\data\\202009-citibike-tripdata.csv","r")

citibike = csv.DictReader(source_csv)
print(f"Names of the {len(citibike.fieldnames)} columns are: \n{citibike.fieldnames}")
