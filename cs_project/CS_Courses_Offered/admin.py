from django.contrib import admin
from .models import Course, Semester, Offering
# Register your models here.

class OfferingInline(admin.TabularInline):
    model = Offering
    extra = 6

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [('Course Number', {'fields': ['course_number'], 'classes': ['collapse']}), ('Course Title', {'fields': ['course_title']}), ('Subject', {'fields': ['subject'], 'classes': ['collapse']}), ]
    # inlines = [OfferingInline]
    list_display = ('course_number', 'course_title', 'subject', )

class SemesterAdmin(admin.ModelAdmin):
    fieldsets = [('Term Code', {'fields': ['term_code'], 'classes': ['collapse']}), ('Term Description', {'fields': ['term_description'], 'classes': ['collapse']}), ]
    # inlines = [OfferingInline]
    list_display = ('term_code', 'term_description', )

    

search_fields = ['course_number', 'course_title']
admin.site.register(Course, CourseAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Offering)
