from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Picture.models import ProfilePic

# Create your views here.
def formview(request):
    return render(request, "form.html")

    