from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Project, Release, Panel


def index(request):
    return render(request, 'index.html')


def production(request):
    project_numbers_list = Project.objects.order_by('project_number')
    # quantity_of_releases = Release.project.get_foreign_related_value(project_numbers_list)
    return render(request, 'production.html', {'project_list': project_numbers_list})


def projects(request, project_num):
    work_number = Project.objects.get(project_num)
    # quantity_of_releases = Release.project.get_foreign_related_value(project_numbers_list)
    return render(request, 'projects.html', work_number)


def management(request):

    return render(request, 'management.html')


def engineering(request):
    return render(request, 'engineering.html', )


def releases(request, rel_title):
    try:
        a = Release.objects.get(rel_titlerelease_title=rel_title)
    except:
        raise Http404('Page not found')

    return render(request, 'releases.html',)

