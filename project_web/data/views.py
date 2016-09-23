from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from models import InputForm
from compute import compute
from compute import showdata
from compute import getline
import os
import json
from django.core.cache import cache

def index(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
           # result = compute(form2.A, form2.b, form2.w, form2.T)
           # result = result.replace('static/', '')
	    result = getline(form2.StartDate,form2.StartTime,form2.EndDate,form2.EndTime)
	    result = result.replace('static/','')
	 #   showdata(1.1,2.2,3.3)
         #   List = ['aaaa', 'bbbb']
	    List = [showdata()]
    else:
        form = InputForm()
	List = """Memory Usage  <table border=1>    <tr><td> max     </td><td>0 GB</td></tr>    <tr><td> min     </td><td>0 GB</td></tr>    <tr><td> mean     </td><td>0 GB</td></tr>  """
    return render_to_response('data.html',
            {'form': form,
             'result': result,
	     'List': json.dumps(List),
             }, context_instance=RequestContext(request))





