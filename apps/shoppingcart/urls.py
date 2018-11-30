from django.conf.urls import url

from apps.shoppingcart import views

urlpatterns = [
    url('^addcar/', views.add_car, name='addcar'),
]
