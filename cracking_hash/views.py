'''
Created on Jan 28, 2014

@author: itox
'''
from django.shortcuts import render_to_response
#import re
from time import time
from django.template import RequestContext
#from django.http import HttpResponseRedirect, HttpResponse
#import settings
from crack import process

def crack_hashlib(request):
        
    if request.method == "POST":
        start_time = time()
        
        input_hash = request.POST['input_hash']
        input_length = request.POST['input_length']
        length_char = int(input_length)
        hashall = process(input_hash, length_char)
        waktunya = time() - start_time
       # waktu = re.match(r'^(\w{10}).(\w{3})$', waktunya)
        print waktunya
        print hashall
    else:
        hashall= []
        waktunya = []
        
    return render_to_response('crack_hash.html', 
                              {'hashall': hashall, 'waktu': waktunya,}, context_instance=RequestContext(request)
    )


