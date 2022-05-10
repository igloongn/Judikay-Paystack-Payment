from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import render


def notFound(request):
    return render(request, 'notFound.html', {})
    

urlpatterns = [
    path('', include('core.urls')),
    re_path('.*', notFound ),
    path('admin/', admin.site.urls),
]
