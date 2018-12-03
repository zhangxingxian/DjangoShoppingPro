from django.conf.urls import url

from apps.shoppingcart import views

urlpatterns = [
    url('^addcar/', views.add_car, name='addcar'),
    url('^showcar/', views.list, name='showcar'),
    url('confirm/', views.confirm, name='confirm'),
    url(r'order/', views.confirm1, name='order'),
]
