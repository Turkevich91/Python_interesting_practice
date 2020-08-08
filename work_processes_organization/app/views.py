from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Project, Release, Panel, Task


# from ..common.modules import ExcelHandler


@gzip_page
def home_view(request):
    return render(request, 'home.html')


@gzip_page
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user = authenticate(request, username=username, password=password)
        print(f'{user} is logging in')
        print('password: ', password)
        if user is not None:
            login(request, user)
            print('Successfully logged in')
            return HttpResponseRedirect('/')
    return render(request, 'login.html')


def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@gzip_page
# @login_required
def production(request):
    projects = Project.objects.order_by('id')
    # print(len(Release.objects.filter(project__id=1)))  # Works!
    return render(request, 'production.html',
                  {'projects': projects})


@gzip_page
def projects(request, project_number):
    try:
        a = Project.objects.get(project_number=project_number)
    except:
        raise Http404("Page not found")
    return render(request, 'projects.html', {'project': a})


@gzip_page
def releases(request, project_number, release_title):
    # releases =
    try:
        # a = Release.objects.filter(project__project_number=project_number, release_title=release_title)
        a = Release.objects.get(release_title=release_title, project__project_number=project_number)
        # print(a[0])
    except:
        raise Http404('VIEWS PROBLEM')
    return render(request, 'releases.html', {'release': a})


@gzip_page
def panels(request, project_number, release_title, panel_title):
    try:
        a = Panel.objects.get(
            release__project__project_number=project_number,
            release__release_title=release_title,
            panel_title=panel_title
        )
    except:
        raise Http404('VIEWS PROBLEM')
    return render(request, 'panels.html', {'panels': a})


# @login_required()
def management(request):
    tasks = Task.objects.order_by('rel_date')
    theads = [
        'Name',
        'Release',
        'PM',
        'loose items',
        'Outsource Paint',
        'Pt Dwgs',
        'Zee Hats Angles',
        'Flashing',
        'Coping',
        'Splice Plate',
        'Blade Screen',
        'Perf',
        'Plate Panels',
        'Frames',
        'Strapping',
        'Clips',
        'Misc.',
        'Est. MH',
        'Rel-Date',
        'Requested Ship Date',
        'Shipped Date',
        'Date dif',
        'Status',
        'Shipped to Location',
        'REMARKS',
    ]
    return render(request, 'management.html', {'tasks': tasks, 'theads': theads})

# def engineering(request):
#     return render(request, 'engineering.html', )
