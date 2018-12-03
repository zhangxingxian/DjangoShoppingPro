from django.conf.urls import url

from apps.testdj import views

urlpatterns = [
    url('^testquery/', views.testquery)
]
