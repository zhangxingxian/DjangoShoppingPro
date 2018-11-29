from django.conf.urls import url

from apps.shoppingcart import views

urlpatterns = [
    url('^add/', views.add_car, name='add')
]
