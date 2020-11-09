# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page

from .models import Project, Release, Panel, Task


# import io
# from reportlab.pdfgen import canvas


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
    active_tasks = Project.objects.filter(release__task__status="In progress")
    # print(len(Release.objects.filter(project__id=1)))  # Works!
    return render(request, 'production.html', {'active_projects': set(active_tasks)})


@gzip_page
def project_view(request, project_number):
    project = Project.objects.filter(project_number=project_number, release__task__status="In progress")
    releases = Release.objects.filter(project__project_number=project_number, task__status="In progress")
    return render(request, 'project_view.html', {'releases': releases, 'project': project[0]})


@gzip_page
def release_view(request, project_number, release_title):
    try:
        release = Release.objects.get(release_title=release_title, project__project_number=project_number)
    except:
        raise Http404('VIEWS PROBLEM')
    return render(request, 'release_view.html', {'release': release})


@gzip_page
def panel_info(request, project_number, release_title, panel_title):
    try:
        panel = Panel.objects.get(
            release__project__project_number=project_number,
            release__release_title=release_title,
            panel_title=panel_title
        )
    except:
        raise Http404('VIEWS PROBLEM')
    return render(request, 'panel.html', {'panel': panel})


# @login_required()
def management(request):
    tasks = Task.objects.order_by('rel_date')
    heads = [
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
    return render(request, 'management.html', {'tasks': tasks, 'heads': heads})


# def pdf_view(request):
#     return render(request, 'pdf.html', {'pdf_name': 'PAP 15.pdf'})
# def engineering(request):
#     return render(request, 'engineering.html', )


# https://docs.djangoproject.com/en/3.0/howto/outputting-pdf/
# def pdf_view(request):
#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer)
#     p.drawString(0, 100, "Hello world.")
#     p.showPage()
#     p.save()
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='Hello.pdf')
# def pdf_view(request):
#     with open('static/pdf/PAP 15.pdf', 'r') as pdf:
#         response = HttpResponse(pdf.read(), mimetype='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=some_file.pdf'
#         return response
#     pdf.closed
