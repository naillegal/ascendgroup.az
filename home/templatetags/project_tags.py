from django import template
from projects.models import Project

register = template.Library()

@register.simple_tag
def get_projects():
    return Project.objects.all()