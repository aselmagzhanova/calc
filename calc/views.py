from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from calc.models import Graph
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
#from forms import CommentForm
#from django.core.context_processors import csrf
#from django.core.paginator import Paginator
from django.contrib import auth
# Create your views here.

def get_user_model_fk_ref():
    if django.VERSION[:2] >= (1, 5):
        return settings.AUTH_USER_MODEL
    else:
        return 'auth.User'

def template_three_simple(request):
    view = "template_three"
    return render_to_response('myview.html', {'name': view})

'''	
def graphs(request):
    return render_to_response('graphs.html')
'''
def graphs(request):
    return render_to_response('graphs.html', {'graphs': Graph.objects.all(), 'username': auth.get_user(request).username})
	
	
	