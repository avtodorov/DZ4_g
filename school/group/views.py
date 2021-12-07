from django.shortcuts import render

from group.models import Group
from django.http import HttpResponse, JsonResponse


# Create your views here.

# path('groups/', group_views.get_groups),
def get_groups(request):
    groups = [
        {
            'group_name': group.group_name,
            'group_theme': group.group_theme,
            'teacher': group.teacher

        }
        for group in Group.objects.all()
    ]

    data = {
        'count': Group.objects.count(),
        'groups': groups,
    }

    return JsonResponse(data)
