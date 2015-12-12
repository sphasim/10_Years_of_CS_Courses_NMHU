from CS_Courses_Offered.models import *
import csv
print ("helo")
#open the file to be read

# from csv_data_manip.csv_data_manipulation import *
# Offering.objects.all().delete()
# Course.objects.all().delete()
# Semester.objects.all().delete()

# from csv_data_manip.csv_data_manipulation import *
# GetCourseData()
# GetSemesterData()
# GetOfferingData()

def GetCourseData():
    with open("CS_Actual_Enrollments.csv", "r") as data_open:
        #read the file using csv reader module.
        data_open_csv = csv.reader(data_open)
        #skip the first row of the CSV file.
        next(data_open_csv)
        for row in data_open_csv:
            try:
                created = Course.objects.get(
                    course_number = eval(row[4])
                    )
            except Course.DoesNotExist:
                created = Course(
                    course_number = eval(row[4]),
                    course_title = row[7],
                    subject = row[3]
                    )
                created.save()

def GetSemesterData():
    with open("CS_Actual_Enrollments.csv", "r") as data_open:
        #read the file using csv reader module.
        data_open_csv = csv.reader(data_open)
        #skip the first row of the CSV file.
        next(data_open_csv)
        for row in data_open_csv:
            _, created = Semester.objects.get_or_create(
                term_code = eval(row[0]),
                term_description = row[1]
                )

def GetOfferingData():
    with open("CS_Actual_Enrollments.csv", "r") as data_open:
        #read the file using csv reader module.
        data_open_csv = csv.reader(data_open)
        #skip the first row of the CSV file.
        next(data_open_csv)
        for row in data_open_csv:
            try:
                created = Offering.objects.get(
                    crn_number = eval(row[2])
                    )
            except Offering.DoesNotExist:
                course = Course.objects.get(
                    course_number = eval(row[4])
                    )
                semester = Semester.objects.get(
                    term_code = eval(row[0])
                    )
                created = Offering(
                    a_course = course,
                    a_semester = semester,
                    crn_number = eval(row[2]),
                    course_type = row[6],
                    section_number = row[5],
                    max_enrollment = eval(row[8]),
                    act_enrollment = eval(row[9])
                    )
                created.save()
            # _, created = Offering.objects.get_or_create(
            #     crn_number = eval(row[2]),
            #     section_number = row[5],
            #     max_enrollment = eval(row[8])
            #     )

# data_open.close()