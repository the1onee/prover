from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from acount.models import Profile


def doctoer_list(ret):
    doctoer=User.objects.all()
    return render(ret, 'users/doctoers.html', {
       'doctoers':doctoer
    })


def doctoer_detail(ret, slug):
    doctoer_detail=Profile.objects.get(slug = slug)
    return render(ret, 'users/doctoer_detail.html', {
       'doctoer_detail':doctoer_detail
    })