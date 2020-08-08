from django.shortcuts import render
from django.http import HttpResponse


def base(request):
    return render(request, 'kit/base.html')
def about(request):
    content = {
        'about': True,
        'experience': False,
        'project': False
    }
    return render(request, 'kit/information.html', content)