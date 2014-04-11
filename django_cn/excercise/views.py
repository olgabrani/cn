from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    return render_to_response('index.html', context)

