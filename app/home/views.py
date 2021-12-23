import logging
from django.shortcuts import render

logger = logging.getLogger('app')


def home_view(request, **kwargs):
    """
    View  /
    """
    return render(request, 'home.html')


def about_view(request, **kwargs):
    """
    View  /about/
    """
    return render(request, 'about.html')
