import csv

source_csv = open("C:\\Users\\lenzm\\Documents\\repository\\data_wranging_exercises\\data\\202009-citibike-tripdata.csv","r")

citibike = csv.DictReader(source_csv)
print(f"Names of the {len(citibike.fieldnames)} columns are: \n{citibike.fieldnames}")

# create a variable to hold the count of each type of Citi Bike user
# assign or "initialize" each with a value of zero (0)
count_subscriber = 0
count_customer = 0
count_other_user = 0

# loop through every row
for i in citibike:
    if i["usertype"] == "Subscriber":
        count_subscriber +=1
    elif i["usertype"] == "Customer":
        count_customer +=1
    else:
        count_other_user +=1
#print numbers of subscriber, customer and others
print(f"Number of Subscribers are: {count_subscriber}\nNumber of Customers are: {count_customer}\nNumber of other User are: {count_other_user}")
    #Output: There are 0 Other Users, therefore we can confirm, that our dataset only contains customer and subscriber

#show unique values of column "usertype"
values_usertypes = []
for row in citibike:
    if row["usertype"] in values_usertypes:
        print(1)
        values_usertypes.append(row["usertype"])
        values_usertypes.__add__(row["usertype"])
        print(row["usertype"])