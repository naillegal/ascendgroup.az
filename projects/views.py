from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project
from django.core.exceptions import ObjectDoesNotExist

def projects(request):
    try:
        projects_list = Project.objects.all()
    except ObjectDoesNotExist:
        projects_list = []

    paginator = Paginator(projects_list, 4)

    page_number = request.GET.get('page')
    try:
        projects = paginator.page(page_number)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, pk, slug):
    project = get_object_or_404(Project, pk=pk, slug=slug)
    return render(request, 'project-detail.html', {'project': project})
