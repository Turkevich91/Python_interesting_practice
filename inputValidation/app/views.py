from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Project, Release, Panel


@gzip_page
def index(request):
    return render(request, 'index.html')


@gzip_page
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print('username: ', username)
    print('password: ', password)
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
    return render(request, 'login.html')



@gzip_page
# @login_required
def production(request):
    project_numbers_list = Project.objects.order_by('id')
    release_quantity = Release.objects.order_by('project')
    # print(release_quantity)
    # print(len(Release.objects.filter(project__id=1)))  # Works!

    return render(request, 'production.html',
                  {'project_list': project_numbers_list,
                   'release_quantity': release_quantity})


@gzip_page
def projects(request, project_number):
    try:
        a = Project.objects.get(project_number=project_number)
        print(a)
    except:
        raise Http404("Page not found")
    # return HttpResponse(f'Project page {project_number}')
    return render(request, 'projects.html', {'project': a})


@gzip_page
def releases(request, project_number, release_title):
    # print(project_number, release_title)
    try:
        a = Release.objects.get(release_title=release_title)
    except:
        raise Http404('Right now this page in develop, please try again later')
    return render(request, 'releases.html', {'release': a})


def management(request):
    return render(request, 'management.html')


def engineering(request):
    return render(request, 'engineering.html', )
