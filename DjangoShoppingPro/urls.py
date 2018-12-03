from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from apps.main import views
import xadmin

urlpatterns = [
                  # url('admin/', admin.site.urls),
                  url('xadmin/', xadmin.site.urls),
                  url('^$', views.index),
                  url('^home/', include('apps.main.urls')),
                  url('shop/', include('apps.detail.urls')),
                  url('search/', include('apps.search.urls')),
                  url('account/', include('apps.account.urls')),
                  url('shopcar/', include('apps.shoppingcart.urls')),
                  url('test/', include('apps.testdj.urls')),
                  url('order/', include('apps.order.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''

from django.conf.urls.static import static
from django.conf import settings

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
是为admin 显示图片用


'''
