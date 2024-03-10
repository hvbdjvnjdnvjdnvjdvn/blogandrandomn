import logging

from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, World!")


def about(request):
    try:
        # sone code that might raise an exteption
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about pade: {e}')
        return HttpResponse("Dops something went wrond.")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")

# Create your views here.
