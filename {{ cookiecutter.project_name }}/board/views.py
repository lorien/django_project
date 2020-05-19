from collections import defaultdict
from bson import ObjectId
from datetime import datetime, timedelta
from pprint import pprint
import json
import yaml

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied
from django.urls import reverse

from project.database import db


def page_home(request):
    return render(request, 'board/home_page.html', {
    })
