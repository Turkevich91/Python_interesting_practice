from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Project, Release, Panel


def index(request):
    project_numbers_list = Project.objects.order_by('project_number')
    # quantity_of_releases = Release.project.get_foreign_related_value(project_numbers_list)
    return render(request, 'list.html', {'project_list': project_numbers_list})


# def releas(request, project_number):
#     try:
#         a = Project.objects.get(project_number=project_number)
#     except:
#         raise Http404('Page not found')
#
#     return render(request, 'app/detail.html', {''})
