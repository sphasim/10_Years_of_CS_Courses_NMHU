from django.db import models
# Create your models here.
class Course(models.Model):
    course_number = models.PositiveIntegerField(unique = True)
    course_title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    def __str__(self):
        return self.course_title

class Semester(models.Model):
    term_code = models.PositiveIntegerField(unique = True)
    term_description = models.CharField(max_length = 255)
    def __str__(self):
        return self.term_description

class Offering(models.Model):
    a_course = models.ForeignKey(Course)
    a_semester = models.ForeignKey(Semester)
    crn_number = models.PositiveIntegerField()
    course_type = models.CharField(max_length=255)
    section_number = models.PositiveIntegerField()
    max_enrollment = models.PositiveIntegerField()
    act_enrollment = models.PositiveIntegerField()
    def __str__(self):
        return self.a_course.course_title


#have a folder with all the methods/function I need to intereact with models. put them in an app. import the methods from the app in models.py so that they add the data. Call them in models.py