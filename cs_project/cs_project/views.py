from django.shortcuts import *
from django.template import RequestContext

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def contact_us(request):
	contact_data = {
		'name' : 'SP',
		'email' : 'sphasim@gmail.com',
		'website' : 'www.mathyogi.com'
	}
	print (contact_data)
	return render_to_response('contact.html', contact_data,context_instance=RequestContext(request))