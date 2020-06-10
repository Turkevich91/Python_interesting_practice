from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Project, Release, Panel


def index(request):
    return render(request, 'index.html')


def production(request):
    project_numbers_list = Project.objects.order_by('id', 'project_number')
    release_quantity = Release.objects.order_by('project')
    print(release_quantity)
    print(len(Release.objects.filter(project__id=1)))  # Works!

    return render(request, 'production.html',
                  {'project_list': project_numbers_list,
                   'release_quantity': release_quantity})


def projects(request, project_num):
    try:
        a = Release.objects.filter(project=project_num)
        print(a)
    except:
        raise Http404('The page wasn\'t found')
    return render(request, 'projects.html', {'project': a})


def management(request):
    return render(request, 'management.html')


def engineering(request):
    return render(request, 'engineering.html', )


def releases(request, rel_title):
    try:
        a = Release.objects.get(rel_titlerelease_title=rel_title)
    except:
        raise Http404('Page not found')

    return render(request, 'releases.html', )
