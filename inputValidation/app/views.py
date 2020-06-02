from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Project, Release, Panel


def index(request):
    project_number = Project.objects.order_by('project_number')
    return render(request, 'list.html', {'Projects': project_number})


# def projects(request, project_number):
#     try:
#         a = Project.objects.get(project_number=project_number)
#     except:
#         raise Http404('Page not found')
#
#     return render(request, 'app/detail.html', {''})
