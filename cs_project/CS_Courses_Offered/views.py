from django.shortcuts import *
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from django.template import RequestContext
from django.core import serializers

import json

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the CS page index.")

def graph_data(request):
	# get all data from offering model
	# class_offered = Offering.objects.raw("SELECT * from Semester")
	class_offered = Offering.objects.all()
	class_offered1 = Offering.objects.filter(course_type = 'Lecture')
	semester_offered = Semester.objects.order_by('id')
	total_classes = Offering.objects.filter(course_type = 'Lecture')



	# results = Semester.objects.include(field1__in=inner_qs)
	# create a dictionary of allthe data in class_offered

	offered = {
		"semester_classes" : class_offered,
		"semester_classes1" : class_offered1,
		"semesters": semester_offered,
		"classes_type": total_classes
	}
	# print(semester_offered)
	# return JsonResponse(context_instance=RequestContext(request), 'graph/graphs.html', data, safe=False)
	# return render_to_response('graph/graphs.html', semsters, context_instance=RequestContext(request))
	return render_to_response('graph/graphs.html', offered, context_instance=RequestContext(request))
	
#this where I will tell what will be displayed. check out https://docs.djangoproject.com/en/1.8/intro/tutorial03/
#view loads the data using ORM and calls templates





# You might consider switching to Class Based Views -- more stable code reuse. Example:

# from django.views.generic import TemplateView

# class GraphDataView(TemplateView):
# 	template_name = 'graph/graphs.html'
	
# 	def get_context_data(self, **kwargs):
#         context = super(GraphDataView, self).get_context_data(**kwargs)
    
# 		# get all data from offering model
# 		class_offered = Offering.objects.all()
# 		# create a dictionary of allthe data in class_offered
# 		data = serializers.serialize("json", class_offered)
	
# 		context['semester_classes'] = data
#     	# Now you can access semester_classes in template
#         return context



