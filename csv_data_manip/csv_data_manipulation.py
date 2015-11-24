print ("helo")
import csv

#open the file to be read
def getcourse():
    with open("CS_Actual_Enrollments.csv", "r") as data_open:
    #read the file using csv reader module.
    data_open_csv = csv.reader(data_open)
    #skip the first row of the CSV file.
    next(data_open_csv)
    course_class = [[row[3], eval(row[4]), row[6], row[7]]for row in data_open_csv]
    for raw in data_open_csv:
        _, created = Course.objects.get_or_create(
            course_title = row[3],
            course_number = eval(row[4]),
            subject = row[6],
            course_type = row[7]
            )
#print (semester_class)


with open("CS_Actual_Enrollments.csv", "r") as data_open:
    
    #read the file using csv reader module.
    data_open_csv=csv.reader(data_open)
    
    #skip the first row of the CSV file.
    next(data_open_csv)
    
    semester_class = [[ eval(row[0]), row[1]]for row in data_open_csv]
    for raw in data_open_csv:
        _, created = Course.objects.get_or_create(
            term_code = eval(row[0]),
            term_description = row[1]
            )
#print semester_class


with open("CS_Actual_Enrollments.csv", "r") as data_open:
    
    #read the file using csv reader module.
    data_open_csv=csv.reader(data_open)
    
    #skip the first row of the CSV file.
    next(data_open_csv)
    
    Offering_class = [[eval(row[2]), row[5], eval(row[8])]for row in data_open_csv]
    for raw in data_open_csv:
        _, created = Course.objects.get_or_create(
            crn_number = eval(row[2]),
            section_number = row[5],
            max_enrollment = eval(row[8])
            )
#print Offering_class

data_open.close()

##writing a file to our directory
##Class csv2
# out = open("course_class.csv", "wb")
# output=csv.writer(out)
#
# for row in course_class:
#     output.writerow(row)
#
## #semester csv
# out = open("semester_class.csv", "wb")
# output=csv.writer(out)
#
# for row in semester_class:
#     output.writerow(row)
#
## #offering csv
# out = open("Offering_class.csv", "wb")
# output=csv.writer(out)
#
# for row in semester_class:
#     output.writerow(row)
#
# out.close()