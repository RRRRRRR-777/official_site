from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail


def index(request):


    return render(request, 'app/base.html')