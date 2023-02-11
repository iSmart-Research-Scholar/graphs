from graph import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getCitations/',views.getCitations,name='getCitations'),
    path('getReferences/',views.getReferences,name='getReferences'),
    path('nested_citations/',views.nested_citations,name='nested_citations')
]
