from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.db.models import Q

def members(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, slug):
    mymembers = Members.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers,
        'emptytestoject': [],
        'fruits': ['Apple', 'Banana', 'Cherry', 'Oranges', 'Kiwi'],
    }
    return HttpResponse(template.render(context, request))

def testing_two(request):
    mydata = Members.objects.all().order_by('firstname').values()
    template = loader.get_template('template2.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))